from fastapi import APIRouter
from datetime import datetime

router = APIRouter(
    prefix="/status",
    tags=["Status"]
)

@router.get("/")
def api_status():
    return {
        "api": "CloudSage",
        "status": "online",
        "timestamp": datetime.utcnow().isoformat()
    }