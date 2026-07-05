# LinkedIn Image Post Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the `post-linkedin` skill so it can publish a single image alongside a post, with the image generated for free (no API key) from the post's own text.

**Architecture:** A new stdlib-only module `linkedin_image.py` handles both free image generation (Pollinations keyless HTTP GET) and the modern LinkedIn Images API upload (`/rest/images` → PUT → `urn:li:image:…`). The existing `linkedin_post.py` gains `--image`/`--alt-text` flags and imports the upload helper; the text-only path is unchanged. Image generation is run as a **separate, previewable step** (CLI of `linkedin_image.py`), so the posting script only ever receives a file path.

**Tech Stack:** Python 3 standard library only (`urllib`, `argparse`, `json`, `pathlib`, `time`). pytest 9.0.3 + `monkeypatch` for unit tests. No `requests`, no `google-genai`, no API keys.

## Global Constraints

- **Repo root:** `~/.claude/skills/post-linkedin/`. All file paths below are relative to this directory unless absolute. All `git` commands run from here.
- **Stdlib only.** No new pip dependencies in shipped code (`linkedin_image.py`, `linkedin_post.py`). pytest is a dev/test dependency only.
- **No API keys for image generation.** Pollinations is keyless. LinkedIn auth continues to come from `~/.config/linkedin-api.env` (`LINKEDIN_ACCESS_TOKEN`, `LINKEDIN_PERSON_ID`).
- **LinkedIn API version:** `202506` (string constant `LINKEDIN_VERSION`). Reused for both `/rest/images` and `/rest/posts`. Also send `X-Restli-Protocol-Version: 2.0.0`.
- **Pollinations resolution is 768×768** and `width`/`height` are ignored — never claim or request other sizes. `seed=<int>` is honored.
- **Fail-loud.** Never fabricate success. Generation/upload/post errors raise or return `{"status":"error","detail":...}` with the real HTTP status/body; a post is "published" only on `/rest/posts` 201 with a returned id.
- **Image limits:** PNG/JPEG only, `< 5 MB`.
- **Commit message trailer:** every commit ends with `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- **Spec:** `~/.claude/docs/superpowers/specs/2026-06-26-linkedin-image-post-design.md`.

---

### Task 1: Test scaffolding + git baseline

**Files:**
- Create: `.gitignore`
- Create: `scripts/tests/__init__.py` (empty)
- Create: `scripts/tests/conftest.py`
- (git init the repo root)

**Interfaces:**
- Consumes: nothing.
- Produces: a git repo at the skill root; a `scripts/tests/` package whose `conftest.py` puts `scripts/` on `sys.path` so `import linkedin_image` / `import linkedin_post` work in tests.

- [ ] **Step 1: Initialize the git repo and a .gitignore**

Run from repo root:
```bash
cd ~/.claude/skills/post-linkedin
git init
```

Create `.gitignore`:
```gitignore
__pycache__/
*.pyc
.pytest_cache/
.DS_Store
*.generated.jpg
```

- [ ] **Step 2: Create the test package and conftest**

Create `scripts/tests/__init__.py` (empty file).

Create `scripts/tests/conftest.py`:
```python
import sys
from pathlib import Path

# Put the scripts/ dir on sys.path so tests can import the modules under test.
SCRIPTS_DIR = Path(__file__).resolve().parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
```

- [ ] **Step 3: Verify pytest collects with no errors**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/ -q`
Expected: `no tests ran` (exit code 5) — collection succeeds, zero tests. This confirms the test harness imports cleanly.

- [ ] **Step 4: Commit the baseline**

```bash
cd ~/.claude/skills/post-linkedin
git add -A
git commit -m "chore: init git, add test scaffolding for image-post work

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 2: Pollinations image generation (`linkedin_image.py`)

**Files:**
- Create: `scripts/linkedin_image.py`
- Test: `scripts/tests/test_linkedin_image_generate.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `class ImageGenError(Exception)`
  - `build_pollinations_url(prompt: str, seed: int | None = None) -> str`
  - `generate(prompt: str, out_path: str, seed: int | None = None, timeout: int = 100) -> str` (returns `out_path`; raises `ImageGenError`)

- [ ] **Step 1: Write the failing tests**

Create `scripts/tests/test_linkedin_image_generate.py`:
```python
import io
import urllib.error
import urllib.request

import linkedin_image as li


class FakeResp:
    def __init__(self, data=b"", headers=None, status=200):
        self._data = data
        self.headers = headers or {}
        self.status = status
    def read(self):
        return self._data
    def __enter__(self):
        return self
    def __exit__(self, *a):
        return False


def test_build_url_encodes_and_adds_nologo():
    url = li.build_pollinations_url("a cat, in space")
    assert url.startswith("https://image.pollinations.ai/prompt/")
    assert "a%20cat%2C%20in%20space" in url
    assert "nologo=true" in url
    assert "seed=" not in url


def test_build_url_includes_seed_when_given():
    url = li.build_pollinations_url("x", seed=42)
    assert "seed=42" in url


def test_generate_writes_image_bytes(tmp_path, monkeypatch):
    out = tmp_path / "img.jpg"
    resp = FakeResp(data=b"\xff\xd8\xff_fakejpeg",
                    headers={"Content-Type": "image/jpeg"})
    monkeypatch.setattr(urllib.request, "urlopen", lambda req, timeout=None: resp)
    result = li.generate("prompt", str(out))
    assert result == str(out)
    assert out.read_bytes() == b"\xff\xd8\xff_fakejpeg"


def test_generate_raises_on_non_image_content_type(tmp_path, monkeypatch):
    resp = FakeResp(data=b"<html>error</html>",
                    headers={"Content-Type": "text/html"})
    monkeypatch.setattr(urllib.request, "urlopen", lambda req, timeout=None: resp)
    try:
        li.generate("prompt", str(tmp_path / "img.jpg"))
        assert False, "expected ImageGenError"
    except li.ImageGenError as e:
        assert "Content-Type" in str(e)


def test_generate_raises_on_http_error(tmp_path, monkeypatch):
    def boom(req, timeout=None):
        raise urllib.error.HTTPError("u", 429, "Too Many", {}, io.BytesIO(b"quota"))
    monkeypatch.setattr(urllib.request, "urlopen", boom)
    try:
        li.generate("prompt", str(tmp_path / "img.jpg"))
        assert False, "expected ImageGenError"
    except li.ImageGenError as e:
        assert "429" in str(e)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/test_linkedin_image_generate.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'linkedin_image'`.

- [ ] **Step 3: Write the minimal implementation**

Create `scripts/linkedin_image.py`:
```python
#!/usr/bin/env python3
"""Image generation (Pollinations, keyless) + LinkedIn Images API upload.

Stdlib only. Used by linkedin_post.py for uploads; runnable as a CLI for
generation.
"""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request


POLLINATIONS_BASE = "https://image.pollinations.ai/prompt/"


class ImageGenError(Exception):
    pass


def build_pollinations_url(prompt, seed=None):
    enc = urllib.parse.quote(prompt, safe="")
    url = f"{POLLINATIONS_BASE}{enc}?nologo=true"
    if seed is not None:
        url += f"&seed={seed}"
    return url


def generate(prompt, out_path, seed=None, timeout=100):
    """Generate an image via Pollinations and write it to out_path.

    Returns out_path on success. Raises ImageGenError on any failure.
    Note: the free model caps output at 768x768; size params are ignored.
    """
    url = build_pollinations_url(prompt, seed)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ctype = resp.headers.get("Content-Type", "")
            data = resp.read()
    except urllib.error.HTTPError as e:
        body = e.read()[:200] if hasattr(e, "read") else b""
        raise ImageGenError(f"Pollinations HTTP {e.code}: {body!r}")
    except urllib.error.URLError as e:
        raise ImageGenError(f"Pollinations request failed: {e.reason}")
    if not ctype.startswith("image/"):
        raise ImageGenError(
            f"Expected image, got Content-Type={ctype!r}; body[:200]={data[:200]!r}"
        )
    if not data:
        raise ImageGenError("Pollinations returned an empty body")
    with open(out_path, "wb") as f:
        f.write(data)
    return out_path
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/test_linkedin_image_generate.py -v`
Expected: 5 passed.

- [ ] **Step 5: Commit**

```bash
cd ~/.claude/skills/post-linkedin
git add scripts/linkedin_image.py scripts/tests/test_linkedin_image_generate.py
git commit -m "feat: add keyless Pollinations image generation

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 3: LinkedIn Images API upload (`linkedin_image.py`)

**Files:**
- Modify: `scripts/linkedin_image.py` (append upload functions)
- Test: `scripts/tests/test_linkedin_image_upload.py`

**Interfaces:**
- Consumes: nothing from earlier tasks (same module).
- Produces:
  - `class ImageUploadError(Exception)`
  - `initialize_upload(person_urn: str, token: str, version: str) -> tuple[str, str]` → `(upload_url, image_urn)`
  - `put_image_bytes(upload_url: str, image_path: str, token: str) -> int` → HTTP status
  - `upload_image(image_path: str, person_urn: str, token: str, version: str) -> str` → image URN

> **Verify-against-docs note:** the request/response field names for `/rest/images?action=initializeUpload` (`initializeUploadRequest.owner`, `value.uploadUrl`, `value.image`) match the documented modern flow but must be confirmed by the real test post in Task 9. If LinkedIn returns a different shape, adjust the parsing in `initialize_upload` and update this plan.

- [ ] **Step 1: Write the failing tests**

Create `scripts/tests/test_linkedin_image_upload.py`:
```python
import io
import json
import urllib.error
import urllib.request

import linkedin_image as li


class FakeResp:
    def __init__(self, data=b"", status=200):
        self._data = data
        self.status = status
    def read(self):
        return self._data
    def __enter__(self):
        return self
    def __exit__(self, *a):
        return False


def test_initialize_upload_parses_url_and_urn(monkeypatch):
    payload = {"value": {"uploadUrl": "https://up.example/abc",
                         "image": "urn:li:image:C123"}}
    monkeypatch.setattr(urllib.request, "urlopen",
                        lambda req: FakeResp(json.dumps(payload).encode()))
    url, urn = li.initialize_upload("urn:li:person:P1", "tok", "202506")
    assert url == "https://up.example/abc"
    assert urn == "urn:li:image:C123"


def test_initialize_upload_raises_on_missing_fields(monkeypatch):
    monkeypatch.setattr(urllib.request, "urlopen",
                        lambda req: FakeResp(json.dumps({"value": {}}).encode()))
    try:
        li.initialize_upload("urn:li:person:P1", "tok", "202506")
        assert False, "expected ImageUploadError"
    except li.ImageUploadError as e:
        assert "uploadUrl" in str(e) or "image" in str(e)


def test_initialize_upload_raises_on_http_error(monkeypatch):
    def boom(req):
        raise urllib.error.HTTPError("u", 403, "Forbidden", {}, io.BytesIO(b"no scope"))
    monkeypatch.setattr(urllib.request, "urlopen", boom)
    try:
        li.initialize_upload("urn:li:person:P1", "tok", "202506")
        assert False, "expected ImageUploadError"
    except li.ImageUploadError as e:
        assert "403" in str(e)


def test_put_image_bytes_ok(tmp_path, monkeypatch):
    img = tmp_path / "x.jpg"
    img.write_bytes(b"\xff\xd8\xff_data")
    monkeypatch.setattr(urllib.request, "urlopen", lambda req: FakeResp(status=201))
    status = li.put_image_bytes("https://up.example/abc", str(img), "tok")
    assert status == 201


def test_put_image_bytes_raises_on_http_error(tmp_path, monkeypatch):
    img = tmp_path / "x.jpg"
    img.write_bytes(b"data")
    def boom(req):
        raise urllib.error.HTTPError("u", 400, "Bad", {}, io.BytesIO(b"bad upload"))
    monkeypatch.setattr(urllib.request, "urlopen", boom)
    try:
        li.put_image_bytes("https://up.example/abc", str(img), "tok")
        assert False, "expected ImageUploadError"
    except li.ImageUploadError as e:
        assert "400" in str(e)


def test_upload_image_orchestrates(tmp_path, monkeypatch):
    img = tmp_path / "x.jpg"
    img.write_bytes(b"\xff\xd8\xff_data")
    monkeypatch.setattr(li, "initialize_upload",
                        lambda person, tok, ver: ("https://up.example/abc", "urn:li:image:C9"))
    monkeypatch.setattr(li, "put_image_bytes",
                        lambda url, path, tok: 201)
    urn = li.upload_image(str(img), "urn:li:person:P1", "tok", "202506")
    assert urn == "urn:li:image:C9"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/test_linkedin_image_upload.py -v`
Expected: FAIL — `AttributeError: module 'linkedin_image' has no attribute 'initialize_upload'`.

- [ ] **Step 3: Append the implementation to `scripts/linkedin_image.py`**

Add after the `generate` function:
```python
LINKEDIN_API = "https://api.linkedin.com"


class ImageUploadError(Exception):
    pass


def initialize_upload(person_urn, token, version):
    """Register an image upload. Returns (upload_url, image_urn)."""
    url = f"{LINKEDIN_API}/rest/images?action=initializeUpload"
    body = json.dumps({"initializeUploadRequest": {"owner": person_urn}}).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "LinkedIn-Version": version,
        "X-Restli-Protocol-Version": "2.0.0",
    }
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise ImageUploadError(f"initializeUpload HTTP {e.code}: {detail}")
    except urllib.error.URLError as e:
        raise ImageUploadError(f"initializeUpload request failed: {e.reason}")
    value = payload.get("value", {})
    upload_url = value.get("uploadUrl")
    image_urn = value.get("image")
    if not upload_url or not image_urn:
        raise ImageUploadError(
            f"initializeUpload response missing uploadUrl/image: {payload}"
        )
    return upload_url, image_urn


def put_image_bytes(upload_url, image_path, token):
    """PUT raw image bytes to the upload URL. Returns the HTTP status."""
    with open(image_path, "rb") as f:
        data = f.read()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/octet-stream",
    }
    req = urllib.request.Request(upload_url, data=data, headers=headers, method="PUT")
    try:
        with urllib.request.urlopen(req) as resp:
            status = resp.status
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise ImageUploadError(f"image PUT HTTP {e.code}: {detail}")
    except urllib.error.URLError as e:
        raise ImageUploadError(f"image PUT request failed: {e.reason}")
    if status not in (200, 201):
        raise ImageUploadError(f"image PUT unexpected status {status}")
    return status


def upload_image(image_path, person_urn, token, version):
    """Full upload: initialize -> PUT bytes. Returns the image URN."""
    upload_url, image_urn = initialize_upload(person_urn, token, version)
    put_image_bytes(upload_url, image_path, token)
    return image_urn
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/test_linkedin_image_upload.py -v`
Expected: 6 passed.

- [ ] **Step 5: Commit**

```bash
cd ~/.claude/skills/post-linkedin
git add scripts/linkedin_image.py scripts/tests/test_linkedin_image_upload.py
git commit -m "feat: add modern /rest/images upload flow

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 4: Generation CLI (`linkedin_image.py`)

**Files:**
- Modify: `scripts/linkedin_image.py` (add `cli_main` + `__main__` guard)
- Test: `scripts/tests/test_linkedin_image_cli.py`

**Interfaces:**
- Consumes: `generate`, `ImageGenError` from Task 2.
- Produces: `cli_main(argv: list[str]) -> int` (returns exit code; prints a JSON line). Invoked as `python3 linkedin_image.py --prompt "<text>" --out <path> [--seed <int>]`.

- [ ] **Step 1: Write the failing tests**

Create `scripts/tests/test_linkedin_image_cli.py`:
```python
import json

import linkedin_image as li


def test_cli_success_prints_path(tmp_path, monkeypatch, capsys):
    out = tmp_path / "img.jpg"
    monkeypatch.setattr(li, "generate",
                        lambda prompt, out_path, seed=None: out_path)
    code = li.cli_main(["--prompt", "a robot", "--out", str(out)])
    assert code == 0
    printed = json.loads(capsys.readouterr().out.strip())
    assert printed["status"] == "success"
    assert printed["path"] == str(out)


def test_cli_error_returns_1(tmp_path, monkeypatch, capsys):
    def boom(prompt, out_path, seed=None):
        raise li.ImageGenError("boom 429")
    monkeypatch.setattr(li, "generate", boom)
    code = li.cli_main(["--prompt", "x", "--out", str(tmp_path / "i.jpg")])
    assert code == 1
    printed = json.loads(capsys.readouterr().out.strip())
    assert printed["status"] == "error"
    assert "boom 429" in printed["detail"]


def test_cli_passes_seed(tmp_path, monkeypatch):
    seen = {}
    monkeypatch.setattr(li, "generate",
                        lambda prompt, out_path, seed=None: seen.setdefault("seed", seed) or out_path)
    li.cli_main(["--prompt", "x", "--out", str(tmp_path / "i.jpg"), "--seed", "7"])
    assert seen["seed"] == 7
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/test_linkedin_image_cli.py -v`
Expected: FAIL — `AttributeError: module 'linkedin_image' has no attribute 'cli_main'`.

- [ ] **Step 3: Add the CLI to `scripts/linkedin_image.py`**

Add `import argparse` to the imports at the top, then append at the end of the file:
```python
def cli_main(argv):
    parser = argparse.ArgumentParser(
        description="Generate an image via Pollinations (keyless, free)."
    )
    parser.add_argument("--prompt", required=True, help="Image generation prompt")
    parser.add_argument("--out", required=True, help="Output file path (.jpg)")
    parser.add_argument("--seed", type=int, default=None,
                        help="Optional integer seed for reproducibility")
    args = parser.parse_args(argv)
    try:
        path = generate(args.prompt, args.out, seed=args.seed)
        print(json.dumps({"status": "success", "path": path}))
        return 0
    except ImageGenError as e:
        print(json.dumps({"status": "error", "detail": str(e)}))
        return 1


if __name__ == "__main__":
    sys.exit(cli_main(sys.argv[1:]))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/test_linkedin_image_cli.py -v`
Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
cd ~/.claude/skills/post-linkedin
git add scripts/linkedin_image.py scripts/tests/test_linkedin_image_cli.py
git commit -m "feat: add generation CLI to linkedin_image

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 5: Post-payload helpers in `linkedin_post.py` (version constant, validation, payload builder)

**Files:**
- Modify: `scripts/linkedin_post.py`
- Test: `scripts/tests/test_linkedin_post_helpers.py`

**Context — current `linkedin_post.py` (92 lines):** module constant `ENV_FILE`; functions `load_env(path)`, `post_to_linkedin(text, token, person_id)` (builds the `/rest/posts` payload inline with `"LinkedIn-Version": "202506"` hardcoded in the headers at the POST), and `main()`. This task does **not** touch `main()` or the network call yet.

**Interfaces:**
- Consumes: nothing.
- Produces:
  - module constant `LINKEDIN_VERSION = "202506"`
  - module constants `SUPPORTED_IMAGE_EXT = {".png", ".jpg", ".jpeg"}`, `MAX_IMAGE_BYTES = 5 * 1024 * 1024`
  - `validate_image(path: str) -> None` (raises `FileNotFoundError` or `ValueError`)
  - `build_post_payload(text: str, person_id: str, image_urn: str | None = None, alt_text: str | None = None) -> dict`

- [ ] **Step 1: Write the failing tests**

Create `scripts/tests/test_linkedin_post_helpers.py`:
```python
import pytest

import linkedin_post as lp


def test_payload_text_only_has_no_content():
    p = lp.build_post_payload("hello world", "PERSON123")
    assert p["author"] == "urn:li:person:PERSON123"
    assert p["commentary"] == "hello world"
    assert p["lifecycleState"] == "PUBLISHED"
    assert p["visibility"] == "PUBLIC"
    assert "content" not in p


def test_payload_with_image_adds_media():
    p = lp.build_post_payload("hi", "P1", image_urn="urn:li:image:C9", alt_text="a chart")
    assert p["content"] == {"media": {"id": "urn:li:image:C9", "altText": "a chart"}}


def test_payload_with_image_defaults_alt_text_to_empty():
    p = lp.build_post_payload("hi", "P1", image_urn="urn:li:image:C9")
    assert p["content"]["media"]["altText"] == ""


def test_validate_image_ok(tmp_path):
    img = tmp_path / "ok.jpg"
    img.write_bytes(b"\xff\xd8\xff" + b"0" * 100)
    lp.validate_image(str(img))  # should not raise


def test_validate_image_missing(tmp_path):
    with pytest.raises(FileNotFoundError):
        lp.validate_image(str(tmp_path / "nope.jpg"))


def test_validate_image_wrong_ext(tmp_path):
    bad = tmp_path / "x.gif"
    bad.write_bytes(b"GIF89a")
    with pytest.raises(ValueError):
        lp.validate_image(str(bad))


def test_validate_image_too_large(tmp_path):
    big = tmp_path / "big.png"
    big.write_bytes(b"0" * (5 * 1024 * 1024 + 1))
    with pytest.raises(ValueError):
        lp.validate_image(str(big))
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/test_linkedin_post_helpers.py -v`
Expected: FAIL — `AttributeError: module 'linkedin_post' has no attribute 'build_post_payload'`.

- [ ] **Step 3: Add constants + helpers to `scripts/linkedin_post.py`**

Add `from pathlib import Path` if not already imported (it is). Add near the top, after the existing `ENV_FILE` constant:
```python
LINKEDIN_VERSION = "202506"
SUPPORTED_IMAGE_EXT = {".png", ".jpg", ".jpeg"}
MAX_IMAGE_BYTES = 5 * 1024 * 1024  # 5 MB
```

Add these two functions (above `post_to_linkedin`):
```python
def validate_image(path):
    """Raise if path is not an existing PNG/JPEG file under 5 MB."""
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"Image not found: {path}")
    if p.suffix.lower() not in SUPPORTED_IMAGE_EXT:
        raise ValueError(
            f"Unsupported image type '{p.suffix}'; use PNG or JPEG"
        )
    size = p.stat().st_size
    if size >= MAX_IMAGE_BYTES:
        raise ValueError(f"Image too large ({size} bytes); must be < 5 MB")


def build_post_payload(text, person_id, image_urn=None, alt_text=None):
    """Build the /rest/posts request body. Adds content.media iff image_urn."""
    payload = {
        "author": f"urn:li:person:{person_id}",
        "lifecycleState": "PUBLISHED",
        "visibility": "PUBLIC",
        "commentary": text,
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
    }
    if image_urn:
        payload["content"] = {"media": {"id": image_urn, "altText": alt_text or ""}}
    return payload
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/test_linkedin_post_helpers.py -v`
Expected: 7 passed.

- [ ] **Step 5: Commit**

```bash
cd ~/.claude/skills/post-linkedin
git add scripts/linkedin_post.py scripts/tests/test_linkedin_post_helpers.py
git commit -m "feat: add image validation + payload builder helpers

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 6: Wire `post_to_linkedin` to the builder + retry-with-backoff

**Files:**
- Modify: `scripts/linkedin_post.py`
- Test: `scripts/tests/test_linkedin_post_retry.py`

**Context:** the current `post_to_linkedin(text, token, person_id)` builds the payload inline and sends it, returning `{"status": "success", "post_id": ..., "http_status": ...}` or `{"status": "error", "http_status": ..., "detail": ...}`. We refactor it to (a) accept `image_urn`/`alt_text` and use `build_post_payload`, and (b) keep using `LINKEDIN_VERSION`. Then add `post_with_retry`.

**Interfaces:**
- Consumes: `build_post_payload`, `LINKEDIN_VERSION` (Task 5).
- Produces:
  - `post_to_linkedin(text, token, person_id, image_urn=None, alt_text=None) -> dict` (refactored signature)
  - `_is_media_not_ready(result: dict) -> bool`
  - `post_with_retry(text, token, person_id, image_urn=None, alt_text=None, attempts=3, delay=2) -> dict`

- [ ] **Step 1: Write the failing tests**

Create `scripts/tests/test_linkedin_post_retry.py`:
```python
import linkedin_post as lp


def test_retry_returns_success_first_try(monkeypatch):
    calls = {"n": 0}
    def fake_post(text, token, person_id, image_urn=None, alt_text=None):
        calls["n"] += 1
        return {"status": "success", "post_id": "urn:li:share:1", "http_status": 201}
    monkeypatch.setattr(lp, "post_to_linkedin", fake_post)
    monkeypatch.setattr(lp.time, "sleep", lambda s: None)
    result = lp.post_with_retry("t", "tok", "P1", image_urn="urn:li:image:C9")
    assert result["status"] == "success"
    assert calls["n"] == 1


def test_retry_on_media_not_ready_then_succeeds(monkeypatch):
    seq = [
        {"status": "error", "http_status": 422, "detail": "media not ready: urn:li:image:C9"},
        {"status": "success", "post_id": "urn:li:share:2", "http_status": 201},
    ]
    calls = {"n": 0}
    def fake_post(text, token, person_id, image_urn=None, alt_text=None):
        r = seq[calls["n"]]
        calls["n"] += 1
        return r
    monkeypatch.setattr(lp, "post_to_linkedin", fake_post)
    monkeypatch.setattr(lp.time, "sleep", lambda s: None)
    result = lp.post_with_retry("t", "tok", "P1", image_urn="urn:li:image:C9")
    assert result["status"] == "success"
    assert calls["n"] == 2


def test_no_retry_when_no_image(monkeypatch):
    calls = {"n": 0}
    def fake_post(text, token, person_id, image_urn=None, alt_text=None):
        calls["n"] += 1
        return {"status": "error", "http_status": 400, "detail": "bad text"}
    monkeypatch.setattr(lp, "post_to_linkedin", fake_post)
    monkeypatch.setattr(lp.time, "sleep", lambda s: None)
    result = lp.post_with_retry("t", "tok", "P1")
    assert result["status"] == "error"
    assert calls["n"] == 1


def test_retry_gives_up_after_attempts(monkeypatch):
    calls = {"n": 0}
    def fake_post(text, token, person_id, image_urn=None, alt_text=None):
        calls["n"] += 1
        return {"status": "error", "http_status": 422, "detail": "image still processing"}
    monkeypatch.setattr(lp, "post_to_linkedin", fake_post)
    monkeypatch.setattr(lp.time, "sleep", lambda s: None)
    result = lp.post_with_retry("t", "tok", "P1", image_urn="urn:li:image:C9", attempts=3)
    assert result["status"] == "error"
    assert calls["n"] == 3
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/test_linkedin_post_retry.py -v`
Expected: FAIL — `AttributeError: module 'linkedin_post' has no attribute 'post_with_retry'` (and/or no attribute `time`).

- [ ] **Step 3: Refactor `post_to_linkedin` and add retry**

Add `import time` to the top imports.

Replace the body of `post_to_linkedin` so it accepts the new params and uses `build_post_payload` + `LINKEDIN_VERSION`. The function becomes:
```python
def post_to_linkedin(text, token, person_id, image_urn=None, alt_text=None):
    url = "https://api.linkedin.com/rest/posts"
    payload = build_post_payload(text, person_id, image_urn=image_urn, alt_text=alt_text)
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "LinkedIn-Version": LINKEDIN_VERSION,
        "X-Restli-Protocol-Version": "2.0.0",
    }
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            location = resp.headers.get("x-restli-id") or resp.headers.get("Location", "")
            return {"status": "success", "post_id": location, "http_status": resp.status}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"status": "error", "http_status": e.code, "detail": body}
```

Add after `post_to_linkedin`:
```python
def _is_media_not_ready(result):
    """Heuristic: did the post fail because the image asset isn't queryable yet?"""
    detail = str(result.get("detail", "")).lower()
    return any(k in detail for k in ("media", "image", "asset", "processing", "not ready"))


def post_with_retry(text, token, person_id, image_urn=None, alt_text=None,
                    attempts=3, delay=2):
    """Post, retrying only the image-URN race (image present + media-not-ready)."""
    result = None
    for i in range(attempts):
        result = post_to_linkedin(text, token, person_id, image_urn, alt_text)
        if result["status"] == "success":
            return result
        if not (image_urn and _is_media_not_ready(result)):
            return result
        if i < attempts - 1:
            time.sleep(delay)
    return result
```

- [ ] **Step 4: Run all tests to verify pass (retry + earlier helper tests still green)**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/test_linkedin_post_retry.py scripts/tests/test_linkedin_post_helpers.py -v`
Expected: 4 + 7 = 11 passed. (Confirms the `post_to_linkedin` refactor didn't break the helper contract.)

- [ ] **Step 5: Commit**

```bash
cd ~/.claude/skills/post-linkedin
git add scripts/linkedin_post.py scripts/tests/test_linkedin_post_retry.py
git commit -m "feat: media-aware post payload + retry-with-backoff for URN race

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 7: Arg parsing + `main()` wiring (with text-only regression)

**Files:**
- Modify: `scripts/linkedin_post.py`
- Test: `scripts/tests/test_linkedin_post_main.py`

**Context:** the current `main()` reads text from `sys.argv[1:]` (joined) or stdin, loads env, and calls `post_to_linkedin`. We replace argv handling with `argparse` while preserving both the positional-text and stdin paths, and we wire in image upload.

**Interfaces:**
- Consumes: `validate_image`, `LINKEDIN_VERSION` (Task 5); `post_with_retry` (Task 6); `linkedin_image.upload_image`, `linkedin_image.ImageUploadError` (Task 3).
- Produces:
  - `parse_args(argv: list[str]) -> argparse.Namespace` (`.text` list, `.image`, `.alt_text`)
  - `get_post_text(args) -> str`
  - refactored `main(argv=None) -> None`

- [ ] **Step 1: Write the failing tests**

Create `scripts/tests/test_linkedin_post_main.py`:
```python
import io

import linkedin_post as lp


def test_parse_args_positional_text():
    args = lp.parse_args(["hello", "world"])
    assert args.text == ["hello", "world"]
    assert args.image is None
    assert args.alt_text is None


def test_parse_args_flags():
    args = lp.parse_args(["--image", "/tmp/x.jpg", "--alt-text", "a chart"])
    assert args.image == "/tmp/x.jpg"
    assert args.alt_text == "a chart"
    assert args.text == []


def test_get_post_text_prefers_positional():
    args = lp.parse_args(["hello", "there"])
    assert lp.get_post_text(args) == "hello there"


def test_get_post_text_falls_back_to_stdin(monkeypatch):
    args = lp.parse_args([])
    monkeypatch.setattr("sys.stdin", io.StringIO("from stdin\n"))
    assert lp.get_post_text(args) == "from stdin"


def test_main_text_only_does_not_upload(monkeypatch, tmp_path):
    # Regression: no --image means no image upload and no content.media.
    env = tmp_path / "linkedin-api.env"
    env.write_text("LINKEDIN_ACCESS_TOKEN=tok\nLINKEDIN_PERSON_ID=P1\n")
    monkeypatch.setattr(lp, "ENV_FILE", env)
    captured = {}
    def fake_retry(text, token, person_id, image_urn=None, alt_text=None):
        captured.update(text=text, image_urn=image_urn)
        return {"status": "success", "post_id": "urn:li:share:1", "http_status": 201}
    monkeypatch.setattr(lp, "post_with_retry", fake_retry)
    def fail_upload(*a, **k):
        raise AssertionError("upload_image must not be called for text-only")
    monkeypatch.setattr(lp.linkedin_image, "upload_image", fail_upload)
    monkeypatch.setattr("sys.stdin", io.StringIO("just text"))
    with pytest.raises(SystemExit) as exc:
        lp.main([])
    assert exc.value.code == 0
    assert captured["text"] == "just text"
    assert captured["image_urn"] is None


def test_main_with_image_uploads_and_posts(monkeypatch, tmp_path):
    env = tmp_path / "linkedin-api.env"
    env.write_text("LINKEDIN_ACCESS_TOKEN=tok\nLINKEDIN_PERSON_ID=P1\n")
    monkeypatch.setattr(lp, "ENV_FILE", env)
    img = tmp_path / "pic.jpg"
    img.write_bytes(b"\xff\xd8\xff" + b"0" * 50)
    monkeypatch.setattr(lp.linkedin_image, "upload_image",
                        lambda path, person, tok, ver: "urn:li:image:C9")
    captured = {}
    def fake_retry(text, token, person_id, image_urn=None, alt_text=None):
        captured.update(image_urn=image_urn, alt_text=alt_text)
        return {"status": "success", "post_id": "urn:li:share:2", "http_status": 201}
    monkeypatch.setattr(lp, "post_with_retry", fake_retry)
    with pytest.raises(SystemExit) as exc:
        lp.main(["--image", str(img), "--alt-text", "my chart", "hello"])
    assert exc.value.code == 0
    assert captured["image_urn"] == "urn:li:image:C9"
    assert captured["alt_text"] == "my chart"


def test_main_bad_image_exits_before_network(monkeypatch, tmp_path):
    env = tmp_path / "linkedin-api.env"
    env.write_text("LINKEDIN_ACCESS_TOKEN=tok\nLINKEDIN_PERSON_ID=P1\n")
    monkeypatch.setattr(lp, "ENV_FILE", env)
    def fail_upload(*a, **k):
        raise AssertionError("must not upload an invalid image")
    monkeypatch.setattr(lp.linkedin_image, "upload_image", fail_upload)
    with pytest.raises(SystemExit) as exc:
        lp.main(["--image", str(tmp_path / "missing.jpg"), "hello"])
    assert exc.value.code == 1
```

Add `import pytest` at the top of this test file.

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/test_linkedin_post_main.py -v`
Expected: FAIL — `AttributeError: module 'linkedin_post' has no attribute 'parse_args'` (and no attribute `linkedin_image`).

- [ ] **Step 3: Add the import, arg parsing, and rewrite `main()`**

At the top of `scripts/linkedin_post.py`, add to the imports:
```python
import argparse
import linkedin_image
```

Add these functions above `main()`:
```python
def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Post text (and optionally one image) to LinkedIn."
    )
    parser.add_argument("text", nargs="*",
                        help="Post text (optional; falls back to stdin)")
    parser.add_argument("--image", default=None,
                        help="Path to a PNG/JPEG image to attach (< 5 MB)")
    parser.add_argument("--alt-text", dest="alt_text", default=None,
                        help="Alt text for the image (accessibility/SEO)")
    return parser.parse_args(argv)


def get_post_text(args):
    if args.text:
        return " ".join(args.text)
    return sys.stdin.read().strip()
```

Replace the entire `main()` function with:
```python
def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)

    if not ENV_FILE.exists():
        print(json.dumps({"status": "error", "detail": f"Env file not found: {ENV_FILE}"}))
        sys.exit(1)

    env = load_env(ENV_FILE)
    token = env.get("LINKEDIN_ACCESS_TOKEN", "")
    person_id = env.get("LINKEDIN_PERSON_ID", "")
    if not token or not person_id:
        print(json.dumps({"status": "error",
                          "detail": "LINKEDIN_ACCESS_TOKEN or LINKEDIN_PERSON_ID missing from env file"}))
        sys.exit(1)

    text = get_post_text(args)
    if not text:
        print(json.dumps({"status": "error", "detail": "No post text provided"}))
        sys.exit(1)

    image_urn = None
    alt_text = args.alt_text
    if args.image:
        try:
            validate_image(args.image)
        except (FileNotFoundError, ValueError) as e:
            print(json.dumps({"status": "error", "detail": str(e)}))
            sys.exit(1)
        try:
            image_urn = linkedin_image.upload_image(
                args.image, f"urn:li:person:{person_id}", token, LINKEDIN_VERSION
            )
        except linkedin_image.ImageUploadError as e:
            print(json.dumps({"status": "error", "detail": str(e)}))
            sys.exit(1)
        if not alt_text:
            alt_text = text.splitlines()[0][:300]
        print(json.dumps({"status": "info", "image_urn": image_urn,
                          "image_path": args.image}))

    result = post_with_retry(text, token, person_id, image_urn, alt_text)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["status"] == "success" else 1)
```

- [ ] **Step 4: Run the full test suite**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/ -v`
Expected: all tests pass (Task 2: 5, Task 3: 6, Task 4: 3, Task 5: 7, Task 6: 4, Task 7: 7 = 32 passed).

- [ ] **Step 5: Commit**

```bash
cd ~/.claude/skills/post-linkedin
git add scripts/linkedin_post.py scripts/tests/test_linkedin_post_main.py
git commit -m "feat: --image/--alt-text flags wired into main (text-only path preserved)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 8: Document the image workflow in `SKILL.md`

**Files:**
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: the CLI of `linkedin_image.py` (Task 4) and the `--image`/`--alt-text` flags of `linkedin_post.py` (Task 7).
- Produces: documentation only (no code).

- [ ] **Step 1: Add an "Image posts" section to `SKILL.md`**

Insert a new section after the existing "Step 6 — Publish" section. Use this exact content:
```markdown
## Step 7 — Image posts (optional)

The skill can attach a single image to a post. The image is generated for
**free** (no API key) from the post's own text, via Pollinations, and uploaded
through LinkedIn's modern Images API. The text-only flow is unchanged — these
steps only apply when an image is wanted.

### 7a. Derive the image prompt (Claude does this)
Read the approved post text and write a concise (1–3 sentence) visual prompt.
- Favor **abstract / conceptual / isometric / flat-illustration** styles.
- **Avoid** literal faces, hands, and embedded text — the free model renders
  these poorly. Surface the derived prompt to the user before generating.

### 7b. Generate and preview
Run the generator (separate, previewable step):
```
python3 scripts/linkedin_image.py --prompt "<derived prompt>" --out /tmp/li_image.jpg [--seed <int>]
```
- Output is **768×768 JPEG** (the free model caps resolution; size params are
  ignored). Use `--seed <int>` to reproduce a chosen image.
- On success it prints `{"status":"success","path":...}`; on failure
  `{"status":"error","detail":...}` and exits 1 — STOP and report the detail.
- **Show the image to the user and get approval** before publishing. Regenerate
  with a new seed or revised prompt if they want changes.

### 7c. Publish with the image
After approval, publish (post text via stdin, as usual):
```
python3 scripts/linkedin_post.py --image /tmp/li_image.jpg --alt-text "<alt text>" < /path/to/approved_post.txt
```
- If `--alt-text` is omitted, the first line of the post is used.
- A user-supplied image works the same way — just point `--image` at any
  existing PNG/JPEG (< 5 MB).
- Success prints a final JSON with `"status":"success"` and a `post_id`. On any
  non-201 / upload error it reports the exact `detail`/`http_status` and exits 1
  — do NOT claim the post was published.

### Known limitations
- **768×768** max (below LinkedIn's ideal ~1200²; fine for feed display).
- **No SLA** — Pollinations is a free community service; failures are surfaced.
- **Not private** — prompts/images may be publicly cached on Pollinations' feed;
  use generic conceptual prompts, never confidential content.
```

- [ ] **Step 2: Verify the doc reads correctly**

Run: `cd ~/.claude/skills/post-linkedin && grep -n "Step 7 — Image posts" SKILL.md`
Expected: one match (the new section header exists).

- [ ] **Step 3: Commit**

```bash
cd ~/.claude/skills/post-linkedin
git add SKILL.md
git commit -m "docs: document image-post workflow in SKILL.md

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 9: Manual end-to-end acceptance (network + visual)

**Files:** none (manual verification).

**Interfaces:**
- Consumes: everything above.
- Produces: a confirmed-working real post + a recorded result.

> This task cannot be unit-tested — it requires live LinkedIn credentials and a
> human (or vision-capable agent) to confirm the image renders. Do not mark the
> feature complete until every box here is checked. If any step fails, STOP and
> report the exact error per the fail-loud rule.

- [ ] **Step 1: Confirm the full unit suite is green**

Run: `cd ~/.claude/skills/post-linkedin && python3 -m pytest scripts/tests/ -q`
Expected: all 32 tests pass.

- [ ] **Step 2: Generate a real image**

Run:
```bash
cd ~/.claude/skills/post-linkedin
python3 scripts/linkedin_image.py --prompt "minimalist flat illustration of a network of glowing nodes, clean editorial style, blue gradient, no text" --out /tmp/li_e2e.jpg --seed 1
```
Expected: `{"status": "success", "path": "/tmp/li_e2e.jpg"}`. Open `/tmp/li_e2e.jpg` and confirm it's a real 768×768 image.

- [ ] **Step 3: Text-only regression (real post)**

Run:
```bash
cd ~/.claude/skills/post-linkedin
echo "Test post (text only) — please ignore." | python3 scripts/linkedin_post.py
```
Expected: JSON with `"status": "success"`, `"http_status": 201`, and a `post_id`. Confirm it appears on LinkedIn as a normal text post.

- [ ] **Step 4: Image post (real)**

Run:
```bash
cd ~/.claude/skills/post-linkedin
echo "Test post with image — please ignore." | python3 scripts/linkedin_post.py --image /tmp/li_e2e.jpg --alt-text "network of glowing nodes"
```
Expected: an `"status":"info"` line with the `image_urn`, then a final JSON with `"status":"success"`, `"http_status":201`, and a `post_id`.

- [ ] **Step 5: Visual confirmation on LinkedIn**

Open the post on LinkedIn. Confirm the **image actually renders** (not a blank media card). This is the real acceptance gate — a 201 alone is not sufficient.

- [ ] **Step 6: Failure-path spot check**

Run:
```bash
cd ~/.claude/skills/post-linkedin
echo "x" | python3 scripts/linkedin_post.py --image /tmp/does-not-exist.jpg
```
Expected: `{"status": "error", "detail": "Image not found: /tmp/does-not-exist.jpg"}` and exit code 1 — no network call, no fabricated success.

- [ ] **Step 7: Final commit (mark feature complete)**

```bash
cd ~/.claude/skills/post-linkedin
git add -A
git commit --allow-empty -m "test: verified image-post end-to-end on LinkedIn

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Notes for the implementer

- **Run order matters for imports:** `linkedin_post.py` does `import linkedin_image`, which resolves because the script's own directory is on `sys.path[0]` when run as `python3 scripts/linkedin_post.py`, and `conftest.py` adds `scripts/` to the path for tests. Don't move the modules out of `scripts/`.
- **Real API shapes are to-verify:** Task 3's `/rest/images` request/response field names are the documented modern flow but are only *proven* in Task 9. If LinkedIn returns a different structure, fix `initialize_upload` parsing and note it.
- **Don't widen scope:** single image only; no carousels/video; no upscaling; no Gemini. The `--image <path>` interface already accommodates a future paid generator without redesign.
