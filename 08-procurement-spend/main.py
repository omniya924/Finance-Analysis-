"""Supplier concentration and procurement spend."""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
purchases = [
    (1, "Atlas Supplies", "IT", 6200, "2025-01-10"),
    (2, "Metro Office", "Facilities", 1800, "2025-01-18"),
    (3, "Atlas Supplies", "IT", 4700, "2025-02-03"),
    (4, "Green Logistics", "Transport", 3100, "2025-02-16"),
    (5, "Atlas Supplies", "IT", 2200, "2025-03-09"),
    (6, "Metro Office", "Facilities", 2500, "2025-03-12"),
]
with sqlite3.connect(ROOT / "procurement.db") as conn:
    conn.executescript((ROOT / "schema.sql").read_text())
    conn.execute("DELETE FROM purchases")
    conn.executemany("INSERT INTO purchases VALUES (?,?,?,?,?)", purchases)
    total = conn.execute("SELECT SUM(amount_gbp) FROM purchases").fetchone()[0]
    report = conn.execute("""
        SELECT supplier, COUNT(*), ROUND(SUM(amount_gbp),2)
        FROM purchases GROUP BY supplier ORDER BY SUM(amount_gbp) DESC
    """).fetchall()
print(f"Total spend: GBP {total:,.2f}")
print("Supplier | Orders | Spend GBP | Share %")
for supplier, count, spend in report:
    print(f"{supplier} | {count} | {spend:,.2f} | {spend / total * 100:.1f}")
print("Supplier share is a concentration indicator, not a supplier risk rating.")
