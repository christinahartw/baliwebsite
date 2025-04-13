from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from datetime import date, time
from ..models.models import Activity

router = APIRouter(prefix="/activities", tags=["activities"])

activities_db = {
    "act1": Activity(
        id="act1",
        title="Check-in at Como Shambhala",
        description="Arrival and check-in at the luxurious Como Shambhala retreat",
        date=date(2025, 4, 18),
        time=time(14, 0),
        location="Como Shambhala Estate, Ubud",
        category="Accommodation"
    ),
    "act2": Activity(
        id="act2",
        title="Morning Yoga Session",
        description="Start your day with a rejuvenating yoga session",
        date=date(2025, 4, 18),
        time=time(7, 0),
        location="Como Shambhala Yoga Pavilion",
        category="Yoga"
    ),
    "act3": Activity(
        id="act3",
        title="Breakfast",
        description="Healthy breakfast with fresh local ingredients",
        date=date(2025, 4, 18),
        time=time(8, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act4": Activity(
        id="act4",
        title="Lunch",
        description="Nutritious lunch featuring Balinese flavors",
        date=date(2025, 4, 18),
        time=time(12, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act5": Activity(
        id="act5",
        title="Afternoon Gym Session",
        description="Guided workout at the resort's fitness center",
        date=date(2025, 4, 18),
        time=time(16, 0),
        location="Como Shambhala Gym",
        category="Fitness"
    ),
    "act6": Activity(
        id="act6",
        title="Pool Time",
        description="Relax by the infinity pool with jungle views",
        date=date(2025, 4, 18),
        time=time(17, 30),
        location="Como Shambhala Pool",
        category="Relaxation"
    ),
    "act7": Activity(
        id="act7",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 18),
        time=time(19, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    
    "act8": Activity(
        id="act8",
        title="Morning Yoga Session",
        description="Start your day with a rejuvenating yoga session",
        date=date(2025, 4, 19),
        time=time(7, 0),
        location="Como Shambhala Yoga Pavilion",
        category="Yoga"
    ),
    "act9": Activity(
        id="act9",
        title="Breakfast",
        description="Healthy breakfast with fresh local ingredients",
        date=date(2025, 4, 19),
        time=time(8, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act10": Activity(
        id="act10",
        title="Lunch",
        description="Nutritious lunch featuring Balinese flavors",
        date=date(2025, 4, 19),
        time=time(12, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act11": Activity(
        id="act11",
        title="Afternoon Gym Session",
        description="Guided workout at the resort's fitness center",
        date=date(2025, 4, 19),
        time=time(16, 0),
        location="Como Shambhala Gym",
        category="Fitness"
    ),
    "act12": Activity(
        id="act12",
        title="Pool Time",
        description="Relax by the infinity pool with jungle views",
        date=date(2025, 4, 19),
        time=time(17, 30),
        location="Como Shambhala Pool",
        category="Relaxation"
    ),
    "act13": Activity(
        id="act13",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 19),
        time=time(19, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    
    "act14": Activity(
        id="act14",
        title="Mount Batur Sunrise Trek",
        description="Early morning hike to witness the sunrise from Mount Batur",
        date=date(2025, 4, 20),
        time=time(2, 30),
        location="Mount Batur",
        category="Hiking"
    ),
    "act15": Activity(
        id="act15",
        title="Late Breakfast",
        description="Relaxed breakfast after the morning hike",
        date=date(2025, 4, 20),
        time=time(10, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act16": Activity(
        id="act16",
        title="Lunch",
        description="Nutritious lunch featuring Balinese flavors",
        date=date(2025, 4, 20),
        time=time(13, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act17": Activity(
        id="act17",
        title="Afternoon Yoga Session",
        description="Gentle yoga session to recover from the morning hike",
        date=date(2025, 4, 20),
        time=time(16, 0),
        location="Como Shambhala Yoga Pavilion",
        category="Yoga"
    ),
    "act18": Activity(
        id="act18",
        title="Afternoon Gym Session",
        description="Optional light workout at the resort's fitness center",
        date=date(2025, 4, 20),
        time=time(17, 30),
        location="Como Shambhala Gym",
        category="Fitness"
    ),
    "act19": Activity(
        id="act19",
        title="Pool Time",
        description="Relax by the infinity pool with jungle views",
        date=date(2025, 4, 20),
        time=time(18, 30),
        location="Como Shambhala Pool",
        category="Relaxation"
    ),
    "act20": Activity(
        id="act20",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 20),
        time=time(20, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    
    "act21": Activity(
        id="act21",
        title="Morning Yoga Session",
        description="Start your day with a rejuvenating yoga session",
        date=date(2025, 4, 21),
        time=time(7, 0),
        location="Como Shambhala Yoga Pavilion",
        category="Yoga"
    ),
    "act22": Activity(
        id="act22",
        title="Breakfast",
        description="Healthy breakfast with fresh local ingredients",
        date=date(2025, 4, 21),
        time=time(8, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act23": Activity(
        id="act23",
        title="Lunch",
        description="Nutritious lunch featuring Balinese flavors",
        date=date(2025, 4, 21),
        time=time(12, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act24": Activity(
        id="act24",
        title="Afternoon Gym Session",
        description="Guided workout at the resort's fitness center",
        date=date(2025, 4, 21),
        time=time(15, 0),
        location="Como Shambhala Gym",
        category="Fitness"
    ),
    "act25": Activity(
        id="act25",
        title="Balinese Massage",
        description="Traditional Balinese massage treatment",
        date=date(2025, 4, 21),
        time=time(17, 0),
        location="Como Shambhala Spa",
        category="Relaxation"
    ),
    "act26": Activity(
        id="act26",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 21),
        time=time(19, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    
    "act27": Activity(
        id="act27",
        title="Morning Yoga Session",
        description="Final yoga session at Como Shambhala",
        date=date(2025, 4, 22),
        time=time(7, 0),
        location="Como Shambhala Yoga Pavilion",
        category="Yoga"
    ),
    "act28": Activity(
        id="act28",
        title="Breakfast",
        description="Healthy breakfast with fresh local ingredients",
        date=date(2025, 4, 22),
        time=time(8, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act29": Activity(
        id="act29",
        title="Check-out & Transfer",
        description="Check out from Como Shambhala and transfer to Alila Uluwatu",
        date=date(2025, 4, 22),
        time=time(11, 0),
        location="Como Shambhala to Alila Uluwatu",
        category="Transportation"
    ),
    "act30": Activity(
        id="act30",
        title="Check-in at Alila Uluwatu",
        description="Arrival and check-in at the stunning Alila Uluwatu",
        date=date(2025, 4, 22),
        time=time(14, 0),
        location="Alila Uluwatu",
        category="Accommodation"
    ),
    "act31": Activity(
        id="act31",
        title="Lunch",
        description="Welcome lunch at Alila Uluwatu",
        date=date(2025, 4, 22),
        time=time(15, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    "act32": Activity(
        id="act32",
        title="Afternoon Yoga Session",
        description="Yoga session with ocean views",
        date=date(2025, 4, 22),
        time=time(17, 0),
        location="Alila Uluwatu Yoga Pavilion",
        category="Yoga"
    ),
    "act33": Activity(
        id="act33",
        title="Dinner",
        description="Dinner at Alila Uluwatu's signature restaurant",
        date=date(2025, 4, 22),
        time=time(19, 30),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    
    "act34": Activity(
        id="act34",
        title="Morning Dive in Uluwatu",
        description="Scuba diving experience in Uluwatu's crystal waters",
        date=date(2025, 4, 23),
        time=time(6, 30),
        location="Uluwatu Dive Site",
        category="Adventure"
    ),
    "act35": Activity(
        id="act35",
        title="Late Breakfast",
        description="Relaxed breakfast after the morning dive",
        date=date(2025, 4, 23),
        time=time(10, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    "act36": Activity(
        id="act36",
        title="Morning Yoga Session",
        description="Alternative yoga session for non-divers",
        date=date(2025, 4, 23),
        time=time(7, 0),
        location="Alila Uluwatu Yoga Pavilion",
        category="Yoga"
    ),
    "act37": Activity(
        id="act37",
        title="Lunch",
        description="Lunch with ocean views",
        date=date(2025, 4, 23),
        time=time(13, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    "act38": Activity(
        id="act38",
        title="Afternoon Gym Session",
        description="Workout at Alila's fitness center",
        date=date(2025, 4, 23),
        time=time(16, 0),
        location="Alila Uluwatu Gym",
        category="Fitness"
    ),
    "act39": Activity(
        id="act39",
        title="Sunset Yoga Session",
        description="Yoga session with stunning sunset views",
        date=date(2025, 4, 23),
        time=time(17, 30),
        location="Alila Uluwatu Cliff Edge",
        category="Yoga"
    ),
    "act40": Activity(
        id="act40",
        title="Dinner",
        description="Dinner at Alila Uluwatu's signature restaurant",
        date=date(2025, 4, 23),
        time=time(19, 30),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    
    "act41": Activity(
        id="act41",
        title="Morning Yoga Session",
        description="Final yoga session of the trip",
        date=date(2025, 4, 24),
        time=time(7, 0),
        location="Alila Uluwatu Yoga Pavilion",
        category="Yoga"
    ),
    "act42": Activity(
        id="act42",
        title="Breakfast",
        description="Farewell breakfast",
        date=date(2025, 4, 24),
        time=time(8, 30),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    "act43": Activity(
        id="act43",
        title="Check-out & Departure",
        description="Check out from Alila Uluwatu and transfer to airport",
        date=date(2025, 4, 24),
        time=time(12, 0),
        location="Alila Uluwatu",
        category="Transportation"
    ),
    "act44": Activity(
        id="act44",
        title="Farewell Lunch",
        description="Optional lunch before departure",
        date=date(2025, 4, 24),
        time=time(13, 0),
        location="Alila Uluwatu Restaurant",
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
