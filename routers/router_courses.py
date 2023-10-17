from fastapi import APIRouter, Depends, HTTPException, status
from classes import  schemas_dto
from classes.schemas_dto import courses
from classes.schemas_dto import Course
from classes.schemas_dto  import Courses_POST_Body
from typing import List
import uuid



router = APIRouter(
    prefix='/courses',
    tags=['/Courses']
)



@router.get('/courses', response_model=List[Course])
async def get_student():
    return courses