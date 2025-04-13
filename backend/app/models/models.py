from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import date, time

class User(BaseModel):
    id: str
    handle: str

class Activity(BaseModel):
    id: str
    title: str
    description: str
    date: date
    time: time
    location: str
    category: str

class UserEvent(BaseModel):
    id: str
    user_id: str
    title: str
    description: str
    date: date
    time: time
    link: Optional[HttpUrl] = None
    created_at: Optional[str] = None

class UserEventCreate(BaseModel):
    title: str
    description: str
    date: date
    time: time
    link: Optional[HttpUrl] = None

class Itinerary(BaseModel):
    user_id: str
    activities: List[str]  # List of activity IDs
