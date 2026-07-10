from fastapi import APIRouter

router = APIRouter()

@router.get("/decision")

def decision():

    return {
        "priority_road": "SEG-1025",
        "reason": "High traffic + Poor PCI + Heavy Rainfall",
        "estimated_budget": "₹18,50,000",
        "expected_life_extension": "5 Years",
        "traffic_improvement": "18%"
    }