from fastapi import APIRouter
import sqlite3

router = APIRouter()

DB_NAME = "infraguard.db"


@router.get("/roads")
def get_roads(page: int = 1, limit: int = 50):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    offset = (page - 1) * limit

    cursor.execute("""
        SELECT
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
        FROM roads
        LIMIT ? OFFSET ?
    """, (limit, offset))

    rows = cursor.fetchall()

    conn.close()

    data = []

    for row in rows:

        data.append({
            "segment_id": row[0],
            "pci": row[1],
            "road_type": row[2],
            "aadt": row[3],
            "asphalt_type": row[4],
            "last_maintenance": row[5],
            "average_rainfall": row[6],
            "rutting": row[7],
            "iri": row[8],
            "needs_maintenance": row[9]
        })

    return data


@router.get("/road/{segment_id}")
def get_single_road(segment_id: str):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM roads
    WHERE segment_id=?
    """, (segment_id,))

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return {"message": "Road Not Found"}

    return {
        "id": row[0],
        "segment_id": row[1],
        "pci": row[2],
        "road_type": row[3],
        "aadt": row[4],
        "asphalt_type": row[5],
        "last_maintenance": row[6],
        "average_rainfall": row[7],
        "rutting": row[8],
        "iri": row[9],
        "needs_maintenance": row[10]
    }


@router.get("/hospitals")
def get_hospitals(page: int = 1, limit: int = 20):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    offset = (page - 1) * limit

    cursor.execute("""
    SELECT *
    FROM hospitals
    LIMIT ? OFFSET ?
    """, (limit, offset))

    rows = cursor.fetchall()

    conn.close()

    hospitals = []

    for row in rows:

        hospitals.append({
            "id": row[0],
            "hospital_name": row[1],
            "city": row[2],
            "state": row[3],
            "district": row[4],
            "density": row[5],
            "latitude": row[6],
            "longitude": row[7],
            "rating": row[8],
            "reviews": row[9]
        })

    return hospitals


@router.get("/dashboard")
def dashboard():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM roads")
    total_roads = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM hospitals")
    total_hospitals = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM roads WHERE needs_maintenance=1")
    maintenance = cursor.fetchone()[0]

    conn.close()

    return {
        "total_roads": total_roads,
        "total_hospitals": total_hospitals,
        "roads_need_maintenance": maintenance,
        "traffic_delay_reduced": "18%",
        "emergency_response_improved": "11%",
        "fuel_saved": "1250 L/day",
        "co2_reduction": "3.2 Tons/month",
        "maintenance_savings": "₹12.4 Cr"
    }