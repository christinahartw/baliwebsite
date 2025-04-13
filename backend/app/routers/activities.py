from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from datetime import date, time
from ..models.models import Activity

router = APIRouter(prefix="/activities", tags=["activities"])

activities_db = {
    "flight1": Activity(
        id="flight1",
        title="Flight from SF to Singapore",
        description="Departure flight from San Francisco to Singapore",
        date=date(2025, 4, 15),
        time=time(22, 30),
        location="San Francisco International Airport",
        category="Transportation"
    ),
    "flight2": Activity(
        id="flight2",
        title="Flight from Singapore to Bali",
        description="Flight from Singapore to Bali",
        date=date(2025, 4, 17),
        time=time(9, 15),
        location="Singapore Changi Airport",
        category="Transportation"
    ),
    "arrival": Activity(
        id="arrival",
        title="Arrival in Bali",
        description="Arrival at Denpasar International Airport",
        date=date(2025, 4, 17),
        time=time(11, 0),
        location="Denpasar International Airport",
        category="Transportation"
    ),
    "act1a": Activity(
        id="act1a",
        title="Check-in at Como Shambhala",
        description="Arrival and check-in at the luxurious Como Shambhala retreat (Option 1)",
        date=date(2025, 4, 17),
        time=time(12, 0),
        location="Como Shambhala Estate, Ubud",
        category="Accommodation"
    ),
    "act1b": Activity(
        id="act1b",
        title="Check-in at Ritz-Carlton",
        description="Arrival and check-in at the Ritz-Carlton Bali (Option 2)",
        date=date(2025, 4, 17),
        time=time(12, 0),
        location="Ritz-Carlton Bali",
        category="Accommodation"
    ),
    "act4": Activity(
        id="act4",
        title="Lunch",
        description="Nutritious lunch featuring Balinese flavors",
        date=date(2025, 4, 17),
        time=time(12, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act5": Activity(
        id="act5",
        title="Afternoon Gym Session",
        description="Guided workout at the resort's fitness center",
        date=date(2025, 4, 17),
        time=time(15, 0),
        location="Como Shambhala Gym",
        category="Fitness"
    ),
    "act7": Activity(
        id="act7",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 17),
        time=time(18, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    
    "act8": Activity(
        id="act8",
        title="Morning Yoga Session",
        description="Start your day with a rejuvenating yoga session",
        date=date(2025, 4, 18),
        time=time(8, 0),
        location="Como Shambhala Yoga Pavilion",
        category="Yoga"
    ),
    "act9": Activity(
        id="act9",
        title="Morning Gym Session",
        description="Guided workout at the resort's fitness center",
        date=date(2025, 4, 18),
        time=time(9, 0),
        location="Como Shambhala Gym",
        category="Fitness"
    ),
    "act10": Activity(
        id="act10",
        title="Brunch",
        description="Nutritious brunch with fresh local ingredients",
        date=date(2025, 4, 18),
        time=time(11, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act11a": Activity(
        id="act11a",
        title="Afternoon Pool Time",
        description="Relax by the infinity pool with jungle views",
        date=date(2025, 4, 18),
        time=time(13, 0),
        location="Como Shambhala Pool",
        category="Relaxation"
    ),
    "act11b": Activity(
        id="act11b",
        title="Spa Treatment",
        description="Relaxing spa treatment",
        date=date(2025, 4, 18),
        time=time(13, 0),
        location="Como Shambhala Spa",
        category="Relaxation"
    ),
    "act13": Activity(
        id="act13",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 18),
        time=time(17, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    
    "act14": Activity(
        id="act14",
        title="Mount Batur Sunrise Trek",
        description="Early morning hike to witness the sunrise from Mount Batur",
        date=date(2025, 4, 19),
        time=time(2, 30),
        location="Mount Batur",
        category="Hiking"
    ),
    "act15": Activity(
        id="act15",
        title="Early Yoga Session",
        description="Gentle yoga session after the morning hike",
        date=date(2025, 4, 19),
        time=time(7, 0),
        location="Como Shambhala Yoga Pavilion",
        category="Yoga"
    ),
    "act16": Activity(
        id="act16",
        title="Late Breakfast",
        description="Relaxed breakfast after the morning hike",
        date=date(2025, 4, 19),
        time=time(8, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act17a": Activity(
        id="act17a",
        title="Morning Gym Session",
        description="Optional light workout at the resort's fitness center",
        date=date(2025, 4, 19),
        time=time(10, 0),
        location="Como Shambhala Gym",
        category="Fitness"
    ),
    "act17b": Activity(
        id="act17b",
        title="Pool Time",
        description="Relax by the infinity pool with jungle views",
        date=date(2025, 4, 19),
        time=time(10, 0),
        location="Como Shambhala Pool",
        category="Relaxation"
    ),
    "act18": Activity(
        id="act18",
        title="Lunch",
        description="Nutritious lunch featuring Balinese flavors",
        date=date(2025, 4, 19),
        time=time(13, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act20": Activity(
        id="act20",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 19),
        time=time(18, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    
    "act21": Activity(
        id="act21",
        title="Morning Yoga Session",
        description="Start your day with a rejuvenating yoga session",
        date=date(2025, 4, 20),
        time=time(7, 0),
        location="Como Shambhala Yoga Pavilion",
        category="Yoga"
    ),
    "act22": Activity(
        id="act22",
        title="Breakfast",
        description="Healthy breakfast with fresh local ingredients",
        date=date(2025, 4, 20),
        time=time(8, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act23": Activity(
        id="act23",
        title="Lunch",
        description="Nutritious lunch featuring Balinese flavors",
        date=date(2025, 4, 20),
        time=time(12, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "act24": Activity(
        id="act24",
        title="Afternoon Gym Session",
        description="Guided workout at the resort's fitness center",
        date=date(2025, 4, 20),
        time=time(15, 0),
        location="Como Shambhala Gym",
        category="Fitness"
    ),
    "act25": Activity(
        id="act25",
        title="Balinese Massage",
        description="Traditional Balinese massage treatment",
        date=date(2025, 4, 20),
        time=time(16, 0),
        location="Como Shambhala Spa",
        category="Relaxation"
    ),
    "act26": Activity(
        id="act26",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 20),
        time=time(18, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    
    "act29": Activity(
        id="act29",
        title="Check-out & Transfer",
        description="Check out from Como Shambhala and transfer to Alila Uluwatu",
        date=date(2025, 4, 21),
        time=time(11, 0),
        location="Como Shambhala to Alila Uluwatu",
        category="Transportation"
    ),
    "act30": Activity(
        id="act30",
        title="Check-in at Alila Uluwatu",
        description="Arrival and check-in at the stunning Alila Uluwatu",
        date=date(2025, 4, 21),
        time=time(14, 0),
        location="Alila Uluwatu",
        category="Accommodation"
    ),
    "act31": Activity(
        id="act31",
        title="Lunch",
        description="Welcome lunch at Alila Uluwatu",
        date=date(2025, 4, 21),
        time=time(15, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    "act32": Activity(
        id="act32",
        title="Afternoon Pilates Class",
        description="Pilates class with ocean views",
        date=date(2025, 4, 21),
        time=time(16, 0),
        location="Alila Uluwatu Fitness Studio",
        category="Fitness"
    ),
    "act33": Activity(
        id="act33",
        title="Sunset Yoga Session",
        description="Yoga session with stunning sunset views",
        date=date(2025, 4, 21),
        time=time(17, 0),
        location="Alila Uluwatu Cliff Edge",
        category="Yoga"
    ),
    "act34": Activity(
        id="act34",
        title="Dinner",
        description="Dinner at Alila Uluwatu's signature restaurant",
        date=date(2025, 4, 21),
        time=time(19, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    
    "act35": Activity(
        id="act35",
        title="Morning Dive in Uluwatu",
        description="Scuba diving experience in Uluwatu's crystal waters",
        date=date(2025, 4, 22),
        time=time(6, 30),
        location="Uluwatu Dive Site",
        category="Adventure"
    ),
    "act36": Activity(
        id="act36",
        title="Morning Yoga Session",
        description="Alternative yoga session for non-divers",
        date=date(2025, 4, 22),
        time=time(7, 0),
        location="Alila Uluwatu Yoga Pavilion",
        category="Yoga"
    ),
    "act37": Activity(
        id="act37",
        title="Late Breakfast",
        description="Relaxed breakfast after the morning activities",
        date=date(2025, 4, 22),
        time=time(10, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    "act38": Activity(
        id="act38",
        title="Lunch",
        description="Lunch with ocean views",
        date=date(2025, 4, 22),
        time=time(13, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    "act39": Activity(
        id="act39",
        title="Afternoon Gym Session",
        description="Workout at Alila's fitness center",
        date=date(2025, 4, 22),
        time=time(16, 0),
        location="Alila Uluwatu Gym",
        category="Fitness"
    ),
    "act40": Activity(
        id="act40",
        title="Sunset Yoga Session",
        description="Yoga session with stunning sunset views",
        date=date(2025, 4, 22),
        time=time(17, 30),
        location="Alila Uluwatu Cliff Edge",
        category="Yoga"
    ),
    "act41": Activity(
        id="act41",
        title="Dinner",
        description="Dinner at Alila Uluwatu's signature restaurant",
        date=date(2025, 4, 22),
        time=time(18, 0),
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
