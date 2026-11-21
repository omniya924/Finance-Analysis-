"""Foreign-currency exposure translated into GBP."""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
positions = [
    (1,"Sales","EUR",150000),(2,"Sales","USD",80000),
    (3,"Purchasing","EUR",-70000),(4,"Purchasing","USD",-115000),
    (5,"Treasury","JPY",9000000),(6,"Treasury","GBP",25000),
]
rates = [("EUR",.86),("USD",.78),("JPY",.0052),("GBP",1.0)]
with sqlite3.connect(ROOT / "fx.db") as conn:
    conn.executescript((ROOT / "schema.sql").read_text())
    conn.execute("DELETE FROM positions")
    conn.execute("DELETE FROM fx_rates")
    conn.executemany("INSERT INTO positions VALUES (?,?,?,?)",positions)
    conn.executemany("INSERT INTO fx_rates VALUES (?,?)",rates)
    report = conn.execute("""
        SELECT p.currency,ROUND(SUM(p.amount_local),2),
               ROUND(SUM(p.amount_local*r.gbp_per_unit),2)
        FROM positions p JOIN fx_rates r ON p.currency=r.currency
        GROUP BY p.currency ORDER BY p.currency
    """).fetchall()
print("Currency | Net local exposure | Net exposure GBP")
for record in report:
    print(" | ".join(map(str,record)))
print("Positive values represent net assets/receivables; negative values represent net liabilities/payables.")
print("Rates are fictional and fixed, not current market rates.")
