from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date, time

class User(BaseModel):
    id: str
    email: EmailStr

class Activity(BaseModel):
    id: str
    title: str
    description: str
    date: date
    time: time
    location: str
    category: str

class Itinerary(BaseModel):
    user_id: str
    activities: List[str]  # List of activity IDs
