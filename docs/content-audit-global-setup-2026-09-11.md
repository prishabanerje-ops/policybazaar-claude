# content-audit skill — global setup

## Current state (verified 2026-09-11)

The skill lives at:

```
.claude/skills/content/content-audit/
  SKILL.md          (28KB, name: content-audit)
  assets/
    policybazaar-urls.txt
  references/
    ai-detection-parameters.md
    eeat-framework.md
    fact-check-parameters.md
    geo-parameters.md
    policybazaar-context.md
    schema-expectations-health.md
    schema-expectations-travel.md
    seo-parameters.md
    ymyl-helpful-content.md
```

It is a **sub-skill of the `content` hub**, checked into this project's git repo (`policybazaar Claude`).

## It is already global — via the existing compatibility symlink

Per `CLAUDE.local.md`, this machine has compatibility symlinks in `~/.claude/skills/` left over from the July 2026 laptop migration:

```
~/.claude/skills/content -> "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/content"
```

`~/.claude/skills/` is scanned by Claude Code regardless of which project directory a session is opened in. Because `content-audit` sits inside that symlinked `content/` folder, it is discovered as its own top-level skill (confirmed: it shows up in this session's skill list as `content-audit`, separately from the `content` hub, with the exact frontmatter description from its `SKILL.md`).

**Practical effect:** `/content audit` and `/content-audit` already work from *any* project directory on this machine, not just this one. You don't need to do anything further for that part.

## What "global" does NOT change

1. **It stays tied to this project folder.** The symlink is a pointer, not a copy. If `"/Users/aakashsrivastava/Documents/PolicyBazaar Claude"` is ever renamed, moved, or deleted, the symlink breaks and the skill disappears everywhere. Any edit you make to the skill here is instantly live everywhere else too (same file, no sync step) — that's the trade-off of a symlink vs. a standalone copy.
2. **Its scope is hardcoded, not just habitual.** The `SKILL.md` frontmatter explicitly restricts it: *"Scoped to Policybazaar UAE (policybazaar.ae) HEALTH and TRAVEL insurance content only... Other verticals (motor/life/home) and Paisabazaar UAE are out of scope."* Running it against unrelated content (a different company's blog, a different vertical) won't error — it just isn't built to score that content correctly, since `references/policybazaar-context.md`, `schema-expectations-health.md`, `schema-expectations-travel.md`, etc. all assume this vertical.

## If you want full independence instead

Only needed if you want the skill to survive this project folder being deleted/renamed, or want to hand a portable copy to someone without git access to this repo. Two options:

- **Standalone copy**: copy the whole `content-audit/` directory (SKILL.md + assets/ + references/) to `~/.claude/skills/content-audit/` as real files, not a symlink. Downside: it stops tracking edits made in this repo — you'd have to manually re-copy after changes.
- **Own symlink entry** (`~/.claude/skills/content-audit -> .../content/content-audit`): purely cosmetic — it's already discoverable through the `content` hub symlink, so this wouldn't add new reach, just a shorter path.

Neither was done here since you didn't ask for decoupling — say the word if you want one of these set up.
