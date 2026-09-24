# WEBSITEFIXER

An on-demand Claude Code subagent (`website-fixer`, defined in
`.claude/agents/website-fixer.md`) that finds broken or unfinished websites
among SYNTHBUILDER's music projects, diagnoses why they're broken, fixes them,
and prepares them for deployment to **each project's own GitHub Pages site**
(workspace hosting policy — see root `C:\Dev\CLAUDE.md`). It does not deploy
without asking first; publishing is a confirm-with-Ted action per workspace
convention.

## Scope (as of 2026-09-22)

Everything catalogued in `../ATALANTA.md` and `../MUSICHACKING.md` under the
SYNTHBUILDER umbrella — currently:

| Project | State | What's wrong |
|---|---|---|
| `C:\Dev\FUGUEJUKEBOX-website` | Broken, deployed to Vercel, dead | Filesystem-relative audio path breaks under real HTTP; wrong host for a static site |
| `C:\Dev\FugueJukebox-repo` | Broken, git-tracked | MP3s excluded from the push entirely — a working deploy would have nothing to play |
| `C:\Dev\FUGUEJUKEBOX` | Music complete, no site | Canonical source: 500 MP3s + 500 WAVs, ~1.8GB across two duplicate folders (`emblems/`, `music/`) |
| `C:\Dev\EMBLEMSIN3D` | Live, working | Not broken — `https://t3dy.github.io/emblems-in-3d/`. Standalone `jukebox.html`/`fugue.html`/`grandtour.html` are local-only by design (absolute-path asset deps), never ported to Pages |
| `EMBLEMSIN3D\ANTIGRAVFUGIENS` | Experimental, undeployed | Not linked from any site nav; worth surfacing, not fixing |
| `C:\Dev\ANTIGRAVEMBLEMSIN3D` | Abandoned fork | Vite rebuild, no git history, not a music project in its own right |

Full diagnosis for all of the above is already written up in
`C:\Dev\SYNTHBUILDER\ATALANTA.md` — the agent should read that file first
rather than re-discover the same bugs.

## Running it

Invoke via the Agent tool with `subagent_type: website-fixer`, or ask Claude
Code in this workspace to "run the website-fixer agent on FUGUEJUKEBOX" (etc).
Point it at one project per run — the agent asks before touching git remotes
or pushing, so a single run is: diagnose -> fix locally -> show you what
would be deployed -> wait for a go-ahead.

## Updating scope later

When a new SYNTHBUILDER-family project needs reviving, add a row to the table
above (or point the agent at `MUSICHACKING.md` for the full project catalog)
rather than widening it to scan all of `C:\Dev` — this tool is deliberately
scoped to the music/website cluster, not a general-purpose site fixer.
