from fastapi import FastAPI
from routers.health import router as health_router
from routers.info import router as info_router
from routers.status import router as status_router
from routers.welcome import router as welcome_router
from config import APP_NAME, APP_VERSION
from routers.projects import router as projects_router

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.include_router(health_router)
app.include_router(info_router)
app.include_router(status_router)
app.include_router(welcome_router)
app.include_router(projects_router)

@app.get("/")
def root():
    return {
        "status": "CloudSage Backend Running",
        "version": APP_VERSION
    }