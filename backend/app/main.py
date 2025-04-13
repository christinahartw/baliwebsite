from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg
from app.routers import users, activities, itineraries, events

app = FastAPI(title="Bali Trip Website API")

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(users.router)
app.include_router(activities.router)
app.include_router(itineraries.router)
app.include_router(events.router)

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "Welcome to the Bali Trip Website API"}
