
from fastapi import APIRouter, Depends, HTTPException, status
from classes import  schemas_dto
from classes.schemas_dto import students
from classes.schemas_dto import Student
from classes.schemas_dto  import StudentNoID
from typing import List
import uuid



router = APIRouter(
    prefix='/students',
    tags=['Students']
)


# Verbs + Endpoints
@router.get('/students', response_model=List[Student])
async def get_student():
    return students


# 1. Exercice (10min) Create new Student: POST
# response_model permet de définir de type de réponse (ici nous retournons le student avec sont id)
# status_code est définit sur 201-Created car c'est un POST
@router.post('/students', response_model=Student, status_code=201)
async def create_student(givenName:str):
    # génération de l'identifiant unique
    generatedId=uuid.uuid4()
    # création de l'object/dict Student 
    newStudent= Student(id=str(generatedId), name=givenName)
    # Ajout du nouveau Student dans la List/Array
    students.append(newStudent)
    # Réponse définit par le Student avec son ID
    return newStudent


# 2. Exercice (10min) Student GET by ID
# response_model est un Student car nous souhaitons trouvé l'étudiant correspodant à l'ID
@router.get('/students/{student_id}', response_model=Student)
async def get_student_by_ID(student_id:str): # student_id correspond au URI parameter du path: '/students/{student_id}'
    #On parcours chaque étudiant de la liste
    for student in students:
        # Si l'ID correspond, on retourne l'étudiant trouvé
        if student.id == student_id:
            return student
        # pas de "else" car si on ne l'a pas trouvé, on continue avec le prochain student
    # Si on arrive ici, c'est que la boucle sur la liste "students" n'a rien trouvé
    # On lève donc un HTTP Exception
    raise HTTPException(status_code= 404, detail="Student not found")

# 3. Exercice (10min) PATCH Student (name)
@router.patch('/students/{student_id}', status_code=204)
async def modify_student_name(student_id:str, modifiedStudent: StudentNoID):
    for student in students:
        if student.id == student_id:
            student.name=modifiedStudent.name
            return
    raise HTTPException(status_code= 404, detail="Student not found")

# 4. Exercice (10min) DELETE Student
@router.delete('/students/{student_id}', status_code=204)
async def delete_student(student_id:str):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return
    raise HTTPException(status_code= 404, detail="Student not found")


# Reste à faire 
# - Sortir mon student's router dans un dossier "routers"
# - Rédiger une documentation et l'ajouter à mon app FastAPI()
# - Sortir mes pydantic models dans un dossier classes
# - Ajouter les tags 