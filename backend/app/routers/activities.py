from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from datetime import date, time
from ..models.models import Activity

router = APIRouter(prefix="/activities", tags=["activities"])

activities_db = {
    "act1": Activity(
        id="act1",
        title="Mount Batur Sunrise Trek",
        description="Early morning hike to witness the sunrise from Mount Batur",
        date=date(2025, 4, 18),
        time=time(4, 0),
        location="Mount Batur",
        category="Hiking"
    ),
    "act2": Activity(
        id="act2",
        title="Ubud Monkey Forest Visit",
        description="Explore the sacred monkey forest sanctuary",
        date=date(2025, 4, 18),
        time=time(14, 0),
        location="Ubud",
        category="Nature"
    ),
    "act3": Activity(
        id="act3",
        title="Tegallalang Rice Terraces",
        description="Visit the famous stepped rice paddies",
        date=date(2025, 4, 19),
        time=time(10, 0),
        location="Tegallalang",
        category="Sightseeing"
    ),
    "act4": Activity(
        id="act4",
        title="Uluwatu Temple Sunset & Kecak Dance",
        description="Watch traditional Kecak dance at sunset",
        date=date(2025, 4, 19),
        time=time(17, 0),
        location="Uluwatu",
        category="Cultural"
    ),
    "act5": Activity(
        id="act5",
        title="Nusa Penida Island Tour",
        description="Day trip to Nusa Penida island",
        date=date(2025, 4, 20),
        time=time(8, 0),
        location="Nusa Penida",
        category="Tour"
    ),
    "act6": Activity(
        id="act6",
        title="Bali Swing Experience",
        description="Try out the famous Bali swing with rice terrace views",
        date=date(2025, 4, 20),
        time=time(15, 0),
        location="Ubud",
        category="Adventure"
    ),
    "act7": Activity(
        id="act7",
        title="Waterbom Bali",
        description="Day at Bali's premier waterpark",
        date=date(2025, 4, 21),
        time=time(10, 0),
        location="Kuta",
        category="Recreation"
    ),
    "act8": Activity(
        id="act8",
        title="Seminyak Beach Sunset",
        description="Relax at Seminyak beach and watch the sunset",
        date=date(2025, 4, 21),
        time=time(17, 0),
        location="Seminyak",
        category="Relaxation"
    ),
    "act9": Activity(
        id="act9",
        title="Tanah Lot Temple Visit",
        description="Visit the iconic sea temple",
        date=date(2025, 4, 22),
        time=time(16, 0),
        location="Tanah Lot",
        category="Cultural"
    ),
    "act10": Activity(
        id="act10",
        title="Ubud Art Market Shopping",
        description="Shop for souvenirs and local crafts",
        date=date(2025, 4, 22),
        time=time(10, 0),
        location="Ubud",
        category="Shopping"
    ),
    "act11": Activity(
        id="act11",
        title="Jimbaran Bay Seafood Dinner",
        description="Fresh seafood dinner on the beach",
        date=date(2025, 4, 23),
        time=time(18, 0),
        location="Jimbaran",
        category="Dining"
    ),
    "act12": Activity(
        id="act12",
        title="Ulun Danu Beratan Temple",
        description="Visit the lakeside temple in the mountains",
        date=date(2025, 4, 23),
        time=time(9, 0),
        location="Bedugul",
        category="Cultural"
    ),
    "act13": Activity(
        id="act13",
        title="Bali Coffee Plantation Tour",
        description="Learn about coffee production and taste Luwak coffee",
        date=date(2025, 4, 24),
        time=time(10, 0),
        location="Ubud",
        category="Tour"
    ),
    "act14": Activity(
        id="act14",
        title="Farewell Dinner",
        description="Group dinner to conclude the trip",
        date=date(2025, 4, 24),
        time=time(19, 0),
        location="Seminyak",
        category="Dining"
    ),
}

@router.get("/", response_model=List[Activity])
async def get_activities():
    return list(activities_db.values())

@router.get("/{activity_id}", response_model=Activity)
async def get_activity(activity_id: str):
    if activity_id not in activities_db:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activities_db[activity_id]
