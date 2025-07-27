import asyncio
import sys
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pathlib import Path

# Add parent directory to path to import from frontend
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'frontend', 'src', 'components'))

ROOT_DIR = Path(__file__).parent.parent
load_dotenv(ROOT_DIR / 'backend' / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Portfolio data to seed
portfolio_data = {
    "profile": {
        "name": "TANISHK TIWARI",
        "title": "B.Tech Student | Future Tech Innovator",
        "location": "Delhi, India",
        "phone": "+91 9119937716",
        "email": "tiwaritanishk555ltp@gmail.com",
        "github": "https://github.com/tiwaritanishk",
        "linkedin": "https://linkedin.com/in/tanishk-tiwari",
        "website": "https://vedic-math-project.com",
        "summary": "First-year B.Tech student at Cluster Innovation Centre, University of Delhi, specializing in Information Technology and Mathematical Innovations. Passionate about research, robotics, software development, and applied mathematics."
    },
    
    "education": [
        {
            "id": "1",
            "institution": "Cluster Innovation Centre, University of Delhi",
            "degree": "B.Tech in Information Technology and Mathematical Innovations",
            "duration": "Aug 2024 – Present",
            "grade": "SGPA: 9.36",
            "order": 1
        },
        {
            "id": "2",
            "institution": "Kendriya Vidyalaya, Lalitpur (CBSE)",
            "degree": "High School (XII), Science Stream",
            "duration": "2024",
            "grade": "Percentage: 96.2% (Physics: 95, Chemistry: 99, Maths: 95)",
            "order": 2
        },
        {
            "id": "3",
            "institution": "Kendriya Vidyalaya, Lalitpur (CBSE)",
            "degree": "Secondary School (X)",
            "duration": "2022",
            "grade": "Percentage: 97.0% (Social Science: 100, Maths: 99, Science: 95)",
            "order": 3
        }
    ],

    "skills": [
        {"category": "programming", "items": ["Python", "Java", "C"]},
        {"category": "webDev", "items": ["HTML", "CSS"]},
        {"category": "tools", "items": ["GitHub", "VS Code", "Mathematica", "MATLAB", "Canva", "Figma"]},
        {"category": "cad", "items": ["Fusion 360", "FreeCAD"]},
        {"category": "concepts", "items": ["OOP", "Data Structures", "Graph Theory", "Linear Algebra", "Calculus", "Engineering Physics"]}
    ],

    "projects": [
        {
            "id": "1",
            "title": "Object Avoiding Robot",
            "date": "2024",
            "description": "Built an autonomous robot that can navigate and avoid obstacles using sensors and intelligent algorithms.",
            "image": "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/06mqxu00_image.png",
            "technologies": ["Arduino", "C++", "Sensors"],
            "type": "Robotics",
            "order": 1
        },
        {
            "id": "2",
            "title": "Line Following Robot",
            "date": "2024",
            "description": "Advanced line following robot that secured 2nd place in Convoke Techfest competition.",
            "image": "https://customer-assets.emergentagent.com/job_028c247b-bf62-4c66-9276-42cef03db150/artifacts/xntucmim_image.png",
            "technologies": ["Arduino", "C++", "IR Sensors"],
            "type": "Robotics",
            "order": 2
        },
        {
            "id": "3",
            "title": "Red Ball Game",
            "date": "2024",
            "description": "Created an engaging Red Ball game using Python and Linear Algebra concepts for physics simulation.",
            "image": "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/4i01pihx_Screenshot%202025-07-27%20000600.png",
            "technologies": ["Python", "Linear Algebra", "Physics"],
            "type": "Game",
            "order": 3
        },
        {
            "id": "4",
            "title": "Vedic Mathematics Educational Game",
            "date": "Dec 2024 – Jun 2025",
            "description": "Led the development of an interactive educational game using Python to teach Vedic Mathematics concepts.",
            "image": "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/xl8r9551_Screenshot%202025-07-27%20000941.png",
            "technologies": ["Python", "Game Development"],
            "type": "Game",
            "order": 4
        },
        {
            "id": "5",
            "title": "Java Quiz Game",
            "date": "2024",
            "description": "Built an interactive quiz-based game in Java using Java Swing to teach core programming concepts.",
            "image": "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/iht3b6cn_Screenshot%202025-07-27%20001406.png",
            "technologies": ["Java", "Swing", "GUI"],
            "type": "Game",
            "order": 5
        },
        {
            "id": "6",
            "title": "Vedic Mathematics Website",
            "date": "Dec 2024",
            "description": "Created a complete educational website to promote Vedic Maths concepts among school students. Every content on the website is created by me, including articles, examples, and interactive elements.",
            "technologies": ["Google Sites", "Web Design", "Content Creation"],
            "type": "Web",
            "link": "https://vedic-math-project.com",
            "order": 6
        },
        {
            "id": "7",
            "title": "CAD Stress Analysis & Optimization",
            "date": "Jun 2025",
            "description": "Designed complex 3D figures using Fusion 360; simulated and analyzed stress using FreeCAD for 3D printing optimization.",
            "image": "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/afua3htu_Screenshot%202024-12-30%20030852.png",
            "technologies": ["Fusion 360", "FreeCAD", "3D Printing"],
            "type": "CAD",
            "order": 7
        },
        {
            "id": "8",
            "title": "Random Graph Generator & Graph Coloring",
            "date": "Dec 2024",
            "description": "Developed a Python-based tool to generate random graphs and perform vertex coloring using Greedy and Backtracking algorithms.",
            "technologies": ["Python", "Graph Theory", "Algorithms"],
            "type": "Software",
            "order": 8
        },
        {
            "id": "9",
            "title": "Research Paper: Solar Energy and Electric Vehicles",
            "date": "Currently Working",
            "description": "Conducting comprehensive research on the integration of solar energy systems with electric vehicle technology for sustainable transportation solutions.",
            "technologies": ["Research", "Solar Energy", "Electric Vehicles", "Sustainability"],
            "type": "Research",
            "order": 9
        }
    ],

    "achievements": [
        {
            "id": "1",
            "title": "Techfest – IIT Bombay | LNMIIIT Jaipur",
            "description": "Participated in 'Meshmerize' and successfully built a Line Following Robot",
            "date": "Apr 2025",
            "order": 1
        },
        {
            "id": "2",
            "title": "Convoke Techfest - Cluster Innovation Centre",
            "description": "Secured 2nd place in Line Follower Robot (LFR) path traversal challenge",
            "date": "Oct 2024",
            "order": 2
        },
        {
            "id": "3",
            "title": "Rajya Puraskar - Bharat Scouts & Guides",
            "description": "Highest state-level scouting award certified Scout",
            "date": "2023",
            "order": 3
        },
        {
            "id": "4",
            "title": "PCRA Essay Writing Competition - State Level Winner",
            "description": "Won state level essay writing competition organized by Petroleum Conservation Research Association",
            "date": "2023",
            "order": 4
        },
        {
            "id": "5",
            "title": "Ganga Quest 2021 - National Level Winner",
            "description": "Secured national level recognition in Ganga Quest environmental awareness competition",
            "date": "2021",
            "order": 5
        },
        {
            "id": "6",
            "title": "Sanskrit Olympiad 2019 - Top 50 National Level Winner",
            "description": "Among top 50 national level winners of Sanskrit Olympiad, demonstrating excellence in classical language proficiency",
            "date": "2019",
            "order": 6
        }
    ],

    "creative_works": [
        {
            "id": "1",
            "title": "How content I was",
            "type": "Poetry",
            "date": "2024",
            "preview": "How content I was \nWith my head on your lap.\nYour hand through my hairs,\nGiving me tingling sensation \nThroughout...",
            "fullContent": """How content I was 
With my head on your lap.
Your hand through my hairs,
Giving me tingling sensation 
Throughout.

How happy I was
When you smiled at me, 
Disarmed me,
Made me feel fluffier, cozier 
Than any book can do.

How free I was
When your fingers held mine.
Hands bounded together.
Like snakes coiling,
Sucking my gloom out.

How vulnerable I was
When your head fell on my shoulder. 
Breathless, unable to move
As if my world depended on it.
And it did.

It did... It still does
But you are no longer here 
For the times have changed 
And I am left wondering 

How suffocated I was
With joy when 
My heart wasn't mine anymore 
Or with ache when
It wasn't there anymore.

For I felt so lonely
When we parted ways.
The corners turned, 
And our lives changed.
Forever."""
        }
    ],

    "photography": [
        {
            "id": "1",
            "title": "Reflections in Crimson",
            "image": "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/1yv7o9pi_WhatsApp%20Image%202025-07-27%20at%2000.24.17.jpeg",
            "description": "The warm crimson glow of burning wood creates a mesmerizing dance of flames and embers, capturing the raw beauty of fire in its natural element.",
            "order": 1
        },
        {
            "id": "2",
            "title": "Bonds Beyond Barriers", 
            "image": "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/iapo6h57_WhatsApp%20Image%202025-07-27%20at%2000.23.32.jpeg",
            "description": "Through the chains that bind, beauty blooms eternal - a metaphor for finding hope in the most constrained circumstances.",
            "order": 2
        },
        {
            "id": "3",
            "title": "Dreams of Paris",
            "image": "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/unz20c1f_WhatsApp%20Image%202025-07-27%20at%2000.23.31.jpeg",
            "description": "When wanderlust meets reality - capturing the essence of Parisian dreams through architectural elegance and cloudy aspirations.",
            "order": 3
        },
        {
            "id": "4",
            "title": "Nature's Vibrant Heart",
            "image": "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/xirg72fz_WhatsApp%20Image%202025-07-27%20at%2000.23.31%20%281%29.jpeg",
            "description": "The delicate dance of magenta petals kissed by golden sunlight - a testament to nature's artistic perfection.",
            "order": 4
        },
        {
            "id": "5",
            "title": "Heritage Illuminated",
            "image": "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/1ivscsbo_WhatsApp%20Image%202025-07-27%20at%2000.23.33.jpeg",
            "description": "A mesmerizing play of light and shadow where human silhouette meets the poetry of water reflections under the night sky.",
            "order": 5
        }
    ]
}

async def seed_database():
    print("🌱 Starting database seeding...")
    
    try:
        # Clear existing data
        await db.profile.delete_many({})
        await db.education.delete_many({})
        await db.skills.delete_many({})
        await db.projects.delete_many({})
        await db.achievements.delete_many({})
        await db.creative_works.delete_many({})
        await db.photography.delete_many({})
        
        print("🗑️  Cleared existing data")
        
        # Insert profile
        await db.profile.insert_one(portfolio_data["profile"])
        print("✅ Profile seeded")
        
        # Insert education
        await db.education.insert_many(portfolio_data["education"])
        print("✅ Education seeded")
        
        # Insert skills
        await db.skills.insert_many(portfolio_data["skills"])
        print("✅ Skills seeded")
        
        # Insert projects
        await db.projects.insert_many(portfolio_data["projects"])
        print("✅ Projects seeded")
        
        # Insert achievements
        await db.achievements.insert_many(portfolio_data["achievements"])
        print("✅ Achievements seeded")
        
        # Insert creative works
        await db.creative_works.insert_many(portfolio_data["creative_works"])
        print("✅ Creative works seeded")
        
        # Insert photography
        await db.photography.insert_many(portfolio_data["photography"])
        print("✅ Photography seeded")
        
        print("🎉 Database seeding completed successfully!")
        
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(seed_database())