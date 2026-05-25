// ─────────────────────────────────────────────
//  main.js — Quantum Debuggers
//  PharmaCentral Frontend Logic
// ─────────────────────────────────────────────

// ── Real-Time Search ──────────────────────────
function initSearch(inputId, tableBodyId) {
    const input = document.getElementById(inputId);
    if (!input) return;

    input.addEventListener("input", function () {
        const query = this.value.toLowerCase().trim();
        const rows = document.querySelectorAll(`#${tableBodyId} tr`);
        let visibleCount = 0;

        rows.forEach(row => {
            const text = row.innerText.toLowerCase();
            const show = text.includes(query);
            row.style.display = show ? "" : "none";
            if (show) visibleCount++;
        });

        // Show "no results" if nothing matches
        const noResult = document.getElementById("no-results");
        if (noResult) {
            noResult.style.display = visibleCount === 0 ? "block" : "none";
        }
    });
}

// ── Filter Chips ──────────────────────────────
function initFilterChips() {
    const chips = document.querySelectorAll(".chip[data-filter]");
    if (!chips.length) return;

    chips.forEach(chip => {
        chip.addEventListener("click", function () {
            // Toggle active state
            chips.forEach(c => c.classList.remove("active"));
            this.classList.add("active");

            const filter = this.dataset.filter;
            const rows = document.querySelectorAll("#medicine-table-body tr");

            rows.forEach(row => {
                if (filter === "all") {
                    row.style.display = "";
                } else {
                    const category = row.dataset.category || "";
                    const status   = row.dataset.status   || "";
                    const branch   = row.dataset.branch   || "";
                    const match = category === filter || status === filter || branch === filter;
                    row.style.display = match ? "" : "none";
                }
            });
        });
    });
}

// ── Form Validation ───────────────────────────
function validateAddForm() {
    const name     = document.getElementById("med-name");
    const quantity = document.getElementById("med-quantity");
    const expiry   = document.getElementById("med-expiry");

    if (!name || !quantity || !expiry) return true; // fields not present

    let valid = true;
    const today = new Date(); today.setHours(0,0,0,0);

    // Name check
    if (!name.value.trim() || name.value.trim().length < 3) {
        showFieldError(name, "Medicine name must be at least 3 characters.");
        valid = false;
    } else clearFieldError(name);

    // Quantity check
    const qty = parseInt(quantity.value);
    if (isNaN(qty) || qty < 0) {
        showFieldError(quantity, "Quantity must be 0 or more.");
        valid = false;
    } else clearFieldError(quantity);

    // Expiry check
    if (expiry.value) {
        const expDate = new Date(expiry.value);
        if (expDate < today) {
            showFieldError(expiry, "Expiry date must be today or in the future.");
            valid = false;
        } else clearFieldError(expiry);
    } else {
        showFieldError(expiry, "Expiry date is required.");
        valid = false;
    }

    return valid;
}

function showFieldError(field, message) {
    field.style.borderColor = "#e74c3c";
    let err = field.parentElement.querySelector(".field-error");
    if (!err) {
        err = document.createElement("span");
        err.className = "field-error";
        err.style.cssText = "color:#e74c3c;font-size:0.78rem;margin-top:3px;display:block;";
        field.parentElement.appendChild(err);
    }
    err.textContent = message;
}

function clearFieldError(field) {
    field.style.borderColor = "";
    const err = field.parentElement.querySelector(".field-error");
    if (err) err.remove();
}

// ── Auto-dismiss Flash Messages ───────────────
function initFlashMessages() {
    const flashes = document.querySelectorAll(".flash");
    flashes.forEach(flash => {
        setTimeout(() => {
            flash.style.transition = "opacity 0.5s";
            flash.style.opacity = "0";
            setTimeout(() => flash.remove(), 500);
        }, 4000);
    });
}

// ── Confirm Delete ────────────────────────────
function confirmDelete(medicineName) {
    return confirm(`Remove "${medicineName}" from inventory?\nThis action cannot be undone.`);
}

// ── Set Expiry Min Date (today) ───────────────
function initExpiryField() {
    const expiry = document.getElementById("med-expiry");
    if (expiry) {
        const today = new Date().toISOString().split("T")[0];
        expiry.setAttribute("min", today);
    }
}

// ── Initialise Everything on DOM Ready ────────
document.addEventListener("DOMContentLoaded", function () {
    initSearch("search-input", "medicine-table-body");
    initFilterChips();
    initFlashMessages();
    initExpiryField();
});
