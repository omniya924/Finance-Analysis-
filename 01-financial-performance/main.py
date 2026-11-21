"""Financial ratio analysis on synthetic company financials."""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
db = sqlite3.connect(ROOT / "financials.db")
db.executescript((ROOT / "schema.sql").read_text())
db.execute("DELETE FROM financials")
rows = [
 ("Alpha Manufacturing",2024,1250000,820000,145000,410000,230000,1750000,720000),
 ("Beta Services",2024,980000,540000,120000,330000,180000,1100000,480000),
 ("Gamma Retail",2024,1650000,1320000,42000,240000,310000,1350000,1020000),
 ("Alpha Manufacturing",2025,1430000,900000,190000,480000,245000,1920000,750000),
 ("Beta Services",2025,1120000,620000,155000,390000,200000,1260000,505000),
 ("Gamma Retail",2025,1720000,1390000,37000,250000,335000,1410000,1090000),
]
db.executemany("INSERT INTO financials VALUES (?,?,?,?,?,?,?,?,?)",rows)
db.commit()
query = """SELECT company,year,ROUND(100.0*(revenue-cogs)/NULLIF(revenue,0),1) gross_margin_pct,
 ROUND(100.0*net_income/NULLIF(revenue,0),1) net_margin_pct,
 ROUND(current_assets/NULLIF(current_liabilities,0),2) current_ratio,
 ROUND(total_liabilities/NULLIF(total_assets,0),2) debt_to_assets
 FROM financials ORDER BY year,company"""
print("Company | Year | Gross margin % | Net margin % | Current ratio | Debt/assets")
for row in db.execute(query): print(*row,sep=" | ")
db.close()
