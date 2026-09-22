# DEPLOY_STATE.md — SYNTHBUILDING

**Status: LIVE and confirmed working, deployed 2026-09-22.**

- **URL:** https://t3dy.github.io/SYNTHBUILDING/ — loaded directly and
  verified: dark console theme renders, card grid and theme-filter nav work,
  a project subpage (`project/nsfripper.html`) loads correctly over the real
  Pages subpath with full text and the stuck/next box intact, confirming the
  relative-link routing survived the subpath deploy as predicted below.
- **Repo:** `github.com/t3dy/SYNTHBUILDING` — `main` branch holds the full
  source (docs, `db/`, `scripts/`, `research/`); `gh-pages` branch holds only
  the built `site/` output (split via `git subtree split --prefix=site`,
  not hand-maintained — regenerate it the same way after any rebuild).
- **Host:** GitHub Pages, source = `gh-pages` branch, path `/`. Confirmed via
  `gh api repos/t3dy/SYNTHBUILDING/pages` → `"status":"built"`.
- Deployed with Ted's explicit go-ahead (2026-09-22 message: "deploy and make
  sure we have detailed documentation...").

## What's live

- 15 verified project entries across 5 themes (NES/NSFRIPPER, Atalanta,
  Bach, Weird/experimental, Other), each with a full page.
- 35 music-technology library books, each with a full page.
- A comprehensive `README.md` on the repo's main branch documenting every
  project family, linked from GitHub's own repo view.

## How to redeploy after an edit

```bash
# from C:\Dev\SYNTHBUILDER, after editing a seed JSON or build_site.py:
python scripts/seed_from_json.py
python scripts/build_site.py
git add -A && git commit -m "..."
git push origin main
git branch -D gh-pages            # drop the old split
git subtree split --prefix=site -b gh-pages
git push origin gh-pages --force
```

Then reload the live URL and click through at least one project page and the
library section before calling the update done — a green push is not a
working site.

## The base-path gotcha (confirmed handled)

GitHub Pages serves from a repo subpath. `build_site.py` emits only relative
links (`project/<slug>.html`, `../style.css`) with no root-absolute paths —
verified in the templates, and confirmed working on the live URL itself
(not just inferred from the source).

## Known gaps, honestly stated

- Mobile/narrow-viewport layout not explicitly tested.
- `REAPERBEYONDNES` and `nes-music-lab` still have no git history — unrelated
  to this deploy, tracked separately in `MUSICHACKING.md`.
