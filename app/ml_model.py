from fastapi import APIRouter
import random

router = APIRouter()

@router.post("/predict")
def predict():

    risk_score = random.randint(50, 100)

    if risk_score >= 80:
        priority = "High"
        recommendation = "Immediate repair within 7 days"

    elif risk_score >= 60:
        priority = "Medium"
        recommendation = "Schedule repair within 30 days"

    else:
        priority = "Low"
        recommendation = "Monitor road condition"

    return {
        "risk_score": risk_score,
        "priority": priority,
        "maintenance_required": risk_score >= 60,
        "recommendation": recommendation
    }