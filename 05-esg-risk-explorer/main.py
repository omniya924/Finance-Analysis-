"""Synthetic ESG indicator screening, not ESG ratings or predictions."""
import sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parent
db=sqlite3.connect(ROOT/"esg.db")
db.executescript((ROOT/"schema.sql").read_text())
db.execute("DELETE FROM esg_metrics")
records=[
 ("Northwind Energy","Energy",120,12,60),
 ("Bluewater Energy","Energy",185,18,45),
 ("Cedar Technology","Technology",18,9,75),
 ("Harbor Technology","Technology",27,14,55),
]
db.executemany("INSERT INTO esg_metrics VALUES (?,?,?,?,?)",records)
db.commit()
print("Company | Industry | Emissions intensity | Employee turnover % | Independent board %")
for row in db.execute("SELECT * FROM esg_metrics ORDER BY industry,company"): print(*row,sep=" | ")
print("\nWithin-industry comparison (lower emissions intensity in these synthetic examples):")
for row in db.execute("""SELECT a.industry,a.company,a.emissions_intensity
 FROM esg_metrics a WHERE a.emissions_intensity=(SELECT MIN(b.emissions_intensity) FROM esg_metrics b WHERE b.industry=a.industry) ORDER BY a.industry"""):
    print(*row,sep=" | ")
print("Indicators are fictional; no ESG rating, prediction, or investment recommendation is implied.")
db.close()
