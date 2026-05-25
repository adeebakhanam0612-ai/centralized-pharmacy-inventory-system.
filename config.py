# ─────────────────────────────────────────────
#  config.py — Quantum Debuggers
#  Central configuration for PharmaCentral
# ─────────────────────────────────────────────

import os

class Config:
    # Flask secret key for session management
    SECRET_KEY = os.environ.get("SECRET_KEY", "quantumdebuggers2026")

    # SQLite database file path
    DATABASE = os.environ.get("DATABASE", "pharmacy.db")

    # Default low-stock threshold (units)
    LOW_STOCK_THRESHOLD = 20

    # Default near-expiry warning window (days)
    NEAR_EXPIRY_DAYS = 30

    # Debug mode — set False in production
    DEBUG = True
