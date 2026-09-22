#!/usr/bin/env python3
"""seed.json -> synthbuilding.db. Idempotent (INSERT OR REPLACE)."""
from __future__ import annotations
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "db" / "synthbuilding.db"


def load(conn: sqlite3.Connection, path: Path, table: str, columns: list[str]) -> int:
    if not path.exists():
        print(f"  (skip, no file) {path.name}")
        return 0
    rows = json.loads(path.read_text(encoding="utf-8"))
    placeholders = ",".join("?" for _ in columns)
    col_list = ",".join(columns)
    n = 0
    for row in rows:
        values = []
        for c in columns:
            v = row.get(c)
            if isinstance(v, list):
                v = ",".join(v)
            values.append(v)
        conn.execute(
            f"INSERT OR REPLACE INTO {table} ({col_list}) VALUES ({placeholders})",
            values,
        )
        n += 1
    return n


def main() -> None:
    conn = sqlite3.connect(DB_PATH)

    project_cols = [
        "slug", "name", "path", "live_url", "status", "tech_stack", "tags",
        "card_summary", "page_summary", "stuck_or_next", "theme",
        "confidence",
    ]
    n = load(conn, ROOT / "db" / "seed_projects.json", "projects", project_cols)
    print(f"projects: {n} rows")

    book_cols = [
        "slug", "title", "author", "path", "card_summary", "page_summary",
        "relevance_to_synthbuilder", "tags",
    ]
    n = load(conn, ROOT / "db" / "seed_books.json", "books", book_cols)
    print(f"books: {n} rows")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
