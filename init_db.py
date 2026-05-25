# ─────────────────────────────────────────────
#  init_db.py — Quantum Debuggers
#  Run this once to set up the database.
#  Usage: python init_db.py
# ─────────────────────────────────────────────

from db_helpers import init_db

if __name__ == "__main__":
    print("Initialising PharmaCentral database...")
    init_db()
    print("Done! pharmacy.db is ready.")
    print("Default login — username: admin  |  password: admin123")
