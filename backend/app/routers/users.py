from fastapi import APIRouter, HTTPException, Body
from pydantic import EmailStr, BaseModel
from typing import List
import uuid
from ..models.models import User

router = APIRouter(prefix="/users", tags=["users"])

users_db = {}

class UserCreate(BaseModel):
    email: EmailStr

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    user_id = str(uuid.uuid4())
    new_user = User(id=user_id, email=user.email)
    users_db[user_id] = new_user
    return new_user

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@router.get("/", response_model=List[User])
async def get_users():
    return list(users_db.values())
