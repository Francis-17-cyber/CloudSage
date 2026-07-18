from database.projects_db import projects


def get_all_projects():
    return projects


def create_project(project):
    projects.append(
        {
            "id": len(projects) + 1,
            "name": project.name,
            "status": project.status
        }
    )

    return {
        "message": "Project created successfully!",
        "project": project
    }