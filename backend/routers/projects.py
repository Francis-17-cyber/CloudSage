from fastapi import APIRouter
from schemas.project import Project
from services.project_service import (
    get_all_projects,
    create_project as create_project_service
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.get("/")
def get_projects():
    return get_all_projects()

@router.post("/")
def create_project(project: Project):
    return create_project_service(project)