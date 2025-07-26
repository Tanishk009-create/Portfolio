// Mock data for Tanishk's portfolio
export const portfolioData = {
  profile: {
    name: "TANISHK TIWARI",
    title: "B.Tech Student | Future Tech Innovator",
    location: "Delhi, India",
    phone: "+91 9119937716",
    email: "tiwaritanishk555ltp@gmail.com",
    github: "https://github.com/tiwaritanishk",
    linkedin: "https://linkedin.com/in/tanishk-tiwari",
    website: "https://vedic-math-project.com",
    summary: "B.Tech student at Cluster Innovation Centre, University of Delhi, specializing in Information Technology and Mathematical Innovations. Passionate about research, robotics, software development, and applied mathematics."
  },
  
  education: [
    {
      institution: "Cluster Innovation Centre, University of Delhi",
      degree: "B.Tech in Information Technology and Mathematical Innovations",
      duration: "Aug 2024 – Present",
      grade: "SGPA: 9.36"
    },
    {
      institution: "Kendriya Vidyalaya, Lalitpur (CBSE)",
      degree: "High School (XII), Science Stream",
      duration: "2024",
      grade: "Percentage: 96.2% (Physics: 95, Chemistry: 99, Maths: 95)"
    },
    {
      institution: "Kendriya Vidyalaya, Lalitpur (CBSE)",
      degree: "Secondary School (X)",
      duration: "2022",
      grade: "Percentage: 97.0% (Social Science: 100, Maths: 99, Science: 95)"
    }
  ],

  skills: {
    programming: ["Python", "Java", "C"],
    webDev: ["HTML", "CSS"],
    tools: ["GitHub", "VS Code", "Mathematica", "MATLAB", "Canva", "Figma"],
    cad: ["Fusion 360", "FreeCAD"],
    concepts: ["OOP", "Data Structures", "Graph Theory", "Linear Algebra", "Calculus", "Engineering Physics"]
  },

  projects: [
    // Robotics Projects First
    {
      id: 1,
      title: "Object Avoiding Robot",
      date: "2024",
      description: "Built an autonomous robot that can navigate and avoid obstacles using sensors and intelligent algorithms.",
      image: "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/06mqxu00_image.png",
      technologies: ["Arduino", "C++", "Sensors"],
      type: "Robotics"
    },
    {
      id: 2,
      title: "Line Following Robot",
      date: "2024",
      description: "Advanced line following robot that secured 2nd place in Convoke Techfest competition.",
      image: "https://customer-assets.emergentagent.com/job_028c247b-bf62-4c66-9276-42cef03db150/artifacts/xntucmim_image.png",
      technologies: ["Arduino", "C++", "IR Sensors"],
      type: "Robotics"
    },
    
    // Games Second
    {
      id: 3,
      title: "Red Ball Game",
      date: "2024",
      description: "Created an engaging Red Ball game using Python and Linear Algebra concepts for physics simulation.",
      image: "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/4i01pihx_Screenshot%202025-07-27%20000600.png",
      technologies: ["Python", "Linear Algebra", "Physics"],
      type: "Game"
    },
    {
      id: 4,
      title: "Vedic Mathematics Educational Game",
      date: "Dec 2024 – Jun 2025",
      description: "Led the development of an interactive educational game using Python to teach Vedic Mathematics concepts.",
      image: "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/xl8r9551_Screenshot%202025-07-27%20000941.png",
      technologies: ["Python", "Game Development"],
      type: "Game"
    },
    {
      id: 5,
      title: "Java Quiz Game",
      date: "2024",
      description: "Built an interactive quiz-based game in Java using Java Swing to teach core programming concepts.",
      image: "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/iht3b6cn_Screenshot%202025-07-27%20001406.png",
      technologies: ["Java", "Swing", "GUI"],
      type: "Game"
    },
    
    // Website Third
    {
      id: 6,
      title: "Vedic Mathematics Website",
      date: "Dec 2024",
      description: "Created a complete educational website to promote Vedic Maths concepts among school students. Every content on the website is created by me, including articles, examples, and interactive elements.",
      technologies: ["Google Sites", "Web Design", "Content Creation"],
      type: "Web",
      link: "https://vedic-math-project.com"
    },
    
    // CAD Fourth
    {
      id: 7,
      title: "CAD Stress Analysis & Optimization",
      date: "Jun 2025",
      description: "Designed complex 3D figures using Fusion 360; simulated and analyzed stress using FreeCAD for 3D printing optimization.",
      image: "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/afua3htu_Screenshot%202024-12-30%20030852.png",
      technologies: ["Fusion 360", "FreeCAD", "3D Printing"],
      type: "CAD"
    },
    
    // Software/Research Last
    {
      id: 8,
      title: "Random Graph Generator & Graph Coloring",
      date: "Dec 2024",
      description: "Developed a Python-based tool to generate random graphs and perform vertex coloring using Greedy and Backtracking algorithms.",
      technologies: ["Python", "Graph Theory", "Algorithms"],
      type: "Software"
    },
    {
      id: 9,
      title: "Research Paper: Solar Energy and Electric Vehicles",
      date: "Currently Working",
      description: "Conducting comprehensive research on the integration of solar energy systems with electric vehicle technology for sustainable transportation solutions.",
      technologies: ["Research", "Solar Energy", "Electric Vehicles", "Sustainability"],
      type: "Research"
    }
  ],

  achievements: [
    {
      title: "Techfest – IIT Bombay | LNMIIT Jaipur", 
      description: "Participated in 'Meshmerize' and successfully built a Line Following Robot",
      date: "Apr 2025"
    },
    {
      title: "Convoke Techfest - Cluster Innovation Centre",
      description: "Secured 2nd place in Line Follower Robot (LFR) path traversal challenge",
      date: "Oct 2024"
    },
    {
      title: "Rajya Puraskar - Bharat Scouts & Guides",
      description: "Highest state-level scouting award certified Scout",
      date: "2023"
    },
    {
      title: "PCRA Essay Writing Competition - State Level Winner",
      description: "Won state level essay writing competition organized by Petroleum Conservation Research Association",
      date: "2023"
    },
    {
      title: "Ganga Quest 2021 - National Level Winner",
      description: "Secured national level recognition in Ganga Quest environmental awareness competition",
      date: "2021"
    },
    {
      title: "Sanskrit Olympiad 2019 - Top 50 National Level Winner",
      description: "Among top 50 national level winners of Sanskrit Olympiad, demonstrating excellence in classical language proficiency",
      date: "2019"
    }
  ],

  creativeWorks: [
    {
      id: 1,
      title: "How content I was",
      type: "Poetry",
      date: "2024",
      preview: "How content I was \nWith my head on your lap.\nYour hand through my hairs,\nGiving me tingling sensation \nThroughout...",
      fullContent: `How content I was 
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
Forever.`
    }
  ],

  photography: [
    {
      id: 1,
      title: "Reflections in Crimson",
      image: "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/1ivscsbo_WhatsApp%20Image%202025-07-27%20at%2000.23.33.jpeg",
      description: "A mesmerizing play of light and shadow where human silhouette meets the poetry of water reflections under the night sky."
    },
    {
      id: 2,
      title: "Bonds Beyond Barriers", 
      image: "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/iapo6h57_WhatsApp%20Image%202025-07-27%20at%2000.23.32.jpeg",
      description: "Through the chains that bind, beauty blooms eternal - a metaphor for finding hope in the most constrained circumstances."
    },
    {
      id: 3,
      title: "Dreams of Paris",
      image: "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/unz20c1f_WhatsApp%20Image%202025-07-27%20at%2000.23.31.jpeg", 
      description: "When wanderlust meets reality - capturing the essence of Parisian dreams through architectural elegance and cloudy aspirations."
    },
    {
      id: 4,
      title: "Nature's Vibrant Heart",
      image: "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/xirg72fz_WhatsApp%20Image%202025-07-27%20at%2000.23.31%20%281%29.jpeg",
      description: "The delicate dance of magenta petals kissed by golden sunlight - a testament to nature's artistic perfection."
    },
    {
      id: 5,
      title: "Heritage Illuminated",
      image: "https://customer-assets.emergentagent.com/job_it-math-innovator/artifacts/1yv7o9pi_WhatsApp%20Image%202025-07-27%20at%2000.24.17.jpeg",
      description: "The majestic Qutub Minar standing tall against the darkness, its ancient stones telling stories of centuries past through modern illumination."
    }
  ]
};