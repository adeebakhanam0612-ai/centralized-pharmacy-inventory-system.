<div align="center">

<!-- BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0D7377&height=200&section=header&text=Centralized%20Pharmacy%20Inventory%20System&fontSize=28&fontColor=ffffff&fontAlignY=38&desc=Team%20Quantum%20Debuggers%20%7C%20Smart%20Healthcare%20Infrastructure&descAlignY=60&descSize=14" width="100%"/>

<!-- BADGES -->
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Analytics-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

<br/>

> **"Don't let medicines expire. Don't let shelves run empty. Don't let patients suffer."**
>
> A full-stack web application that centralizes pharmacy inventory across branches — with real-time alerts, analytics, and zero-configuration deployment.

<br/>

[🚀 Quick Start](#-installation-guide) · [📸 Screenshots](#-ui-gallery) · [🏗️ Architecture](#-system-architecture) · [🌍 SDG Impact](#-un-sdg-global-impact) · [👥 Team](#-team)

</div>

---

## 📋 Table of Contents

- [Product Overview](#-product-overview)
- [Key Features](#-key-features)
- [UN SDG Global Impact](#-un-sdg-global-impact)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Installation Guide](#-installation-guide)
- [Project Structure](#-project-structure)
- [UI Gallery](#-ui-gallery)
- [SDLC Journey](#-sdlc-journey)
- [Testing & Resilience](#-testing--resilience)
- [Team](#-team)

---

## 🏥 Product Overview

The **Centralized Pharmacy Inventory Management System (CPIMS)** is a web-based platform built to solve a critical real-world problem in healthcare: **medicine stockouts and undetected expiry** in pharmacies and hospital dispensaries.

Pharmacies managing dozens or hundreds of medicines across multiple branches often rely on paper registers or disconnected spreadsheets. This leads to:
- 💊 Medicines expiring on shelves without warning
- 📉 Critical drugs going out of stock unnoticed
- 📊 No visibility for procurement teams to plan restocking
- 🏥 Patients unable to access essential medications

CPIMS addresses all of this with a single, deployable web application that requires **no external database server**, runs on any OS, and provides real-time inventory intelligence to every stakeholder.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔐 **Secure Login** | Session-based authentication with flash messages and redirect protection |
| 📊 **Live Dashboard** | At-a-glance KPIs: total medicines, low stock count, expiry alerts, branch summary |
| 💊 **Inventory CRUD** | Add, edit, delete medicines with full 5-layer input validation |
| 🔍 **Real-Time Search** | Instant medicine search with filter chips (category, branch, status) |
| 🚨 **Smart Alerts** | Auto-flags low stock (< 10 units) and near-expiry (≤ 30 days) medicines |
| 📈 **Analytics** | Stock distribution charts, category breakdown, branch comparisons via Pandas |
| 🏢 **Branch Management** | View and manage inventory per branch; cross-branch sync simulation |
| 📥 **CSV Export** | One-click filtered data export to CSV |
| ⚙️ **Settings** | Configurable thresholds for low-stock and near-expiry detection |
| ⚡ **Flash Messages** | Real-time user feedback on every action (success / warning / error) |

---

## 🌍 UN SDG Global Impact

CPIMS directly advances **four United Nations Sustainable Development Goals**:

<div align="center">

| SDG | Goal | How CPIMS Contributes |
|:---:|---|---|
| **SDG 3** 🏥 | Good Health & Well-Being | Prevents medicine shortages that directly endanger patient health and continuity of care |
| **SDG 9** 🏗️ | Industry, Innovation & Infrastructure | Replaces manual pharmacy processes with modern, scalable digital infrastructure |
| **SDG 11** 🏙️ | Sustainable Cities & Communities | Strengthens urban healthcare systems through smart, data-driven inventory management |
| **SDG 12** ♻️ | Responsible Consumption & Production | Reduces medicine wastage from undetected expiry — estimated up to 40% reduction |

</div>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        CLIENT BROWSER                               │
│          HTML5 · CSS3 · JavaScript · Jinja2 Templates               │
└───────────────────────────┬─────────────────────────────────────────┘
                            │  HTTP Requests
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     FLASK APPLICATION LAYER                         │
│                                                                     │
│  ┌──────────┐  ┌───────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │  Auth    │  │ Inventory │  │  Alerts  │  │    Analytics     │  │
│  │  Routes  │  │  Routes   │  │  Routes  │  │     Routes       │  │
│  └──────────┘  └───────────┘  └──────────┘  └──────────────────┘  │
│                                                                     │
│  ┌──────────┐  ┌───────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │ Branches │  │  Orders   │  │   Sync   │  │    Settings      │  │
│  │  Routes  │  │  Routes   │  │  Routes  │  │     Routes       │  │
│  └──────────┘  └───────────┘  └──────────┘  └──────────────────┘  │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              VALIDATION & BUSINESS LOGIC LAYER              │   │
│  │  Layer 1: HTML5  →  Layer 2: JS  →  Layer 3: Flask Route   │   │
│  │  Layer 4: Business Logic  →  Layer 5: DB Constraints        │   │
│  └─────────────────────────────────────────────────────────────┘   │
└───────────────────────────┬─────────────────────────────────────────┘
                            │  SQL Queries (Parameterised)
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        DATA LAYER                                   │
│                                                                     │
│   ┌─────────────┐    ┌──────────────┐    ┌──────────────────────┐  │
│   │   SQLite    │    │    Pandas    │    │    CSV Export        │  │
│   │  Database   │    │  Analytics   │    │    Engine            │  │
│   │  (.db file) │    │  Engine      │    │                      │  │
│   └─────────────┘    └──────────────┘    └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### Database Schema

```
medicines
├── id              INTEGER PRIMARY KEY AUTOINCREMENT
├── name            TEXT NOT NULL
├── category        TEXT
├── quantity        INTEGER NOT NULL CHECK(quantity >= 0)
├── unit_price      REAL NOT NULL CHECK(unit_price > 0)
├── expiry_date     DATE NOT NULL
├── branch          TEXT NOT NULL
├── supplier        TEXT
├── reorder_level   INTEGER DEFAULT 10
└── last_updated    TIMESTAMP DEFAULT CURRENT_TIMESTAMP

users
├── id              INTEGER PRIMARY KEY AUTOINCREMENT
├── username        TEXT UNIQUE NOT NULL
├── password_hash   TEXT NOT NULL
└── role            TEXT DEFAULT 'staff'

settings
├── id              INTEGER PRIMARY KEY
├── low_stock_threshold    INTEGER DEFAULT 10
└── near_expiry_days       INTEGER DEFAULT 30
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | HTML5, CSS3, JavaScript | UI templates, interactivity, real-time search |
| **Backend** | Python 3.8+, Flask 2.x | Route handling, session management, business logic |
| **Database** | SQLite 3 | Zero-config persistent storage — single `.db` file |
| **Data Layer** | Pandas | Analytics aggregation, CSV export, data processing |
| **Templating** | Jinja2 | Server-side HTML rendering with template inheritance |
| **Version Control** | Git + GitHub | Collaboration, history, deployment |

---

## 🚀 Installation Guide

### Prerequisites

Make sure you have the following installed:

```bash
python --version    # Python 3.8 or higher required
pip --version       # pip package manager
git --version       # Git for cloning
```

### Step 1 — Clone the Repository

```bash
git clone https://github.com/adeebakhanam0612-ai/centralized-pharmacy-inventory-system.git
cd centralized-pharmacy-inventory-system
```

### Step 2 — Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt includes:**
```
flask
pandas
```

### Step 4 — Initialise the Database

```bash
python init_db.py
```

This creates `pharmacy.db` with all required tables and sample data.

### Step 5 — Run the Application

```bash
python app.py
```

### Step 6 — Open in Browser

```
http://127.0.0.1:5000
```

**Default login credentials:**
```
Username: admin
Password: admin123
```

> ⚠️ Change the default password after first login via the Settings page.

---

## 📁 Project Structure

```
centralized-pharmacy-inventory-system/
│
├── app.py                  # Main Flask application entry point
├── init_db.py              # Database initialisation script
├── config.py               # App configuration (thresholds, secret key)
├── db_helpers.py           # Centralised database connection helpers
├── requirements.txt        # Python dependencies
├── pharmacy.db             # SQLite database (auto-created on init)
│
├── templates/              # Jinja2 HTML templates
│   ├── base.html           # Base layout with sidebar navigation
│   ├── login.html          # Authentication page
│   ├── dashboard.html      # Main overview dashboard
│   ├── inventory.html      # Medicine inventory management
│   ├── alerts.html         # Low stock & expiry alerts
│   ├── analytics.html      # Charts and data analytics
│   ├── branches.html       # Branch management
│   ├── sync.html           # Cross-branch synchronisation
│   ├── orders.html         # Order management
│   └── settings.html       # System configuration
│
├── static/
│   ├── css/
│   │   └── style.css       # Global stylesheet
│   └── js/
│       └── main.js         # Search, filter, and UI interactions
│
└── docs/
    ├── architecture.png    # System architecture diagram
    └── screenshots/        # UI screenshots
```

---

## 📸 UI Gallery

> Screenshots of the live application:
> <img width="1911" height="1030" alt="image" src="https://github.com/user-attachments/assets/1bf0a2b6-dd2a-4b3c-9923-73ca185b1382" />
### 🏠 Dashboard
The main dashboard shows real-time KPIs — total medicines, low stock count, near-expiry alerts, and branch summaries at a glance.

<img width="1900" height="1021" alt="image" src="https://github.com/user-attachments/assets/aee4d2ef-1a9a-4e89-b592-4a4dfb9210cb" />
### 💊 Inventory Management
Full CRUD interface with real-time search, category filter chips, status badges (In Stock / Low Stock / Expired), and CSV export.

<img width="1896" height="1008" alt="image" src="https://github.com/user-attachments/assets/69d3c883-8456-4439-b432-9d794ad71506" />

### 🚨 Alerts Page
Automatically populated with medicines below the stock threshold or expiring within 30 days. Color-coded for urgency.

<img width="1912" height="1027" alt="image" src="https://github.com/user-attachments/assets/85d8582d-5b41-41d6-9521-ae8fee2a4387" />
### 📈 Analytics
Pandas-powered breakdowns: stock by category, branch comparisons, expiry timeline — helping procurement teams make data-driven decisions.

<img width="1895" height="1025" alt="image" src="https://github.com/user-attachments/assets/f3965bb6-7d45-4e42-8540-a488e28fc3d7" />

### ⚙️ Settings
Configurable low-stock threshold and near-expiry detection window — adjustable at runtime without code changes.

---

## 📅 SDLC Journey

| Week | Phase | Key Deliverables |
|:---:|---|---|
| **Week 1** | Planning + Requirements | Problem statement, stakeholder analysis, tech stack selection, GitHub setup |
| **Week 2** | Design + Implementation | System architecture diagram, ER diagram, UI mockups, base Flask app (10 pages) |
| **Week 3** | Testing + Error Handling | 35 manual test cases, 5-layer validation, edge case handling, error showcase |
| **Week 4** | Refactoring + Documentation | Codebase modularisation, SDLC report, production README, Expo preparation |

---

## 🧪 Testing & Resilience

CPIMS implements a **5-layer defence-in-depth validation strategy**:

```
User Input
    │
    ▼
[Layer 1] HTML5 Validation ──── required fields, type constraints, min/max
    │
    ▼
[Layer 2] JavaScript Checks ─── date logic, range validation, pre-submit
    │
    ▼
[Layer 3] Flask Route Handler ── request.form.get() with defaults, try/except
    │
    ▼
[Layer 4] Business Logic ─────── cross-field rules, duplicate detection
    │
    ▼
[Layer 5] SQLite Constraints ─── NOT NULL, CHECK, UNIQUE — final safety net
    │
    ▼
 Database Write ✅
```

**Test Coverage:** 35 manual test cases · 100% pass rate · 10 edge cases validated

---

## 👥 Team

<div align="center">

### 🔬 Quantum Debuggers

| Member | Role |
|---|---|
| **Adeeba Khanam** | Full-Stack Developer · Project Lead · Documentation |
| **Juvairiya Ifthekhar** | Frontend Developer · UI Design · Testing |
| **Syeda Sara Fathima** | Backend Developer · Database Design · Analytics |

</div>

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ by Team Quantum Debuggers**

*Centralized Pharmacy Inventory Management System — Week 4 · 2026*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0D7377&height=100&section=footer" width="100%"/>

</div>
