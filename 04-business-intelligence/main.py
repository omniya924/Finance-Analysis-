"""Sales and contribution-margin KPI reporting with SQLite."""
import sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parent
db=sqlite3.connect(ROOT/"sales.db")
db.executescript((ROOT/"schema.sql").read_text())
db.execute("DELETE FROM sales")
rows=[
 (1,"2025-01-04","North","Software",5,350,80),
 (2,"2025-01-07","South","Consulting",3,700,260),
 (3,"2025-02-12","North","Consulting",4,700,260),
 (4,"2025-02-20","West","Software",8,350,80),
 (5,"2025-03-03","South","Software",6,350,80),
 (6,"2025-03-21","West","Consulting",2,700,260),
]
db.executemany("INSERT INTO sales VALUES (?,?,?,?,?,?,?)",rows)
db.commit()
sql="""SELECT region,COUNT(*) orders,SUM(units) units,
 ROUND(SUM(units*unit_price),2) revenue,
 ROUND(SUM(units*(unit_price-unit_cost)),2) contribution,
 ROUND(100.0*SUM(units*(unit_price-unit_cost))/NULLIF(SUM(units*unit_price),0),1) contribution_margin_pct
 FROM sales GROUP BY region ORDER BY revenue DESC"""
print("Region | Orders | Units | Revenue | Contribution | Contribution margin %")
for row in db.execute(sql): print(*row,sep=" | ")
print("Note: contribution excludes fixed operating costs; it is not net profit.")
db.close()
