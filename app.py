from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "quantumdebuggers2026"
DB = "pharmacy.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, category TEXT NOT NULL,
        quantity INTEGER NOT NULL, expiry TEXT NOT NULL, branch TEXT NOT NULL)""")
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE, password TEXT NOT NULL, role TEXT NOT NULL)""")
    try:
        c.execute("INSERT INTO users (username,password,role) VALUES (?,?,?)",("admin","admin123","Admin"))
        c.execute("INSERT INTO users (username,password,role) VALUES (?,?,?)",("adeeba","quantum2026","Manager"))
    except: pass
    conn.commit(); conn.close()

def get_db():
    try: return sqlite3.connect(DB)
    except: return None

def get_medicines():
    conn = get_db()
    if not conn: return []
    c = conn.cursor()
    c.execute("SELECT * FROM medicines ORDER BY id DESC")
    rows = c.fetchall(); conn.close()
    today = datetime.today(); warn = today + timedelta(days=30)
    result = []
    for r in rows:
        try: exp = datetime.strptime(r[4],"%Y-%m-%d"); expiring = today <= exp <= warn
        except: expiring = False
        result.append(r + (expiring,))
    return result

def validate_medicine(name, category, quantity, expiry, branch):
    errors = []
    if not name or name.strip() == "": errors.append("Medicine name cannot be empty.")
    if not expiry or expiry.strip() == "": errors.append("Expiry date cannot be empty.")
    try:
        qty = int(quantity)
        if qty < 0: errors.append("Quantity cannot be negative.")
        if qty > 100000: errors.append("Quantity too large.")
    except: errors.append("Quantity must be a valid number.")
    if name and len(name.strip()) < 3: errors.append("Medicine name too short (min 3 chars).")
    if expiry:
        try:
            if datetime.strptime(expiry,"%Y-%m-%d") < datetime.today(): errors.append("Expiry date cannot be in the past.")
        except: errors.append("Invalid expiry date format.")
    return errors

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session: return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

@app.route("/", methods=["GET","POST"])
@app.route("/login", methods=["GET","POST"])
def login():
    if "user" in session: return redirect(url_for("dashboard"))
    if request.method == "POST":
        username = request.form.get("username","").strip()
        password = request.form.get("password","").strip()
        if not username or not password:
            flash("Please enter both username and password.", "error")
            return render_template("login.html")
        conn = get_db()
        if conn:
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = c.fetchone(); conn.close()
            if user:
                session["user"] = user[1]; session["role"] = user[3]
                flash(f"Welcome back, {user[1]}!", "success")
                return redirect(url_for("dashboard"))
        flash("Invalid username or password.", "error")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear(); flash("You have been logged out.", "success")
    return redirect(url_for("login"))

@app.route("/dashboard")
@login_required
def dashboard():
    medicines = get_medicines()
    low_stock = sum(1 for m in medicines if m[3] < 20)
    expiring_soon = sum(1 for m in medicines if m[6])
    return render_template("dashboard.html", medicines=medicines, low_stock=low_stock, expiring_soon=expiring_soon, active="dashboard")

@app.route("/inventory")
@login_required
def inventory():
    medicines = get_medicines()
    low_stock = sum(1 for m in medicines if m[3] < 20)
    expiring_soon = sum(1 for m in medicines if m[6])
    return render_template("inventory.html", medicines=medicines, low_stock=low_stock, expiring_soon=expiring_soon, active="inventory")

@app.route("/add", methods=["POST"])
@login_required
def add():
    name = request.form.get("name","").strip()
    category = request.form.get("category","").strip()
    quantity = request.form.get("quantity","").strip()
    expiry = request.form.get("expiry","").strip()
    branch = request.form.get("branch","").strip()
    errors = validate_medicine(name, category, quantity, expiry, branch)
    if errors:
        for e in errors: flash(e, "error")
        return redirect(url_for("inventory"))
    try:
        conn = get_db(); c = conn.cursor()
        c.execute("INSERT INTO medicines (name,category,quantity,expiry,branch) VALUES (?,?,?,?,?)",
                  (name, category, int(quantity), expiry, branch))
        conn.commit(); conn.close()
        flash(f"'{name}' added to inventory!", "success")
    except Exception as e: flash(f"Error: {str(e)}", "error")
    return redirect(url_for("inventory"))

@app.route("/delete/<int:id>")
@login_required
def delete(id):
    try:
        conn = get_db(); c = conn.cursor()
        c.execute("SELECT name FROM medicines WHERE id=?", (id,))
        med = c.fetchone()
        if not med: flash("Medicine not found.", "error")
        else:
            c.execute("DELETE FROM medicines WHERE id=?", (id,))
            conn.commit(); flash(f"'{med[0]}' removed from inventory.", "success")
        conn.close()
    except Exception as e: flash(f"Error: {str(e)}", "error")
    return redirect(url_for("inventory"))

@app.route("/alerts")
@login_required
def alerts():
    medicines = get_medicines()
    low_stock = sum(1 for m in medicines if m[3] < 20)
    expiring_soon = sum(1 for m in medicines if m[6])
    low_meds = [m for m in medicines if m[3] < 20]
    exp_meds = [m for m in medicines if m[6]]
    return render_template("alerts.html", medicines=medicines, low_stock=low_stock,
        expiring_soon=expiring_soon, low_meds=low_meds, exp_meds=exp_meds, active="alerts")

@app.route("/analytics")
@login_required
def analytics():
    medicines = get_medicines()
    low_stock = sum(1 for m in medicines if m[3] < 20)
    expiring_soon = sum(1 for m in medicines if m[6])
    categories = {}
    for m in medicines: categories[m[2]] = categories.get(m[2], 0) + 1
    branches = {}
    for m in medicines: branches[m[5]] = branches.get(m[5], 0) + 1
    total_qty = sum(m[3] for m in medicines)
    return render_template("analytics.html", medicines=medicines, low_stock=low_stock,
        expiring_soon=expiring_soon, categories=categories, branches=branches,
        total_qty=total_qty, active="analytics")

@app.route("/branches")
@login_required
def branches():
    medicines = get_medicines()
    low_stock = sum(1 for m in medicines if m[3] < 20)
    expiring_soon = sum(1 for m in medicines if m[6])
    branch_data = {}
    for m in medicines:
        b = m[5]
        if b not in branch_data: branch_data[b] = {"count":0,"low":0,"expiring":0}
        branch_data[b]["count"] += 1
        if m[3] < 20: branch_data[b]["low"] += 1
        if m[6]: branch_data[b]["expiring"] += 1
    return render_template("branches.html", medicines=medicines, low_stock=low_stock,
        expiring_soon=expiring_soon, branch_data=branch_data, active="branches")

@app.route("/settings")
@login_required
def settings():
    medicines = get_medicines()
    low_stock = sum(1 for m in medicines if m[3] < 20)
    expiring_soon = sum(1 for m in medicines if m[6])
    return render_template("settings.html", medicines=medicines, low_stock=low_stock,
        expiring_soon=expiring_soon, active="settings")


@app.route("/export")
@login_required
def export():
    import csv, io
    from flask import Response
    medicines = get_medicines()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID","Medicine Name","Category","Quantity","Expiry Date","Branch","Status"])
    for med in medicines:
        if med[6]: status = "Expiring Soon"
        elif med[3] < 20: status = "Low Stock"
        elif med[3] < 50: status = "Moderate"
        else: status = "In Stock"
        writer.writerow([med[0], med[1], med[2], med[3], med[4], med[5], status])
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=pharmacy_inventory.csv"}
    )


@app.route("/sync")
@login_required
def sync():
    medicines    = get_medicines()
    low_stock    = sum(1 for m in medicines if m[3] < 20)
    expiring_soon= sum(1 for m in medicines if m[6])
    branch_data  = {}
    for m in medicines:
        b = m[5]
        if b not in branch_data: branch_data[b] = {"count":0,"low":0,"expiring":0}
        branch_data[b]["count"] += 1
        if m[3] < 20: branch_data[b]["low"] += 1
        if m[6]:      branch_data[b]["expiring"] += 1
    return render_template("sync.html", medicines=medicines, low_stock=low_stock,
        expiring_soon=expiring_soon, branch_data=branch_data, active="sync")

@app.route("/orders")
@login_required
def orders():
    medicines    = get_medicines()
    low_stock    = sum(1 for m in medicines if m[3] < 20)
    expiring_soon= sum(1 for m in medicines if m[6])
    return render_template("orders.html", medicines=medicines, low_stock=low_stock,
        expiring_soon=expiring_soon, active="orders")

@app.route("/save_settings", methods=["POST"])
@login_required
def save_settings():
    low_threshold  = request.form.get("low_threshold", "20")
    expiry_days    = request.form.get("expiry_days", "30")
    try:
        session["low_threshold"]  = int(low_threshold)
        session["expiry_days"]    = int(expiry_days)
        flash(f"Settings saved! Low stock threshold: {low_threshold} units, Expiry warning: {expiry_days} days.", "success")
    except:
        flash("Invalid values. Please enter valid numbers.", "error")
    return redirect(url_for("settings"))

if __name__ == "__main__":
    init_db()
    print("PharmaCentral running at http://127.0.0.1:5000")
    app.run(debug=True)