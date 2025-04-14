from fastapi import APIRouter, HTTPException, Body, Depends
from typing import List
import uuid
from datetime import datetime
from ..models.models import UserEvent, UserEventCreate

router = APIRouter(prefix="/events", tags=["events"])

events_db = {}

@router.post("/", response_model=UserEvent)
async def create_event(event: UserEventCreate, user_id: str = Body(...)):
    """Create a new user event that will be visible to all users"""
    event_id = str(uuid.uuid4())
    
    new_event = UserEvent(
        id=event_id,
        user_id=user_id,
        title=event.title,
        description=event.description,
        date=event.date,  # Now accepts string format
        time=event.time,  # Now accepts string format
        link=event.link,
        created_at=datetime.now().isoformat()
    )
    
    events_db[event_id] = new_event
    return new_event

@router.get("/", response_model=List[UserEvent])
async def get_events():
    """Get all user-created events"""
    return list(events_db.values())

@router.get("/{event_id}", response_model=UserEvent)
async def get_event(event_id: str):
    """Get a specific user event by ID"""
    if event_id not in events_db:
        raise HTTPException(status_code=404, detail="Event not found")
    return events_db[event_id]

@router.delete("/{event_id}")
async def delete_event(event_id: str, user_id: str = Body(...)):
    """Delete a user event (only the creator can delete their events)"""
    if event_id not in events_db:
        raise HTTPException(status_code=404, detail="Event not found")
    
    event = events_db[event_id]
    if event.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this event")
    
    del events_db[event_id]
    return {"message": "Event deleted successfully"}
