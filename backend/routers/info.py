from fastapi import APIRouter

router = APIRouter(
    prefix="/info",
    tags=["Info"]
)

@router.get("/")
def api_info():
    return {
        "application": "CloudSage API",
        "version": "0.1.0",
        "status": "development"
    }