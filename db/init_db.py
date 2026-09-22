#!/usr/bin/env python3
"""SYNTHBUILDING schema. Source of truth: seed.json -> this DB -> site/.

Follows the workspace's standard DH-portal pattern (WitcherPortal,
ARTHURROBINPORTAL): SQLite is authoritative, generated HTML is never
hand-edited, every row carries provenance. Idempotent: safe to re-run.
"""
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "synthbuilding.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS projects (
    slug TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    path TEXT,
    live_url TEXT,
    status TEXT NOT NULL,               -- ACTIVE | STABLE | ARCHIVED | SCRATCH | STUB
    tech_stack TEXT,
    tags TEXT,                          -- comma-separated
    card_summary TEXT NOT NULL,         -- ~50 words
    page_summary TEXT NOT NULL,         -- ~500 words
    stuck_or_next TEXT,                 -- where it's blocked / what's next, or NULL
    theme TEXT,                         -- nsfripper | atalanta | bach | weird | other
    source_method TEXT NOT NULL DEFAULT 'LLM_ASSISTED',
    review_status TEXT NOT NULL DEFAULT 'DRAFT',
    confidence TEXT NOT NULL DEFAULT 'MEDIUM',
    verified_date TEXT
);

CREATE TABLE IF NOT EXISTS books (
    slug TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    path TEXT NOT NULL,
    card_summary TEXT NOT NULL,
    page_summary TEXT NOT NULL,
    relevance_to_synthbuilder TEXT,
    tags TEXT,
    source_method TEXT NOT NULL DEFAULT 'LLM_ASSISTED',
    review_status TEXT NOT NULL DEFAULT 'DRAFT',
    confidence TEXT NOT NULL DEFAULT 'MEDIUM'
);

CREATE TABLE IF NOT EXISTS site_meta (
    key TEXT PRIMARY KEY,
    value TEXT
);
"""


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()
    print(f"Schema ready at {DB_PATH}")


if __name__ == "__main__":
    main()
