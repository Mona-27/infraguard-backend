from fastapi import APIRouter
import sqlite3
from geopy.distance import geodesic
from pathlib import Path

router = APIRouter()

# Always use the database inside backend/app
BASE_DIR = Path(__file__).resolve().parent
DB_NAME = BASE_DIR / "infraguard.db"


@router.get("/emergency-route")
def emergency_route(latitude: float, longitude: float):

    conn = sqlite3.connect(str(DB_NAME))
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            hospital_name,
            city,
            latitude,
            longitude,
            rating
        FROM hospitals
    """)

    hospitals = cursor.fetchall()

    conn.close()

    if len(hospitals) == 0:
        return {
            "status": "No hospitals found in database"
        }

    nearest = None
    shortest_distance = float("inf")

    for hospital in hospitals:

        try:
            hospital_location = (
                float(hospital[2]),
                float(hospital[3])
            )

            distance = geodesic(
                (latitude, longitude),
                hospital_location
            ).km

            if distance < shortest_distance:
                shortest_distance = distance
                nearest = hospital

        except:
            continue

    if nearest is None:
        return {
            "status": "No valid hospital coordinates found"
        }

    estimated_time = round((shortest_distance / 40) * 60)

    return {
        "status": "Emergency Corridor Activated",
        "nearest_hospital": nearest[0],
        "city": nearest[1],
        "distance_km": round(shortest_distance, 2),
        "estimated_time_minutes": estimated_time,
        "rating": nearest[4]
    }