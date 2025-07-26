# Portfolio Backend API Contracts

## Overview
This document outlines the API contracts for Tanishk's portfolio website backend implementation. The frontend currently uses mock data that needs to be migrated to a MongoDB-based backend.

## Current Mock Data Structure

### 1. Profile Information
```javascript
profile: {
  name, title, location, phone, email, github, linkedin, website, summary
}
```

### 2. Education Records
```javascript
education: [
  { institution, degree, duration, grade }
]
```

### 3. Skills Categories
```javascript
skills: {
  programming: [],
  webDev: [],
  tools: [],
  cad: [],
  concepts: []
}
```

### 4. Projects
```javascript
projects: [
  { id, title, date, description, image?, technologies, type, link? }
]
```

### 5. Achievements
```javascript
achievements: [
  { title, description, date }
]
```

### 6. Creative Works
```javascript
creativeWorks: [
  { id, title, type, date, preview, fullContent }
]
```

### 7. Photography
```javascript
photography: [
  { id, title, image, description }
]
```

## API Endpoints to Implement

### Profile Management
- `GET /api/profile` - Get profile information
- `PUT /api/profile` - Update profile information

### Education
- `GET /api/education` - Get all education records
- `POST /api/education` - Add new education record
- `PUT /api/education/:id` - Update education record
- `DELETE /api/education/:id` - Delete education record

### Skills
- `GET /api/skills` - Get all skills categorized
- `PUT /api/skills` - Update skills (bulk update)

### Projects
- `GET /api/projects` - Get all projects
- `GET /api/projects?type=Robotics` - Filter projects by type
- `POST /api/projects` - Add new project
- `PUT /api/projects/:id` - Update project
- `DELETE /api/projects/:id` - Delete project

### Achievements
- `GET /api/achievements` - Get all achievements (sorted by date desc)
- `POST /api/achievements` - Add new achievement
- `PUT /api/achievements/:id` - Update achievement
- `DELETE /api/achievements/:id` - Delete achievement

### Creative Works
- `GET /api/creative-works` - Get all creative works
- `POST /api/creative-works` - Add new creative work
- `PUT /api/creative-works/:id` - Update creative work
- `DELETE /api/creative-works/:id` - Delete creative work

### Photography
- `GET /api/photography` - Get all photos
- `POST /api/photography` - Add new photo
- `PUT /api/photography/:id` - Update photo
- `DELETE /api/photography/:id` - Delete photo

## MongoDB Models

### Profile Model
```javascript
{
  _id: ObjectId,
  name: String,
  title: String,
  location: String,
  phone: String,
  email: String,
  github: String,
  linkedin: String,
  website: String,
  summary: String,
  createdAt: Date,
  updatedAt: Date
}
```

### Education Model
```javascript
{
  _id: ObjectId,
  institution: String,
  degree: String,
  duration: String,
  grade: String,
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

### Skills Model
```javascript
{
  _id: ObjectId,
  category: String, // 'programming', 'webDev', 'tools', 'cad', 'concepts'
  items: [String],
  createdAt: Date,
  updatedAt: Date
}
```

### Project Model
```javascript
{
  _id: ObjectId,
  title: String,
  date: String,
  description: String,
  image: String (optional),
  technologies: [String],
  type: String, // 'Robotics', 'Game', 'Web', 'CAD', 'Software', 'Research'
  link: String (optional),
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

### Achievement Model
```javascript
{
  _id: ObjectId,
  title: String,
  description: String,
  date: String,
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

### CreativeWork Model
```javascript
{
  _id: ObjectId,
  title: String,
  type: String, // 'Poetry', 'Essay', etc.
  date: String,
  preview: String,
  fullContent: String,
  createdAt: Date,
  updatedAt: Date
}
```

### Photography Model
```javascript
{
  _id: ObjectId,
  title: String,
  image: String,
  description: String,
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

## Frontend Integration Plan

### 1. Create API Service Layer
- Replace mock.js with apiService.js
- Create HTTP client functions for each endpoint
- Handle loading states and error handling

### 2. Update Components
- Replace direct mock data imports with API calls
- Add loading spinners and error messages
- Implement optimistic updates where appropriate

### 3. State Management
- Use React hooks (useState, useEffect) for data fetching
- Implement local state management for form submissions
- Add refresh mechanisms

### 4. Error Handling
- Display user-friendly error messages
- Implement retry mechanisms
- Add fallback UI states

## Implementation Priority

1. **Phase 1**: Profile, Education, Skills (read-only)
2. **Phase 2**: Projects and Achievements (read-only)
3. **Phase 3**: Creative Works and Photography (read-only)
4. **Phase 4**: Add CRUD operations (if needed for admin functionality)

## Data Migration Strategy
1. Create database seeder script with current mock data
2. Insert initial data into MongoDB collections
3. Test API endpoints with Thunderclient/Postman
4. Update frontend components one by one
5. Remove mock.js file after complete migration

## Notes
- All endpoints should return consistent response format: `{ success: boolean, data: any, message?: string }`
- Implement proper error handling and validation
- Add request logging for debugging
- Consider pagination for large datasets (projects, photos)
- Maintain backward compatibility during migration