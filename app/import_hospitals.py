import sqlite3
import pandas as pd
from pathlib import Path
import os

# Connect Database
conn = sqlite3.connect("infraguard.db")
cursor = conn.cursor()

# Dataset Path
BASE_DIR = Path(__file__).resolve().parents[2]
csv_file = BASE_DIR / "dataset" / "Hospitals.csv"

print("Looking for:", csv_file)
print("Exists:", os.path.exists(csv_file))

if not os.path.exists(csv_file):
    raise FileNotFoundError(csv_file)

# Read CSV
df = pd.read_csv(csv_file)

print("CSV Loaded Successfully!")
print(df.columns.tolist())

# Delete old table
cursor.execute("DROP TABLE IF EXISTS hospitals")

# Create table
cursor.execute("""
CREATE TABLE hospitals(
    id INTEGER PRIMARY KEY,
    hospital_name TEXT,
    city TEXT,
    state TEXT,
    district TEXT,
    density REAL,
    latitude REAL,
    longitude REAL,
    rating REAL,
    reviews INTEGER
)
""")

# Insert data
count = 0

for _, row in df.iterrows():

    cursor.execute("""
    INSERT INTO hospitals VALUES(?,?,?,?,?,?,?,?,?,?)
    """,(
    None,                     # Auto-increment ID
    row["id"],                # Hospital name ("Hospital #0")
    row["City"],
    row["State"],
    row["District"],
    float(row["Density"]),
    float(row["Latitude"]),
    float(row["Longitude"]),
    float(row["Rating"]),
    int(row["Number of Reviews"])
))

    count += 1

conn.commit()
conn.close()

print(f"Imported {count} Hospitals Successfully!")