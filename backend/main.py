from fastapi import FastAPI
from routers.health import router as health_router
from routers.info import router as info_router
from routers.status import router as status_router

app = FastAPI(
    title="CloudSage API",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(info_router)
app.include_router(status_router)

@app.get("/")
def root():
    return {
        "status": "CloudSage Backend Running",
        "version": "0.1.0"
    }