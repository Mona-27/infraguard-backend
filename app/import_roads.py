import sqlite3
import pandas as pd
from pathlib import Path
import os

# -----------------------------
# Connect Database
# -----------------------------
conn = sqlite3.connect("infraguard.db")
cursor = conn.cursor()

# -----------------------------
# Drop old table
# -----------------------------
cursor.execute("DROP TABLE IF EXISTS roads")

# -----------------------------
# Create new table
# -----------------------------
cursor.execute("""
CREATE TABLE roads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    segment_id TEXT,
    pci REAL,
    road_type TEXT,
    aadt INTEGER,
    asphalt_type TEXT,
    last_maintenance INTEGER,
    average_rainfall REAL,
    rutting REAL,
    iri REAL,
    needs_maintenance INTEGER
)
""")

# -----------------------------
# Locate CSV
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
csv_file = BASE_DIR / "dataset" / "ESC 12 Pavement Dataset.csv"

print("Looking for:", csv_file)

if not os.path.exists(csv_file):
    raise FileNotFoundError(csv_file)

df = pd.read_csv(csv_file)

print("CSV Loaded Successfully!")
print(df.columns.tolist())

# -----------------------------
# Insert Data
# -----------------------------
for _, row in df.iterrows():

    cursor.execute("""
    INSERT INTO roads(
        segment_id,
        pci,
        road_type,
        aadt,
        asphalt_type,
        last_maintenance,
        average_rainfall,
        rutting,
        iri,
        needs_maintenance
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        str(row["Segment ID"]),
        float(row["PCI"]),
        str(row["Road Type"]),
        int(row["AADT"]),
        str(row["Asphalt Type"]),
        int(row["Last Maintenance"]),
        float(row["Average Rainfall"]),
        float(row["Rutting"]),
        float(row["IRI"]),
        int(row["Needs Maintenance"])
    ))

conn.commit()

print(f"Imported {len(df)} Roads Successfully!")

conn.close()