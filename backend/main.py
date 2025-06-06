from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from .config import Config
import random

app = FastAPI(title="TheFramework World")

class Persona(BaseModel):
    id: int
    name: str
    gender: str
    age: int
    profession: str
    face_model: str

class WorldTracker(BaseModel):
    population: int
    tick: int

db: List[Persona] = []
tracker = WorldTracker(population=0, tick=0)

@app.post("/person", response_model=Persona)
def create_person(name: str, gender: str, age: int, profession: str):
    """Create a new persona with a placeholder 3D face."""
    pid = len(db) + 1
    face_model = generate_face(gender, age, profession)
    persona = Persona(id=pid, name=name, gender=gender, age=age, profession=profession, face_model=face_model)
    db.append(persona)
    tracker.population = len(db)
    return persona

@app.get("/people", response_model=List[Persona])
def list_people():
    return db

@app.get("/tracker", response_model=WorldTracker)
def get_tracker():
    return tracker

@app.post("/tick")
def advance_tick():
    tracker.tick += 1
    return tracker

def generate_face(gender: str, age: int, profession: str) -> str:
    """Placeholder for 3D face generation."""
    # Actual implementation would use Config.FACE_API_KEY
    hash_seed = f"{gender}-{age}-{profession}-{random.randint(0,9999)}"
    return f"faces/{hash_seed}.glb"
