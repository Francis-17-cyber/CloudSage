from fastapi import APIRouter
from config import APP_NAME, APP_VERSION, APP_STATUS

router = APIRouter(
    prefix="/info",
    tags=["Info"]
)

@router.get("/")
def api_info():
    return {
        "application": APP_NAME,
        "version": APP_VERSION,
        "status": APP_STATUS
    }