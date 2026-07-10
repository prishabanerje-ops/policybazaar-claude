import pytest

from filter_urls import STATE_FIELDS
from state import mark, next_batch, next_batch_cascading, read_state, reset_stale, write_state


def make_row(**overrides):
    row = {field: "" for field in STATE_FIELDS}
    row.update({"status": "pending", **overrides})
    return row


def test_state_roundtrips_through_csv(tmp_path):
    path = tmp_path / "state.csv"
    rows = [make_row(url="https://x/a/", slug="a", tier="A-core")]
    write_state(path, rows)
    assert read_state(path) == rows


def test_next_batch_takes_only_pending_of_requested_tiers():
    rows = [
        make_row(url="u1", tier="A-core"),
        make_row(url="u2", tier="B"),
        make_row(url="u3", tier="A-core", status="done"),
        make_row(url="u4", tier="A-core"),
    ]
    batch = next_batch(rows, size=5, tiers=["A-core"])
    assert [r["url"] for r in batch] == ["u1", "u4"]


def test_mark_raises_when_a_url_is_missing_from_state():
    rows = [make_row(url="u1")]
    with pytest.raises(ValueError):
        mark(rows, ["u1", "ghost"], status="in_progress")


def test_reset_stale_returns_in_progress_rows_without_json_to_pending(tmp_path):
    (tmp_path / "has-json.json").write_text("{}")
    rows = [
        make_row(url="u1", slug="has-json", status="in_progress"),
        make_row(url="u2", slug="no-json", status="in_progress"),
    ]
    assert reset_stale(rows, tmp_path) == 1
    assert rows[0]["status"] == "in_progress"
    assert rows[1]["status"] == "pending"


def test_cascading_batch_falls_through_to_next_tier_when_exhausted():
    rows = [
        make_row(url="u1", tier="A-core"),
        make_row(url="u2", tier="A-articles"),
        make_row(url="u3", tier="A-articles"),
        make_row(url="u4", tier="B"),
    ]
    batch = next_batch_cascading(rows, size=3, start_tier="A-core")
    assert [r["url"] for r in batch] == ["u1", "u2", "u3"]


def test_cascading_batch_stops_at_size_within_first_tier():
    rows = [make_row(url=f"u{i}", tier="A-core") for i in range(5)]
    assert len(next_batch_cascading(rows, size=2, start_tier="A-core")) == 2


def test_cascading_batch_rejects_unknown_tier():
    with pytest.raises(ValueError):
        next_batch_cascading([], size=1, start_tier="A-cor")
