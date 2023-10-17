
# import du framework
from fastapi import FastAPI , HTTPException


#Import des routers
import routers.router_students
import routers.router_courses

# Documentation
from documentation.description import api_description
from documentation.tags import tags_metadata


#initialisation de l'API
app  = FastAPI(
    title = "Attendance Tracker",
    description=api_description,
    openapi_tags=tags_metadata # tagsmetadata definit au dessus
)



# Ajouter les routers dédiés
app.include_router(routers.router_students.router)
app.include_router(routers.router_courses.router)