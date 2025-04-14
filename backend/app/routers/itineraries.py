from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from ..models.models import Itinerary

router = APIRouter(prefix="/itineraries", tags=["itineraries"])

itineraries_db = {}

@router.post("/", response_model=Itinerary)
async def create_itinerary(user_id: str):
    itinerary = Itinerary(user_id=user_id, activities=[])
    itineraries_db[user_id] = itinerary
    return itinerary

@router.get("/{user_id}", response_model=Itinerary)
async def get_itinerary(user_id: str):
    if user_id not in itineraries_db:
        itinerary = Itinerary(user_id=user_id, activities=[])
        itineraries_db[user_id] = itinerary
        return itinerary
    return itineraries_db[user_id]

@router.post("/{user_id}/activities/{activity_id}")
async def add_activity(user_id: str, activity_id: str):
    if user_id not in itineraries_db:
        itinerary = Itinerary(user_id=user_id, activities=[activity_id])
        itineraries_db[user_id] = itinerary
        return {"message": "Activity added to new itinerary"}
    
    if activity_id not in itineraries_db[user_id].activities:
        itineraries_db[user_id].activities.append(activity_id)
    
    return {"message": "Activity added to itinerary"}

@router.delete("/{user_id}/activities/{activity_id}")
async def remove_activity(user_id: str, activity_id: str):
    if user_id not in itineraries_db:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    
    if activity_id in itineraries_db[user_id].activities:
        itineraries_db[user_id].activities.remove(activity_id)
    
    return {"message": "Activity removed from itinerary"}
