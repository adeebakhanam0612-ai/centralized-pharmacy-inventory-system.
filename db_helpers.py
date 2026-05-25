# ─────────────────────────────────────────────
#  db_helpers.py — Quantum Debuggers
#  Centralised database connection helpers
# ─────────────────────────────────────────────

import sqlite3
from config import Config


def get_db():
    """Open and return a SQLite database connection. Returns None on failure."""
    try:
        conn = sqlite3.connect(Config.DATABASE)
        conn.row_factory = sqlite3.Row  # Optional: enables column-name access
        return conn
    except sqlite3.Error:
        return None


def close_db(conn):
    """Safely close a database connection."""
    if conn:
        try:
            conn.close()
        except sqlite3.Error:
            pass


def init_db():
    """
    Initialise the database — create tables and seed default users.
    Called once at app startup via app.py.
    """
    conn = sqlite3.connect(Config.DATABASE)
    c = conn.cursor()

    # Medicines table
    c.execute("""
        CREATE TABLE IF NOT EXISTS medicines (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT    NOT NULL,
            category TEXT    NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity >= 0),
            expiry   TEXT    NOT NULL,
            branch   TEXT    NOT NULL
        )
    """)

    # Users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT    NOT NULL UNIQUE,
            password TEXT    NOT NULL,
            role     TEXT    NOT NULL
        )
    """)

    # Seed default users (ignore if already exist)
    default_users = [
        ("admin",  "admin123",    "Admin"),
        ("adeeba", "quantum2026", "Manager"),
    ]
    for username, password, role in default_users:
        try:
            c.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (username, password, role)
            )
        except sqlite3.IntegrityError:
            pass  # User already exists — skip silently

    conn.commit()
    conn.close()
