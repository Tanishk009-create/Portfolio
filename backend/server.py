from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional, Any, Union
import uuid
from datetime import datetime


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Pydantic Models
class Profile(BaseModel):
    name: str
    title: str
    location: str
    phone: str
    email: str
    github: str
    linkedin: str
    website: str
    summary: str

class Education(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    institution: str
    degree: str
    duration: str
    grade: str
    order: int = 0

class Skills(BaseModel):
    category: str
    items: List[str]

class Project(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    date: str
    description: str
    image: Optional[str] = None
    technologies: List[str]
    type: str
    link: Optional[str] = None
    order: int = 0

class Achievement(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    date: str
    order: int = 0

class CreativeWork(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    type: str
    date: str
    preview: str
    fullContent: str

class Photography(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    image: str
    description: str
    order: int = 0

# API Endpoints

# Profile endpoints
@api_router.get("/profile")
async def get_profile():
    try:
        profile = await db.profile.find_one()
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        
        # Remove MongoDB _id from response
        profile.pop('_id', None)
        return {"success": True, "data": profile}
    except Exception as e:
        logging.error(f"Error fetching profile: {e}")
        return {"success": False, "message": "Failed to fetch profile"}

@api_router.put("/profile")
async def update_profile(profile: Profile):
    try:
        profile_dict = profile.dict()
        profile_dict['updatedAt'] = datetime.utcnow()
        
        result = await db.profile.replace_one({}, profile_dict, upsert=True)
        return {"success": True, "message": "Profile updated successfully"}
    except Exception as e:
        logging.error(f"Error updating profile: {e}")
        return {"success": False, "message": "Failed to update profile"}

# Education endpoints
@api_router.get("/education")
async def get_education():
    try:
        education_list = await db.education.find().sort("order", 1).to_list(100)
        for edu in education_list:
            edu.pop('_id', None)
        return {"success": True, "data": education_list}
    except Exception as e:
        logging.error(f"Error fetching education: {e}")
        return {"success": False, "message": "Failed to fetch education"}

# Skills endpoints
@api_router.get("/skills")
async def get_skills():
    try:
        skills_list = await db.skills.find().to_list(100)
        skills_dict = {}
        for skill in skills_list:
            skills_dict[skill['category']] = skill['items']
        return {"success": True, "data": skills_dict}
    except Exception as e:
        logging.error(f"Error fetching skills: {e}")
        return {"success": False, "message": "Failed to fetch skills"}

# Projects endpoints
@api_router.get("/projects")
async def get_projects(project_type: Optional[str] = None):
    try:
        query = {}
        if project_type and project_type != "All":
            query["type"] = project_type
            
        projects = await db.projects.find(query).sort("order", 1).to_list(100)
        for project in projects:
            project.pop('_id', None)
        return {"success": True, "data": projects}
    except Exception as e:
        logging.error(f"Error fetching projects: {e}")
        return {"success": False, "message": "Failed to fetch projects"}

# Achievements endpoints
@api_router.get("/achievements")
async def get_achievements():
    try:
        achievements = await db.achievements.find().sort("order", 1).to_list(100)
        for achievement in achievements:
            achievement.pop('_id', None)
        return {"success": True, "data": achievements}
    except Exception as e:
        logging.error(f"Error fetching achievements: {e}")
        return {"success": False, "message": "Failed to fetch achievements"}

# Creative works endpoints
@api_router.get("/creative-works")
async def get_creative_works():
    try:
        creative_works = await db.creative_works.find().to_list(100)
        for work in creative_works:
            work.pop('_id', None)
        return {"success": True, "data": creative_works}
    except Exception as e:
        logging.error(f"Error fetching creative works: {e}")
        return {"success": False, "message": "Failed to fetch creative works"}

# Photography endpoints
@api_router.get("/photography")
async def get_photography():
    try:
        photos = await db.photography.find().sort("order", 1).to_list(100)
        for photo in photos:
            photo.pop('_id', None)
        return {"success": True, "data": photos}
    except Exception as e:
        logging.error(f"Error fetching photography: {e}")
        return {"success": False, "message": "Failed to fetch photography"}

# Data seeding endpoint (for initial setup)
@api_router.post("/seed-data")
async def seed_data():
    try:
        # This endpoint will be used to populate initial data from mock.js
        return {"success": True, "message": "Data seeding endpoint ready"}
    except Exception as e:
        logging.error(f"Error seeding data: {e}")
        return {"success": False, "message": "Failed to seed data"}

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
