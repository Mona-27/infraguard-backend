import sqlite3

# Connect to road.db (creates it if it doesn't exist)
conn = sqlite3.connect("road.db")
cursor = conn.cursor()

# ==========================
# Roads Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    road_name TEXT NOT NULL,
    location TEXT,
    latitude REAL,
    longitude REAL,
    road_condition TEXT
)
""")

# ==========================
# Prediction Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Prediction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    road_id INTEGER,
    damage_type TEXT,
    severity TEXT,
    confidence REAL,
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (road_id) REFERENCES Roads(id)
)
""")

# ==========================
# Budget Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Budget (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    road_id INTEGER,
    estimated_cost REAL,
    repair_priority TEXT,
    budget_status TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (road_id) REFERENCES Roads(id)
)
""")

# ==========================
# Reports Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    road_id INTEGER,
    report_title TEXT,
    report_description TEXT,
    report_status TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (road_id) REFERENCES Roads(id)
)
""")

# ==========================
# Potholes Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Potholes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    road_id INTEGER,
    latitude REAL,
    longitude REAL,
    severity TEXT,
    image_path TEXT,
    detected_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (road_id) REFERENCES Roads(id)
)
""")

# ==========================
# Detections Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Detections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pothole_id INTEGER,
    model_name TEXT,
    damage_type TEXT,
    confidence REAL,
    detection_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pothole_id) REFERENCES Potholes(id)
)
""")

conn.commit()
conn.close()

print("road.db created successfully with all 6 tables!")