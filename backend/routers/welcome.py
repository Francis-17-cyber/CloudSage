from fastapi import APIRouter

router = APIRouter(
    prefix="/welcome",
    tags=["Welcome"]
)

@router.get("/")
def welcome():
    return {
        "message": "Welcome to CloudSage API!",
        "available_endpoints": [
            "/",
            "/health",
            "/info",
            "/status",
            "/welcome"
        ]
    }