# Import du framework
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uuid

# Initialisation de l'API
app = FastAPI(
    title="Attendance Tracker"
)

# Model Pydantic = Datatype
class Student(BaseModel):
    id: str
    name: str

students = [
    Student(id="1", name="Adama"),
    Student(id="2", name="Adrien"),
    Student(id="3", name="Akbar")
]

# Verbs + Endpoints
@app.get('/students', response_model=List[Student])
async def get_student():
    return students

# 1. Exercice (10min) Create new Student: POST
# response_model permet de définir de type de réponse (ici nous retournons le student avec sont id)
# status_code est définit sur 201-Created car c'est un POST
@app.post('/students', response_model=Student, status_code=201)
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

# 3. Exercice (10min) PATCH Student (name)
# 4. Exercice (10min) DELETE Student

# Spécification...
# "Students" auront des "Attendances" pour des "Sessions"
# Utilisateurs, lien vers une ressource
# API vendu à des centre de formations ... "Center" -> Sessions + Students -> Attendances
