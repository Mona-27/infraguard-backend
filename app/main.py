from ml_model import router as ml_router
from decision_engine import router as decision_router
from emergency import router as emergency_router
from fastapi import FastAPI
from routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="InfraGuard AI Backend",
    version="1.0"

)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(ml_router)
app.include_router(decision_router)
app.include_router(emergency_router)

@app.get("/")
def home():
    return {
        "message": "InfraGuard AI Backend Running"
    }