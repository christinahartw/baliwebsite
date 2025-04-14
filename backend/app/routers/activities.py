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
        date=date(2025, 4, 17),
        time=time(22, 30),
        location="San Francisco International Airport",
        category="Transportation"
    ),
    
    "flight2": Activity(
        id="flight2",
        title="Flight from Singapore to Bali",
        description="Flight from Singapore to Bali",
        date=date(2025, 4, 19),
        time=time(9, 15),
        location="Singapore Changi Airport",
        category="Transportation"
    ),
    "arrival": Activity(
        id="arrival",
        title="Arrival in Bali",
        description="Arrival at Denpasar International Airport",
        date=date(2025, 4, 19),
        time=time(11, 0),
        location="Denpasar International Airport",
        category="Transportation"
    ),
    "checkin1": Activity(
        id="checkin1",
        title="Check-in at Como Shambhala",
        description="Arrival and check-in at the luxurious Como Shambhala retreat (Option 1)",
        date=date(2025, 4, 19),
        time=time(12, 0),
        location="Como Shambhala Estate, Ubud",
        category="Accommodation"
    ),
    "checkin2": Activity(
        id="checkin2",
        title="Check-in at Ritz-Carlton",
        description="Arrival and check-in at the Ritz-Carlton Bali (Option 2)",
        date=date(2025, 4, 19),
        time=time(12, 0),
        location="Ritz-Carlton Bali",
        category="Accommodation"
    ),
    "lunch_fri": Activity(
        id="lunch_fri",
        title="Lunch",
        description="Nutritious lunch featuring Balinese flavors",
        date=date(2025, 4, 19),
        time=time(13, 0),
        location="Resort Restaurant",
        category="Dining"
    ),
    "pool_fri": Activity(
        id="pool_fri",
        title="Afternoon Pool Time",
        description="Relax by the infinity pool with jungle views",
        date=date(2025, 4, 19),
        time=time(14, 30),
        location="Resort Pool",
        category="Relaxation"
    ),
    "gym_fri": Activity(
        id="gym_fri",
        title="Afternoon Gym Session",
        description="Guided workout at the resort's fitness center",
        date=date(2025, 4, 19),
        time=time(16, 0),
        location="Resort Gym",
        category="Fitness"
    ),
    "dinner_fri": Activity(
        id="dinner_fri",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 19),
        time=time(18, 0),
        location="Resort Restaurant",
        category="Dining"
    ),
    
    "yoga_sat": Activity(
        id="yoga_sat",
        title="Morning Yoga Session",
        description="Start your day with a rejuvenating yoga session",
        date=date(2025, 4, 20),
        time=time(8, 0),
        location="Como Shambhala Yoga Pavilion",
        category="Yoga"
    ),
    "gym_sat": Activity(
        id="gym_sat",
        title="Morning Gym Session",
        description="Guided workout at the resort's fitness center",
        date=date(2025, 4, 20),
        time=time(9, 0),
        location="Como Shambhala Gym",
        category="Fitness"
    ),
    "lunch_sat": Activity(
        id="lunch_sat",
        title="Lunch",
        description="Nutritious lunch featuring Balinese flavors",
        date=date(2025, 4, 20),
        time=time(12, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "pool_sat": Activity(
        id="pool_sat",
        title="Afternoon Pool Time",
        description="Relax by the infinity pool with jungle views",
        date=date(2025, 4, 20),
        time=time(14, 0),
        location="Como Shambhala Pool",
        category="Relaxation"
    ),
    "spa_sat": Activity(
        id="spa_sat",
        title="Spa Treatment",
        description="Relaxing spa treatment",
        date=date(2025, 4, 20),
        time=time(14, 0),
        location="Como Shambhala Spa",
        category="Relaxation"
    ),
    "dinner_sat": Activity(
        id="dinner_sat",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 20),
        time=time(18, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    
    "batur_hike": Activity(
        id="batur_hike",
        title="Mount Batur Sunrise Trek",
        description="Early morning hike to witness the sunrise from Mount Batur",
        date=date(2025, 4, 21),
        time=time(2, 30),
        location="Mount Batur",
        category="Hiking"
    ),
    "yoga_sun": Activity(
        id="yoga_sun",
        title="Early Yoga Session",
        description="Gentle yoga session after the morning hike",
        date=date(2025, 4, 21),
        time=time(7, 0),
        location="Como Shambhala Yoga Pavilion",
        category="Yoga"
    ),
    "breakfast_sun": Activity(
        id="breakfast_sun",
        title="Late Breakfast",
        description="Relaxed breakfast after the morning hike",
        date=date(2025, 4, 21),
        time=time(8, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "gym_sun": Activity(
        id="gym_sun",
        title="Morning Gym Session (Optional)",
        description="Optional light workout at the resort's fitness center",
        date=date(2025, 4, 21),
        time=time(10, 0),
        location="Como Shambhala Gym",
        category="Fitness"
    ),
    "pool_sun": Activity(
        id="pool_sun",
        title="Pool Time",
        description="Relax by the infinity pool with jungle views",
        date=date(2025, 4, 21),
        time=time(10, 0),
        location="Como Shambhala Pool",
        category="Relaxation"
    ),
    "lunch_sun": Activity(
        id="lunch_sun",
        title="Lunch",
        description="Nutritious lunch featuring Balinese flavors",
        date=date(2025, 4, 21),
        time=time(13, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "spa_sun": Activity(
        id="spa_sun",
        title="Spa Treatment",
        description="Relaxing spa treatment",
        date=date(2025, 4, 21),
        time=time(15, 0),
        location="Como Shambhala Spa",
        category="Relaxation"
    ),
    "dinner_sun": Activity(
        id="dinner_sun",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 21),
        time=time(18, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    
    "yoga_mon": Activity(
        id="yoga_mon",
        title="Morning Yoga Session",
        description="Start your day with a rejuvenating yoga session",
        date=date(2025, 4, 22),
        time=time(7, 0),
        location="Como Shambhala Yoga Pavilion",
        category="Yoga"
    ),
    "breakfast_mon": Activity(
        id="breakfast_mon",
        title="Breakfast",
        description="Healthy breakfast with fresh local ingredients",
        date=date(2025, 4, 22),
        time=time(8, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "pilates_mon": Activity(
        id="pilates_mon",
        title="Morning Pilates Class",
        description="Pilates class with jungle views",
        date=date(2025, 4, 22),
        time=time(10, 0),
        location="Como Shambhala Fitness Studio",
        category="Fitness"
    ),
    "lunch_mon": Activity(
        id="lunch_mon",
        title="Lunch",
        description="Nutritious lunch featuring Balinese flavors",
        date=date(2025, 4, 22),
        time=time(12, 30),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    "massage_mon": Activity(
        id="massage_mon",
        title="Balinese Massage",
        description="Traditional Balinese massage treatment",
        date=date(2025, 4, 22),
        time=time(15, 0),
        location="Como Shambhala Spa",
        category="Relaxation"
    ),
    "dinner_mon": Activity(
        id="dinner_mon",
        title="Dinner",
        description="Gourmet dinner with organic ingredients",
        date=date(2025, 4, 22),
        time=time(18, 0),
        location="Como Shambhala Restaurant",
        category="Dining"
    ),
    
    "checkout_tue": Activity(
        id="checkout_tue",
        title="Check-out & Transfer",
        description="Check out from Como Shambhala and transfer to Alila Uluwatu",
        date=date(2025, 4, 23),
        time=time(11, 0),
        location="Como Shambhala to Alila Uluwatu",
        category="Transportation"
    ),
    "checkin_uluwatu": Activity(
        id="checkin_uluwatu",
        title="Check-in at Alila Uluwatu",
        description="Arrival and check-in at the stunning Alila Uluwatu",
        date=date(2025, 4, 23),
        time=time(14, 0),
        location="Alila Uluwatu",
        category="Accommodation"
    ),
    "lunch_tue": Activity(
        id="lunch_tue",
        title="Lunch",
        description="Welcome lunch at Alila Uluwatu",
        date=date(2025, 4, 23),
        time=time(15, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    "pilates_tue": Activity(
        id="pilates_tue",
        title="Afternoon Pilates Class",
        description="Pilates class with ocean views",
        date=date(2025, 4, 23),
        time=time(16, 0),
        location="Alila Uluwatu Fitness Studio",
        category="Fitness"
    ),
    "yoga_tue": Activity(
        id="yoga_tue",
        title="Sunset Yoga Session",
        description="Yoga session with stunning sunset views",
        date=date(2025, 4, 23),
        time=time(17, 0),
        location="Alila Uluwatu Cliff Edge",
        category="Yoga"
    ),
    "dinner_tue": Activity(
        id="dinner_tue",
        title="Dinner",
        description="Dinner at Alila Uluwatu's signature restaurant",
        date=date(2025, 4, 23),
        time=time(19, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    
    "dive_wed": Activity(
        id="dive_wed",
        title="Morning Dive in Uluwatu",
        description="Scuba diving experience in Uluwatu's crystal waters",
        date=date(2025, 4, 24),
        time=time(6, 30),
        location="Uluwatu Dive Site",
        category="Adventure"
    ),
    "yoga_wed": Activity(
        id="yoga_wed",
        title="Morning Yoga Session",
        description="Alternative yoga session for non-divers",
        date=date(2025, 4, 24),
        time=time(7, 0),
        location="Alila Uluwatu Yoga Pavilion",
        category="Yoga"
    ),
    "breakfast_wed": Activity(
        id="breakfast_wed",
        title="Late Breakfast",
        description="Relaxed breakfast after the morning activities",
        date=date(2025, 4, 24),
        time=time(10, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    "lunch_wed": Activity(
        id="lunch_wed",
        title="Lunch",
        description="Lunch with ocean views",
        date=date(2025, 4, 24),
        time=time(13, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    "gym_wed": Activity(
        id="gym_wed",
        title="Afternoon Gym Session",
        description="Workout at Alila's fitness center",
        date=date(2025, 4, 24),
        time=time(16, 0),
        location="Alila Uluwatu Gym",
        category="Fitness"
    ),
    "yoga_sunset_wed": Activity(
        id="yoga_sunset_wed",
        title="Sunset Yoga Session",
        description="Yoga session with stunning sunset views",
        date=date(2025, 4, 24),
        time=time(17, 30),
        location="Alila Uluwatu Cliff Edge",
        category="Yoga"
    ),
    "dinner_wed": Activity(
        id="dinner_wed",
        title="Dinner",
        description="Dinner at Alila Uluwatu's signature restaurant",
        date=date(2025, 4, 24),
        time=time(18, 0),
        location="Alila Uluwatu Restaurant",
        category="Dining"
    ),
    
    "checkout_thu": Activity(
        id="checkout_thu",
        title="Check-out from Alila Uluwatu",
        description="Check out and prepare for departure",
        date=date(2025, 4, 25),
        time=time(10, 0),
        location="Alila Uluwatu",
        category="Transportation"
    ),
    "airport_transfer": Activity(
        id="airport_transfer",
        title="Transfer to Denpasar Airport",
        description="Transfer from Alila Uluwatu to Denpasar International Airport",
        date=date(2025, 4, 25),
        time=time(12, 0),
        location="Alila Uluwatu to Denpasar Airport",
        category="Transportation"
    ),
    "flight_to_singapore": Activity(
        id="flight_to_singapore",
        title="Flight to Singapore",
        description="Flight from Bali to Singapore",
        date=date(2025, 4, 25),
        time=time(15, 0),
        location="Denpasar International Airport",
        category="Transportation"
    )
}

@router.get("/", response_model=List[Activity])
async def get_activities():
    return list(activities_db.values())

@router.get("/{activity_id}", response_model=Activity)
async def get_activity(activity_id: str):
    if activity_id not in activities_db:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activities_db[activity_id]
