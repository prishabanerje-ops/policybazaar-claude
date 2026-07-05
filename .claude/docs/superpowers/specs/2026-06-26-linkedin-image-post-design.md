# LinkedIn Image Post — Design Spec

**Date:** 2026-06-26
**Status:** Approved for implementation planning
**Scope:** Extend the existing `post-linkedin` skill so it can publish image posts, with the image generated for free from the post's own text.

---

## 1. Goal

Today the `post-linkedin` skill publishes **text-only** posts via `scripts/linkedin_post.py`. This change adds the ability to attach a **single image** to a post, where the image is:

- **generated automatically** from a prompt derived from the post text (free, no API key), or
- **supplied as a file** the user already has (drop-in fallback).

The text-only path must remain unchanged.

---

## 2. Verified context (facts established during brainstorming)

These were confirmed by inspection/testing, not assumed:

1. **Existing script uses the modern LinkedIn API.** `scripts/linkedin_post.py` posts to `https://api.linkedin.com/rest/posts` with headers `LinkedIn-Version: 202506` and `X-Restli-Protocol-Version: 2.0.0`. It is **stdlib-only** (`urllib`, no `requests`). It authenticates from `~/.config/linkedin-api.env` and uses a **cached** `LINKEDIN_PERSON_ID` (no `/v2/me` call per run).
2. **Consequence:** the image-upload flow must use the **modern Images API** (`/rest/images`), not the legacy `/v2/assets?action=registerUpload` flow shown in the source PDF. Legacy `digitalmediaAsset` URNs are the wrong companion for `/rest/posts`.
3. **No Gemini/Google AI key is configured** anywhere (`~/.config`, shell env, `settings.json`), and the `google-genai` SDK is not installed. Gemini image generation via API is **paid-only**: the free tier returns `429 RESOURCE_EXHAUSTED` with `limit: 0` for every image model (`gemini-3.1-flash-image`, `gemini-2.5-flash-image`). The consumer "Gemini Pro" subscription cannot be driven programmatically. **Therefore the skill does not use Gemini.**
4. **Free image source verified working:** `https://image.pollinations.ai/prompt/<url-encoded-prompt>` returns a real JPEG with **no API key**, over a plain `urllib` GET. Verified output is professional-quality for LinkedIn when steered to abstract/illustrative/isometric styles.
5. **Pollinations resolution is capped at 768×768.** `width`/`height` query params are **ignored** by the free model — confirmed by requesting 1200² and 1024² and receiving 768² both times. `seed=<int>` is honored (reproducible output).

---

## 3. Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Packaging | **Extend** the `post-linkedin` skill (not a separate skill) | Credentials, `/rest/posts` logic, and the script already live here; a second skill reaching into this one's `scripts/` is fragile. |
| Image source | **Pollinations.ai** (free, keyless) | Verified working; no key, no billing; fits stdlib-`urllib` design. |
| Upload API | **Modern Images API** (`/rest/images?action=initializeUpload`) | Correct companion to the existing `/rest/posts` call. |
| Dependencies | **stdlib `urllib` only** | Matches existing script; zero install footprint; no `requests`/`google-genai`. |
| Orchestration | **Generation is a separate, previewable step** | The parent skill has a mandatory approval gate; the user must see the image before it publishes. The posting script takes a **file path**, not a prompt. |
| Generated-image cleanup | **Do not delete**; log the path | The script didn't create the source file philosophy + keeps artifacts for debugging. Files land in scratch/Downloads, not a temp dir that must be reaped. |

---

## 4. Architecture & components

All new/changed code is **stdlib `urllib`**, lives in `~/.claude/skills/post-linkedin/scripts/`, and requires **no API keys** for image generation.

### 4.1 `linkedin_image.py` (new module + thin CLI)

Two responsibilities, both importable and the first also runnable as a CLI:

**(a) Generation — `generate(prompt, out_path, seed=None) -> str`**
- URL-encodes `prompt`, GETs `https://image.pollinations.ai/prompt/<enc>?nologo=true[&seed=<seed>]`.
- Sends a `User-Agent` header (the bare default UA can be rejected).
- Validates: HTTP 200, `Content-Type` starts with `image/`, non-empty body. Anything else → raise `ImageGenError` with status + first bytes of body (Pollinations occasionally returns HTML/JSON errors).
- Writes bytes to `out_path`; returns `out_path`.
- CLI form: `python3 linkedin_image.py --prompt "<text>" --out <path> [--seed <int>]` → prints the saved path (or a JSON error and exit 1).

**(b) Upload — `upload_image(image_path, person_urn, token, version) -> str`**
- Step 1 — initialize: `POST https://api.linkedin.com/rest/images?action=initializeUpload`
  - Headers: `Authorization: Bearer <token>`, `Content-Type: application/json`, `LinkedIn-Version: <version>`, `X-Restli-Protocol-Version: 2.0.0`.
  - Body: `{"initializeUploadRequest": {"owner": "<person_urn>"}}`.
  - Parse `value.uploadUrl` and `value.image` (the `urn:li:image:…`).
- Step 2 — upload bytes: `PUT <uploadUrl>` with `Authorization: Bearer <token>` and the raw image bytes (`Content-Type: application/octet-stream`). Expect 200/201; otherwise raise with status + body.
- Returns the image URN.

> **Verification note:** exact field names/shapes for `/rest/images` must be confirmed against current LinkedIn docs during implementation and proven by a real test post. The shapes above are the documented modern flow but are treated as *to-verify*, not gospel.

### 4.2 `linkedin_post.py` (extended)

- Adopt `argparse` while **preserving the existing contract**:
  - Post text continues to come from **stdin** (the pattern the current `SKILL.md` already uses: `python3 linkedin_post.py < file`). Positional text (`python3 linkedin_post.py "text"`) remains supported for backward-compatibility.
  - New optional flags: `--image <path>`, `--alt-text <text>`.
- When `--image` is **absent** → behavior is byte-for-byte the current text-only flow (unchanged payload).
- When `--image` is **present**:
  1. Validate the file: exists, extension/content is PNG or JPEG, size < 5 MB. Fail before any network call otherwise.
  2. `urn = linkedin_image.upload_image(path, person_urn, token, version)`.
  3. Build the `/rest/posts` body as today **plus**:
     ```json
     "content": { "media": { "id": "<urn>", "altText": "<alt-text or derived>" } }
     ```
  4. If `--alt-text` is omitted, derive a short alt text from the post's first line / prompt (accessibility + SEO).
- The existing `LinkedIn-Version` / `X-Restli-Protocol-Version` headers and env-loading are reused as-is.

### 4.3 `SKILL.md` (updated)

Document the image workflow as an extension of the existing post flow, including the approval-gated preview step (Section 5) and the known limitations (Section 7).

---

## 5. End-to-end flow

```
1. Write / refine the LinkedIn post text  → user approves text (existing post-linkedin flow)
2. Claude derives a 1–3 sentence image prompt from the post
     - favor abstract / illustrative / isometric styles
     - avoid literal faces, hands, and embedded text (free-model weak spots)
     - surface the prompt to the user
3. Claude runs: linkedin_image.py --prompt "<derived>" --out <scratch>/li_image.jpg [--seed N]
     → Pollinations → 768×768 JPEG
4. Claude SHOWS the image to the user
     - user approves, OR asks to regenerate (new seed / revised prompt) — loop until happy
5. On approval: linkedin_post.py --image <scratch>/li_image.jpg --alt-text "<…>"  (post text via stdin)
     → /rest/images initializeUpload → PUT bytes → urn:li:image:…
     → /rest/posts with content.media = { id: urn, altText }
6. Report the post_id (urn:li:share:… / x-restli-id) as the verified confirmation.
```

Because step 5 takes a **file path**, a user-supplied image (e.g. one made in the Gemini Pro app) is a drop-in: skip steps 2–4 and point `--image` at it.

---

## 6. Error handling (fail-loud, per user's global rule)

- **Generation failure** (non-200, non-image content-type, empty body) → raise/report status + body snippet; do **not** proceed to post.
- **File validation failure** (missing / wrong format / ≥5 MB) → stop before any LinkedIn API call.
- **initializeUpload or PUT failure** → raise with HTTP status + response body; do not create the post.
- **Image-URN race** (post creation fails referencing the image) → retry-with-backoff: **3 attempts, ~2 s apart**, around the `/rest/posts` call only — **not** a blind `sleep()`, and **not** around the upload. If still failing, report and stop.
- **No fabricated success:** a post is only "published" when `/rest/posts` returns 201 with a post id. Anything else is reported as failure with the exact `http_status`/`detail`.
- The generated image file is **left in place** and its **path logged** on both success and failure.

---

## 7. Known limitations (documented in SKILL.md)

- **Resolution:** Pollinations free model caps at **768×768** (size params ignored). Acceptable for LinkedIn feed display; below the ideal ~1200². No upscaling in scope.
- **No SLA:** Pollinations is a free community service; it can rate-limit, change, or be unavailable. Failures are surfaced, not masked.
- **Privacy:** prompts and generated images **may be publicly cached** on Pollinations' feed. Use generic/conceptual prompts; do not encode confidential information in prompts. (Relevant for a corporate/professional account.)
- **Style reliability:** abstract / conceptual / isometric styles render cleanly; literal humans/hands and on-screen text are unreliable → the prompt-derivation step actively avoids them.
- **Output model not guaranteed:** the `model` param may be ignored; style can vary call-to-call. Use `seed` to reproduce a chosen image.

---

## 8. Prerequisites

- Existing LinkedIn credentials in `~/.config/linkedin-api.env` (`LINKEDIN_ACCESS_TOKEN`, `LINKEDIN_PERSON_ID`) — already present.
- The token's existing posting scope (e.g. `w_member_social`) is sufficient; image upload needs no extra scope. Re-verify only if a 403 appears.
- **No Gemini / Google AI key. No billing. No new pip packages.**

---

## 9. Testing / acceptance criteria

1. **Text-only regression:** a text-only post (no `--image`) still publishes exactly as before (201 + post id).
2. **Generation:** `linkedin_image.py` produces a valid JPEG from a prompt and fails loudly on a simulated bad response.
3. **File validation:** non-image, missing file, and >5 MB inputs are rejected before any API call.
4. **End-to-end image post:** one real post with a generated image returns 201 **and the image visually renders on LinkedIn** — confirmed by eye, not just the status code (LinkedIn can accept an asset and still show a blank card if fields are wrong).
5. **BYO image:** `--image <existing-file>` posts successfully.
6. **Failure reporting:** induced upload/post failures report the exact HTTP status + body and never claim success.

---

## 10. Out of scope (YAGNI)

- Multiple images / carousels (single image only).
- Video, documents, polls.
- Image upscaling / post-processing / resizing.
- Gemini/Imagen integration (revisit only if billing is enabled later; the `--image <path>` interface already accommodates any external generator without redesign).
- A separate `linkedin-image-post` skill.

---

## 11. Deviations from the source PDF

- **Modern `/rest/images`** Images API instead of the PDF's legacy `/v2/assets?action=registerUpload`.
- **Free keyless Pollinations** instead of Gemini/Imagen + `google-genai` (Gemini image API is paid-only; verified).
- **stdlib `urllib`** instead of the PDF's `requests` examples (matches the existing script).
- **768×768** practical resolution (documented), not the PDF's 1200² target.
- **Generation is a separate previewable step**; the posting script takes `--image <path>`, not `--image-prompt`, to honor the approval gate.
