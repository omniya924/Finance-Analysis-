"""Simple payment anomalies using customer-relative transaction size."""
import sqlite3
from pathlib import Path
from collections import defaultdict
from statistics import median

ROOT = Path(__file__).resolve().parent
payments = [
    (1, "A10", 45, "GB", "2025-05-01 09:00"),
    (2, "A10", 55, "GB", "2025-05-02 10:00"),
    (3, "A10", 49, "GB", "2025-05-03 11:00"),
    (4, "A10", 950, "GB", "2025-05-04 12:00"),
    (5, "B20", 430, "GB", "2025-05-01 09:00"),
    (6, "B20", 470, "GB", "2025-05-02 10:00"),
    (7, "B20", 440, "GB", "2025-05-03 11:00"),
    (8, "B20", 5200, "DE", "2025-05-04 12:00"),
]
with sqlite3.connect(ROOT / "payments.db") as conn:
    conn.executescript((ROOT / "schema.sql").read_text())
    conn.execute("DELETE FROM payments")
    conn.executemany("INSERT INTO payments VALUES (?,?,?,?,?)", payments)
    records = conn.execute("SELECT * FROM payments ORDER BY account_id,payment_time").fetchall()

history = defaultdict(list)
print("Payment | Account | Amount GBP | Prior median GBP | Flag")
for pid, account, amount, country, timestamp in records:
    baseline = median(history[account]) if history[account] else None
    flag = baseline is not None and len(history[account]) >= 3 and amount > 5 * baseline
    print(f"{pid} | {account} | {amount:.2f} | {baseline if baseline is not None else 'N/A'} | {flag}")
    history[account].append(amount)
print("Flags identify unusual size only, not fraud.")
