#!/usr/bin/env python3
"""
pbcheck — helpers for auditing Policybazaar UAE /health-insurance/cover/ drafts.

Four subcommands, each replacing a helper that otherwise gets rewritten by hand
every audit:

  status <path...>     HTTP status + final URL for each path. Confirms a new slug
                       is free (404) and every proposed link target is live (200).
  page <path...>       title / description / canonical / H1 / H2 list, with
                       character counts. Used for the draft's own baseline and for
                       reading overlap pages before trusting a disposition label.
  peg <aed...>         Divide AED figures by the USD peg. Round dollar results mean
                       the table is a converted foreign price list, not UAE data.
  count                Read text from stdin, one item per line, and report lengths
                       against the title (<=60) and description (140-160) rules.

Network calls are deliberately slow and serial: policybazaar.ae rate-limits and
has timed out on parallel bursts. Retries once on timeout rather than reporting a
failure that is really just a slow response.
"""
import sys, re, html, json, ssl, argparse, urllib.request, urllib.error

BASE = "https://www.policybazaar.ae"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")
PEG = 3.6725  # AED per USD, pegged

def _ctx():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl.create_default_context()

def _url(p):
    return p if p.startswith("http") else BASE + ("" if p.startswith("/") else "/") + p

def _get(path, timeout=60, cap=400_000):
    """Return (status, final_url, body). status is an int, or a string on failure."""
    url = _url(path)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in (1, 2):
        try:
            r = urllib.request.urlopen(req, timeout=timeout, context=_ctx())
            return r.status, r.url, r.read(cap).decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            return e.code, url, ""
        except Exception as e:
            if attempt == 2:
                return f"ERR:{type(e).__name__}", url, ""
    return "ERR", url, ""

def _meta(body):
    def first(pat):
        m = re.search(pat, body, re.I | re.S)
        return html.unescape(m.group(1).strip()) if m else None
    title = first(r"<title[^>]*>(.*?)</title>")
    desc = (first(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']')
            or first(r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']'))
    canon = first(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']')
    strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()
    h1 = [strip(x) for x in re.findall(r"<h1[^>]*>(.*?)</h1>", body, re.I | re.S)]
    h2 = [strip(x) for x in re.findall(r"<h2[^>]*>(.*?)</h2>", body, re.I | re.S)]
    return title, desc, canon, h1, h2

def cmd_status(paths, as_json):
    out = []
    for p in paths:
        st, final, _ = _get(p, timeout=45, cap=1)
        red = final.replace(BASE, "") if str(st) == "200" and final.rstrip("/") != _url(p).rstrip("/") else ""
        out.append({"path": p, "status": st, "redirect_to": red})
        if not as_json:
            note = f"  REDIR-> {red}" if red else ""
            print(f"{str(st):<8} {p}{note}")
    if as_json:
        print(json.dumps(out, indent=2))

def cmd_page(paths, as_json):
    out = []
    for p in paths:
        st, final, body = _get(p)
        if str(st) != "200":
            print(f"{st}  {p}  (no content)")
            out.append({"path": p, "status": st})
            continue
        t, d, c, h1, h2 = _meta(body)
        rec = {"path": p, "status": st, "title": t, "title_len": len(t) if t else 0,
               "description": d, "description_len": len(d) if d else 0,
               "canonical": c, "h1": h1, "h2": h2}
        out.append(rec)
        if not as_json:
            print("=" * 8, p)
            print(f"  title [{rec['title_len']}] {t}")
            print(f"  desc  [{rec['description_len']}] {d}")
            print(f"  canon {c}")
            print(f"  H1 x{len(h1)}: {h1}")
            print(f"  H2 x{len(h2)}:")
            for x in h2:
                print("     -", x[:88])
    if as_json:
        print(json.dumps(out, indent=2))

def cmd_peg(vals):
    """A converted price list shows up as round USD on both bounds of every row."""
    print(f"{'AED':>12} {'/'+str(PEG):>11}   round USD?")
    hits = 0
    for v in vals:
        n = float(str(v).replace(",", "").replace("AED", "").strip())
        usd = n / PEG
        # round hundreds, or round tens under 1000 (consultation-scale fees)
        rnd = abs(usd - round(usd, -2)) < 1.0 or (usd < 1000 and abs(usd - round(usd, -1)) < 0.5)
        hits += rnd
        print(f"{n:12,.0f} {usd:11,.1f}   {'YES  <-- ' + f'${round(usd):,}' if rnd else 'no'}")
    print(f"\n{hits}/{len(vals)} values resolve to round USD.")
    if vals and hits == len(vals):
        print("VERDICT: every value is round USD. This is a converted foreign price list,\n"
              "         not UAE provider data. Hard publish blocker under Decision 4.")
    elif hits > len(vals) * 0.6:
        print("VERDICT: most values resolve to round USD. Treat as converted until sourced.")
    else:
        print("VERDICT: no clear peg pattern. Still needs a named source + capture date.")

def cmd_count():
    for line in sys.stdin.read().splitlines():
        s = line.strip()
        if not s:
            continue
        n = len(s)
        # 60 is the title ceiling before the " | Policybazaar.ae" suffix; 140-160 desc
        verdict = "title OK" if n <= 60 else ("desc OK" if 140 <= n <= 160 else "CHECK")
        print(f"[{n:3}] {verdict:<9} {s}")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["status", "page", "peg", "count"])
    ap.add_argument("args", nargs="*")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    a = ap.parse_args()
    if a.cmd == "status":
        cmd_status(a.args, a.json)
    elif a.cmd == "page":
        cmd_page(a.args, a.json)
    elif a.cmd == "peg":
        cmd_peg(a.args)
    else:
        cmd_count()

if __name__ == "__main__":
    main()
