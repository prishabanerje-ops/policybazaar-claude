"""Read/update audit-state.csv — the resumable backbone of the audit run."""
import csv
import json
import sys
from collections import Counter
from pathlib import Path

from filter_urls import STATE_FIELDS


def read_state(path):
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def write_state(path, rows):
    with open(path, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=STATE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def next_batch(rows, size, tiers=None):
    pending = [
        r for r in rows
        if r["status"] == "pending" and (tiers is None or r["tier"] in tiers)
    ]
    return pending[:size]


TIER_PRIORITY = ["A-core", "A-articles", "B"]


def next_batch_cascading(rows, size, start_tier):
    """Fill a batch starting at start_tier, falling through the tier priority order."""
    if start_tier not in TIER_PRIORITY:
        raise ValueError(
            f"unknown tier {start_tier!r} — expected one of {TIER_PRIORITY}"
        )
    batch = []
    for tier in TIER_PRIORITY[TIER_PRIORITY.index(start_tier):]:
        batch.extend(next_batch(rows, size - len(batch), [tier]))
        if len(batch) >= size:
            break
    return batch


def mark(rows, urls, **updates):
    urls = set(urls)
    hit = 0
    for row in rows:
        if row["url"] in urls:
            row.update({k: str(v) for k, v in updates.items()})
            hit += 1
    if hit != len(urls):
        raise ValueError(
            f"mark() matched {hit} of {len(urls)} urls — batch and state file are out of sync"
        )
    return rows


def reset_stale(rows, audit_data_dir):
    """in_progress rows with no JSON on disk died mid-run — return them to pending."""
    audit_data_dir = Path(audit_data_dir)
    count = 0
    for row in rows:
        if row["status"] == "in_progress" and not (audit_data_dir / f"{row['slug']}.json").exists():
            row["status"] = "pending"
            count += 1
    return count


if __name__ == "__main__":
    from config import AUDIT_DATA_DIR, STATE_CSV

    rows = read_state(STATE_CSV)
    cmd = sys.argv[1] if len(sys.argv) > 1 else "summary"
    if cmd == "summary":
        print(Counter(r["status"] for r in rows))
        print(Counter((r["tier"], r["status"]) for r in rows))
    elif cmd == "reset-stale":
        n = reset_stale(rows, AUDIT_DATA_DIR)
        write_state(STATE_CSV, rows)
        print(f"reset {n} stale rows to pending")
    elif cmd == "take":
        size = int(sys.argv[2])
        batch_id = sys.argv[4] if len(sys.argv) > 4 else "batch"
        if len(sys.argv) > 3:
            batch = next_batch_cascading(rows, size, sys.argv[3])
        else:
            batch = next_batch(rows, size)
        mark(rows, [r["url"] for r in batch], status="in_progress", batch_id=batch_id)
        write_state(STATE_CSV, rows)
        print(json.dumps(
            [{k: r[k] for k in ("url", "slug", "page_type", "tier")} for r in batch]
        ))
    elif cmd == "fail":
        mark(rows, [sys.argv[2]], status="failed", failure_reason=sys.argv[3])
        write_state(STATE_CSV, rows)
        print(f"marked failed: {sys.argv[2]}")
    else:
        sys.exit(f"unknown command {cmd!r} — use summary | reset-stale | take | fail")
