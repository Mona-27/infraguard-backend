import sqlite3

conn = sqlite3.connect("infraguard.db")
cursor = conn.cursor()

# Roads Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS roads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    segment_id TEXT,
    pci REAL,
    road_type TEXT,
    aadt INTEGER,
    asphalt_type TEXT,
    last_maintenance INTEGER,
    average_roughness REAL,
    rutting REAL,
    iri REAL,
    needs_maintenance INTEGER
)
""")

# Hospitals Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS hospitals (
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

# Predictions Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    road_id INTEGER,
    risk_score REAL,
    risk_level TEXT
)
""")

# Budget Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS budget (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_budget REAL,
    allocated_budget REAL,
    remaining_budget REAL
)
""")

# Reports Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    report_name TEXT,
    generated_on TEXT
)
""")

# Emergency Routes Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS emergency_routes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hospital_name TEXT,
    incident_latitude REAL,
    incident_longitude REAL,
    recommended_route TEXT,
    estimated_time INTEGER,
    time_saved INTEGER
)
""")

conn.commit()
conn.close()

print("All tables created successfully!")