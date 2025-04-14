from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from typing import List, Optional
import uuid
from ..models.models import User

router = APIRouter(prefix="/users", tags=["users"])

users_db = {}
handle_to_id = {}  # Map handles to user IDs for quick lookup

class UserCreate(BaseModel):
    handle: str

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    if user.handle in handle_to_id:
        existing_user_id = handle_to_id[user.handle]
        return users_db[existing_user_id]
    
    user_id = str(uuid.uuid4())
    new_user = User(id=user_id, handle=user.handle)
    users_db[user_id] = new_user
    handle_to_id[user.handle] = user_id
    return new_user

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@router.get("/by-handle/{handle}", response_model=Optional[User])
async def get_user_by_handle(handle: str):
    if handle not in handle_to_id:
        return None
    user_id = handle_to_id[handle]
    return users_db[user_id]

@router.get("/", response_model=List[User])
async def get_users():
    return list(users_db.values())
