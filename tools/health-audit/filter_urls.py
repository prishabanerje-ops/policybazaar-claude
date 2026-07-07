"""Build the health-insurance audit URL set and initialise audit-state.csv."""
import csv
import sys

from config import STATE_CSV, URLS_TXT

STATE_FIELDS = [
    "url", "slug", "page_type", "tier", "status",
    "seo", "geo", "human_likeness", "ymyl", "fact_check", "overall",
    "md_file", "json_file", "audit_date", "batch_id", "failure_reason",
]

SUFFIX_RULES = [
    ("-hipvd/", "provider", "A-core"),
    ("-hiart/", "article", "A-articles"),
    ("-hic/", "category", "A-core"),
    ("-hinh/", "hospital-listing", "B"),
    ("-hicf/", "claim-form", "B"),
]

PATH_RULES = [
    ("/network-hospitals/", "hospital-listing", "B"),
    ("/health-insurance/hospitals/", "hospital-listing", "B"),
    ("/health-insurance/glossary/", "glossary", "B"),
    ("/health-insurance/news-and-update/", "news", "B"),
    ("/health-insurance/articles/", "article", "A-articles"),
    ("/health-insurance/tpa/", "tpa", "A-core"),
    ("/health-insurance/health-guide/", "health-guide", "A-core"),
]


def classify(url):
    """Return (page_type, tier), or None when the URL is out of scope."""
    if "/ar-ae/" in url:
        return None
    for suffix, page_type, tier in SUFFIX_RULES:
        if url.endswith(suffix):
            return page_type, tier
    for fragment, page_type, tier in PATH_RULES:
        if fragment in url:
            return page_type, tier
    if "/health-insurance/" in url:
        return "core-page", "A-core"
    return None


def make_slug(url, taken):
    """Last path segment; on collision prefix the parent segment."""
    path = url.split("policybazaar.ae", 1)[-1]
    segments = [s for s in path.split("/") if s]
    slug = segments[-1]
    if slug in taken and len(segments) >= 2:
        slug = f"{segments[-2]}-{segments[-1]}"
    if slug in taken:
        raise ValueError(f"slug collision unresolved for {url}: {slug!r} already taken")
    return slug


def build_rows(urls):
    rows = []
    taken = set()
    for url in sorted({u.strip() for u in urls if u.strip()}):
        result = classify(url)
        if result is None:
            continue
        page_type, tier = result
        slug = make_slug(url, taken)
        taken.add(slug)
        row = {field: "" for field in STATE_FIELDS}
        row.update(url=url, slug=slug, page_type=page_type, tier=tier, status="pending")
        rows.append(row)
    return rows


def main(force=False):
    if STATE_CSV.exists() and not force:
        sys.exit(
            f"{STATE_CSV} already exists — refusing to overwrite a live audit state. "
            "Re-run with --force to rebuild from scratch."
        )
    rows = build_rows(URLS_TXT.read_text().splitlines())
    STATE_CSV.parent.mkdir(parents=True, exist_ok=True)
    with STATE_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=STATE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {STATE_CSV}")


if __name__ == "__main__":
    main(force="--force" in sys.argv)
