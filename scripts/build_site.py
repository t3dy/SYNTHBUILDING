#!/usr/bin/env python3
"""synthbuilding.db -> site/ (static HTML). Never hand-edit site/ output."""
from __future__ import annotations
import html
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "db" / "synthbuilding.db"
SITE = ROOT / "site"

THEME_LABELS = {
    "nsfripper": "NES / NSFRIPPER family",
    "atalanta": "Atalanta Fugiens x NES",
    "bach": "Chipped On Bach",
    "weird": "Weird / experimental",
    "other": "Other tools",
}

STATUS_COLOR = {
    "ACTIVE": "#5ec26a",
    "STABLE": "#5ec2b8",
    "ARCHIVED": "#8a8a8a",
    "SCRATCH": "#c2a15e",
    "STUB": "#c25e5e",
}

CSS = """
:root {
  --bg: #10120f;
  --panel: #181b16;
  --ink: #d8dccb;
  --dim: #8b9080;
  --accent: #e8c15a;
  --accent2: #6fd68f;
  --rule: #2c3025;
  --mono: 'Cascadia Code', 'Consolas', 'SFMono-Regular', Menlo, monospace;
}
* { box-sizing: border-box; }
body {
  background: var(--bg); color: var(--ink);
  font-family: Georgia, 'Iowan Old Style', serif;
  margin: 0; padding: 0 16px 64px;
  line-height: 1.55;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
header.site {
  max-width: 900px; margin: 0 auto; padding: 40px 0 16px;
  border-bottom: 1px solid var(--rule);
}
header.site h1 {
  font-family: var(--mono); letter-spacing: 0.03em;
  font-size: 1.9rem; margin: 0 0 6px; color: var(--accent);
}
header.site p.tagline { color: var(--dim); margin: 0 0 14px; font-family: var(--mono); font-size: 0.92rem; }
nav.themes { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
nav.themes a {
  font-family: var(--mono); font-size: 0.8rem; color: var(--dim);
  border: 1px solid var(--rule); padding: 4px 10px; border-radius: 3px;
}
nav.themes a:hover, nav.themes a.active { color: var(--accent); border-color: var(--accent); text-decoration: none; }
main { max-width: 900px; margin: 0 auto; padding-top: 24px; }
h2.section { font-family: var(--mono); color: var(--accent2); font-size: 1rem;
  text-transform: uppercase; letter-spacing: 0.08em; margin: 36px 0 14px;
  border-bottom: 1px solid var(--rule); padding-bottom: 6px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 14px; }
.card {
  background: var(--panel); border: 1px solid var(--rule); border-radius: 4px;
  padding: 14px 16px; display: flex; flex-direction: column; gap: 6px;
}
.card h3 { margin: 0; font-size: 1.02rem; }
.card .meta { font-family: var(--mono); font-size: 0.72rem; color: var(--dim); display: flex; gap: 8px; flex-wrap: wrap; }
.badge { font-family: var(--mono); font-size: 0.68rem; padding: 1px 6px; border-radius: 2px; border: 1px solid currentColor; }
.card p.card-summary { color: var(--ink); font-size: 0.92rem; margin: 4px 0 2px; }
.card .live { font-family: var(--mono); font-size: 0.75rem; }
.page-header { margin-bottom: 8px; }
.page-header h1 { margin: 0 0 4px; font-size: 1.7rem; }
.page-meta { font-family: var(--mono); font-size: 0.78rem; color: var(--dim); margin-bottom: 18px; }
.page-body p { margin: 0 0 14px; }
.stuck-box {
  margin-top: 22px; padding: 14px 16px; background: #1c1408; border: 1px solid #4a3418;
  border-radius: 4px; font-size: 0.92rem;
}
.stuck-box strong { color: var(--accent); font-family: var(--mono); font-size: 0.8rem; text-transform: uppercase; }
.back { display: inline-block; margin-bottom: 18px; font-family: var(--mono); font-size: 0.85rem; }
footer.site { max-width: 900px; margin: 48px auto 0; padding-top: 16px; border-top: 1px solid var(--rule);
  color: var(--dim); font-family: var(--mono); font-size: 0.75rem; }
"""


def e(s):
    return html.escape(s or "")


def card_html(p: sqlite3.Row) -> str:
    color = STATUS_COLOR.get(p["status"], "#888")
    live = f'<div class="live">&#9654; <a href="{e(p["live_url"])}" target="_blank" rel="noopener">live site</a></div>' if p["live_url"] else ""
    path = f'<span>{e(p["path"])}</span>' if p["path"] else "<span>(deployed only, no local path)</span>"
    return f"""<div class="card">
  <h3><a href="project/{e(p['slug'])}.html">{e(p['name'])}</a></h3>
  <div class="meta">
    <span class="badge" style="color:{color}">{e(p['status'])}</span>
    {path}
  </div>
  <p class="card-summary">{e(p['card_summary'])}</p>
  {live}
</div>"""


def book_card_html(b: sqlite3.Row) -> str:
    author = f" &mdash; {e(b['author'])}" if b["author"] else ""
    return f"""<div class="card">
  <h3><a href="library/{e(b['slug'])}.html">{e(b['title'])}</a></h3>
  <div class="meta"><span>{author.lstrip(' &mdash;')}</span></div>
  <p class="card-summary">{e(b['card_summary'])}</p>
</div>"""


def page_shell(title: str, body: str, depth: int = 0) -> str:
    prefix = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} — SYNTHBUILDING</title>
<link rel="stylesheet" href="{prefix}style.css">
</head><body>
{body}
</body></html>"""


def project_page(p: sqlite3.Row) -> str:
    color = STATUS_COLOR.get(p["status"], "#888")
    paras = "".join(f"<p>{e(para)}</p>" for para in (p["page_summary"] or "").split("\n\n"))
    live = f'<p><a href="{e(p["live_url"])}" target="_blank" rel="noopener">&#9654; live site</a></p>' if p["live_url"] else ""
    path = f"<code>{e(p['path'])}</code>" if p["path"] else "deployed only, no local path"
    stuck = f'<div class="stuck-box"><strong>Stuck / next</strong><br>{e(p["stuck_or_next"])}</div>' if p["stuck_or_next"] else ""
    body = f"""<a class="back" href="../index.html">&larr; all projects</a>
<div class="page-header">
  <h1>{e(p['name'])}</h1>
  <div class="page-meta">
    <span class="badge" style="color:{color}">{e(p['status'])}</span>
    &nbsp;{path}&nbsp;&middot;&nbsp;{e(p['tech_stack'])}
  </div>
  {live}
</div>
<div class="page-body">{paras}</div>
{stuck}"""
    return page_shell(p["name"], body, depth=1)


def book_page(b: sqlite3.Row) -> str:
    paras = "".join(f"<p>{e(para)}</p>" for para in (b["page_summary"] or "").split("\n\n"))
    rel = f'<div class="stuck-box"><strong>Relevance to SYNTHBUILDER</strong><br>{e(b["relevance_to_synthbuilder"])}</div>' if b["relevance_to_synthbuilder"] else ""
    body = f"""<a class="back" href="../index.html">&larr; all projects</a>
<div class="page-header">
  <h1>{e(b['title'])}</h1>
  <div class="page-meta">{e(b['author'] or '')} &middot; <code>{e(b['path'])}</code></div>
</div>
<div class="page-body">{paras}</div>
{rel}"""
    return page_shell(b["title"], body, depth=1)


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    (SITE / "project").mkdir(parents=True, exist_ok=True)
    (SITE / "library").mkdir(parents=True, exist_ok=True)
    (SITE / "style.css").write_text(CSS, encoding="utf-8")

    projects = conn.execute("SELECT * FROM projects ORDER BY theme, name").fetchall()
    books = conn.execute("SELECT * FROM books ORDER BY title").fetchall()

    for p in projects:
        (SITE / "project" / f"{p['slug']}.html").write_text(project_page(p), encoding="utf-8")
    for b in books:
        (SITE / "library" / f"{b['slug']}.html").write_text(book_page(b), encoding="utf-8")

    by_theme: dict[str, list] = {}
    for p in projects:
        by_theme.setdefault(p["theme"] or "other", []).append(p)

    sections = []
    for theme_key, label in THEME_LABELS.items():
        rows = by_theme.get(theme_key, [])
        if not rows:
            continue
        cards = "\n".join(card_html(r) for r in rows)
        sections.append(f'<h2 class="section" id="{theme_key}">{e(label)}</h2><div class="grid">{cards}</div>')

    lib_section = ""
    if books:
        lib_cards = "\n".join(book_card_html(b) for b in books)
        lib_section = f'<h2 class="section" id="library">Music book library</h2><div class="grid">{lib_cards}</div>'
    else:
        lib_section = '<h2 class="section" id="library">Music book library</h2><p style="color:var(--dim)">Catalog pending.</p>'

    nav = " ".join(f'<a href="#{k}">{e(v)}</a>' for k, v in THEME_LABELS.items() if by_theme.get(k)) + ' <a href="#library">Library</a>'

    index_body = f"""<header class="site">
  <h1>SYNTHBUILDING</h1>
  <p class="tagline">Ted Hand's music-hacking &amp; music-composition projects — synths, NES chiptune extraction, Atalanta Fugiens fugues, Bach mashups, and everything in between.</p>
  <nav class="themes">{nav}</nav>
</header>
<main>
{''.join(sections)}
{lib_section}
</main>
<footer class="site">Generated from <code>db/synthbuilding.db</code>. Source: <a href="https://github.com/t3dy/SYNTHBUILDING">github.com/t3dy/SYNTHBUILDING</a>.</footer>"""

    (SITE / "index.html").write_text(page_shell("SYNTHBUILDING", index_body, depth=0), encoding="utf-8")
    conn.close()
    print(f"Built {len(projects)} project pages, {len(books)} book pages -> {SITE}")


if __name__ == "__main__":
    main()
