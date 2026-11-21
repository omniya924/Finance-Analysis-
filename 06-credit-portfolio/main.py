"""Credit portfolio exposure and delinquency analysis."""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
with sqlite3.connect(ROOT / "credit.db") as conn:
    conn.executescript((ROOT / "schema.sql").read_text())
    conn.execute("DELETE FROM loans")
    loans = [
        (101, "SME", 80000, .095, 36, 0),
        (102, "Consumer", 12000, .135, 24, 35),
        (103, "SME", 125000, .085, 48, 65),
        (104, "Mortgage", 210000, .052, 240, 0),
        (105, "Consumer", 6500, .155, 18, 95),
        (106, "Mortgage", 180000, .057, 180, 12),
    ]
    conn.executemany("INSERT INTO loans VALUES (?,?,?,?,?,?)", loans)
    report = conn.execute("""
        SELECT segment, COUNT(*), ROUND(SUM(principal),2),
          ROUND(SUM(CASE WHEN days_past_due >= 30 THEN principal ELSE 0 END),2),
          ROUND(100.0 * SUM(CASE WHEN days_past_due >= 30 THEN principal ELSE 0 END)
                / NULLIF(SUM(principal),0),2)
        FROM loans GROUP BY segment ORDER BY segment
    """).fetchall()
print("Segment | Loans | Exposure GBP | 30+ DPD exposure GBP | 30+ DPD share %")
for record in report:
    print(" | ".join(map(str, record)))
print("Synthetic outstanding principal; delinquency is not a default probability.")
