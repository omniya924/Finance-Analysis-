"""Monthly acquisition cohort retention using SQL and Python."""
import sqlite3
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
orders = [
    (1,"C1","2025-01",100),(2,"C2","2025-01",60),
    (3,"C1","2025-02",85),(4,"C3","2025-02",120),
    (5,"C2","2025-03",75),(6,"C3","2025-03",95),
    (7,"C4","2025-03",55),(8,"C1","2025-03",90),
    (9,"C4","2025-04",65),(10,"C3","2025-04",100),
]
with sqlite3.connect(ROOT / "retention.db") as conn:
    conn.executescript((ROOT / "schema.sql").read_text())
    conn.execute("DELETE FROM orders")
    conn.executemany("INSERT INTO orders VALUES (?,?,?,?)", orders)
    records = conn.execute("SELECT customer_id,order_month FROM orders ORDER BY order_month").fetchall()
first_month = {}
activity = defaultdict(set)
for customer, month in records:
    first_month.setdefault(customer, month)
    activity[first_month[customer]].add((customer, month))
cohorts = defaultdict(set)
for customer, month in first_month.items():
    cohorts[month].add(customer)
print("Cohort | Active month | Active customers | Cohort size | Retention %")
for cohort, members in sorted(cohorts.items()):
    for month in sorted({m for _, m in activity[cohort]}):
        active = len({c for c, m in activity[cohort] if m == month})
        print(f"{cohort} | {month} | {active} | {len(members)} | {100 * active / len(members):.1f}")
print("Only months with observed activity are printed; missing months are not zero-filled.")
