import React, { useState, useEffect } from 'react';
import { Github, Linkedin, Mail, Phone, MapPin, ExternalLink, Code, Database, Wrench, Brain, Trophy, Calendar, ChevronDown } from 'lucide-react';
import { portfolioData } from './mock';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { Button } from './ui/button';
import { Separator } from './ui/separator';

const Portfolio = () => {
  const [activeSection, setActiveSection] = useState('hero');
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    setIsLoaded(true);
  }, []);

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setActiveSection(sectionId);
    }
  };

  const skillCategories = [
    { name: 'Programming Languages', items: portfolioData.skills.programming, icon: Code },
    { name: 'Web Development', items: portfolioData.skills.webDev, icon: Database },
    { name: 'Tools & Platforms', items: portfolioData.skills.tools, icon: Wrench },
    { name: 'CAD & Simulation', items: portfolioData.skills.cad, icon: Wrench },
    { name: 'Core Concepts', items: portfolioData.skills.concepts, icon: Brain }
  ];

  const projectTypes = ['All', 'Robotics', 'Software', 'Game', 'Web', 'CAD', 'Research'];
  const [selectedType, setSelectedType] = useState('All');

  const filteredProjects = selectedType === 'All' 
    ? portfolioData.projects 
    : portfolioData.projects.filter(project => project.type === selectedType);

  return (
    <div className="min-h-screen bg-gray-900 text-gray-100">
      {/* Tech Grid Background */}
      <div className="fixed inset-0 opacity-5 pointer-events-none">
        <div className="absolute inset-0" style={{
          backgroundImage: `
            linear-gradient(rgba(59, 130, 246, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(59, 130, 246, 0.1) 1px, transparent 1px)
          `,
          backgroundSize: '50px 50px'
        }} />
      </div>

      {/* Navigation Header */}
      <nav className="fixed top-0 w-full z-50 bg-gray-900/95 backdrop-blur-sm border-b border-gray-800">
        <div className="container mx-auto px-6 py-4">
          <div className="flex justify-between items-center">
            <div className="text-xl font-bold text-blue-400">Portfolio</div>
            <div className="hidden md:flex space-x-8">
              {['hero', 'about', 'education', 'skills', 'projects', 'achievements', 'creative', 'contact'].map((section) => (
                <button
                  key={section}
                  onClick={() => scrollToSection(section)}
                  className={`capitalize hover:text-blue-400 transition-colors ${
                    activeSection === section ? 'text-blue-400' : 'text-gray-300'
                  }`}
                >
                  {section === 'creative' ? 'Creative Works' : section}
                </button>
              ))}
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section id="hero" className="min-h-screen flex items-center justify-center relative pt-20">
        <div className="container mx-auto px-6 text-center">
          <div className={`transition-all duration-1000 ${isLoaded ? 'translate-y-0 opacity-100' : 'translate-y-10 opacity-0'}`}>
            <h1 className="text-5xl md:text-7xl font-bold mb-6 bg-gradient-to-r from-blue-400 via-purple-500 to-blue-600 bg-clip-text text-transparent">
              {portfolioData.profile.name}
            </h1>
            <h2 className="text-xl md:text-2xl text-gray-300 mb-8 font-light">
              {portfolioData.profile.title}
            </h2>
            <div className="flex items-center justify-center space-x-4 text-gray-400 mb-8">
              <MapPin className="w-5 h-5" />
              <span>Delhi, India</span>
            </div>
            <p className="text-lg text-gray-300 max-w-3xl mx-auto mb-12 leading-relaxed">
              {portfolioData.profile.summary}
            </p>
            <div className="flex justify-center space-x-4">
              <Button onClick={() => scrollToSection('projects')} className="bg-blue-600 hover:bg-blue-700">
                View Projects
              </Button>
              <Button onClick={() => scrollToSection('contact')} variant="outline" className="border-gray-600 text-gray-300 hover:bg-gray-800">
                Contact Me
              </Button>
            </div>
          </div>
        </div>
        <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
          <ChevronDown className="w-6 h-6 text-gray-400" />
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="py-20 bg-gray-800/50">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-16 text-blue-400">About Me</h2>
          <div className="max-w-4xl mx-auto">
            <Card className="bg-gray-800 border-gray-700">
              <CardContent className="p-8">
                <p className="text-lg text-gray-300 leading-relaxed">
                  I'm a first-year B.Tech student at Cluster Innovation Centre, University of Delhi, 
                  passionate about pushing the boundaries of technology through research, robotics, 
                  and software development. My journey combines strong academic excellence with 
                  hands-on technical projects, from building autonomous robots to developing 
                  educational games and web applications.
                </p>
                <Separator className="my-6 bg-gray-700" />
                <p className="text-lg text-gray-300 leading-relaxed">
                  With expertise in multiple programming languages and a strong foundation in 
                  mathematical concepts, I strive to create impactful tech-driven solutions 
                  that bridge theoretical knowledge with practical innovation.
                </p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Education Section */}
      <section id="education" className="py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-16 text-blue-400">Education</h2>
          <div className="max-w-4xl mx-auto space-y-6">
            {portfolioData.education.map((edu, index) => (
              <Card key={index} className="bg-gray-800 border-gray-700 hover:border-blue-500/50 transition-colors">
                <CardContent className="p-6">
                  <div className="flex flex-col md:flex-row md:items-center md:justify-between">
                    <div className="flex-1">
                      <h3 className="text-xl font-semibold text-white mb-2">{edu.institution}</h3>
                      <p className="text-blue-400 mb-2">{edu.degree}</p>
                      <p className="text-gray-400">{edu.duration}</p>
                    </div>
                    <div className="mt-4 md:mt-0">
                      <Badge variant="secondary" className="bg-blue-600/20 text-blue-400">
                        {edu.grade}
                      </Badge>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section id="skills" className="py-20 bg-gray-800/50">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-16 text-blue-400">Technical Skills</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
            {skillCategories.map((category, index) => {
              const IconComponent = category.icon;
              return (
                <Card key={index} className="bg-gray-800 border-gray-700 hover:border-blue-500/50 transition-colors">
                  <CardHeader>
                    <CardTitle className="flex items-center space-x-3 text-white">
                      <IconComponent className="w-6 h-6 text-blue-400" />
                      <span>{category.name}</span>
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="flex flex-wrap gap-2">
                      {category.items.map((skill, skillIndex) => (
                        <Badge key={skillIndex} variant="secondary" className="bg-blue-600/20 text-blue-400">
                          {skill}
                        </Badge>
                      ))}
                    </div>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>
      </section>

      {/* Projects Section */}
      <section id="projects" className="py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-8 text-blue-400">Projects</h2>
          
          {/* Project Type Filter */}
          <div className="flex justify-center mb-12">
            <div className="flex flex-wrap gap-2">
              {projectTypes.map((type) => (
                <Button
                  key={type}
                  onClick={() => setSelectedType(type)}
                  variant={selectedType === type ? "default" : "outline"}
                  className={selectedType === type 
                    ? "bg-blue-600 hover:bg-blue-700" 
                    : "border-gray-600 text-gray-300 hover:bg-gray-800"
                  }
                >
                  {type}
                </Button>
              ))}
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto">
            {filteredProjects.map((project) => (
              <Card key={project.id} className="bg-gray-800 border-gray-700 hover:border-blue-500/50 transition-all duration-300 group">
                {project.image && (
                  <div className="aspect-video overflow-hidden">
                    <img 
                      src={project.image} 
                      alt={project.title}
                      className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                    />
                  </div>
                )}
                <CardContent className="p-6">
                  <div className="flex items-center justify-between mb-3">
                    <Badge variant="secondary" className="bg-blue-600/20 text-blue-400">
                      {project.type}
                    </Badge>
                    <span className="text-sm text-gray-400">{project.date}</span>
                  </div>
                  <h3 className="text-xl font-semibold text-white mb-3">{project.title}</h3>
                  <p className="text-gray-300 mb-4 leading-relaxed">{project.description}</p>
                  <div className="flex flex-wrap gap-2 mb-4">
                    {project.technologies.map((tech, index) => (
                      <Badge key={index} variant="outline" className="border-gray-600 text-gray-300">
                        {tech}
                      </Badge>
                    ))}
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Achievements Section */}
      <section id="achievements" className="py-20 bg-gray-800/50">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-16 text-blue-400">Achievements & Leadership</h2>
          <div className="max-w-4xl mx-auto space-y-6">
            {portfolioData.achievements.map((achievement, index) => (
              <Card key={index} className="bg-gray-800 border-gray-700 hover:border-blue-500/50 transition-colors">
                <CardContent className="p-6">
                  <div className="flex items-start space-x-4">
                    <Trophy className="w-6 h-6 text-yellow-500 mt-1 flex-shrink-0" />
                    <div className="flex-1">
                      <h3 className="text-xl font-semibold text-white mb-2">{achievement.title}</h3>
                      <p className="text-gray-300 mb-2">{achievement.description}</p>
                      <div className="flex items-center text-gray-400">
                        <Calendar className="w-4 h-4 mr-2" />
                        <span>{achievement.date}</span>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-16 text-blue-400">Contact Me</h2>
          <div className="max-w-4xl mx-auto">
            <Card className="bg-gray-800 border-gray-700">
              <CardContent className="p-8">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                  <div className="space-y-6">
                    <h3 className="text-2xl font-semibold text-white mb-6">Get In Touch</h3>
                    <div className="space-y-4">
                      <a href={`mailto:${portfolioData.profile.email}`} 
                         className="flex items-center space-x-3 text-gray-300 hover:text-blue-400 transition-colors">
                        <Mail className="w-5 h-5" />
                        <span>{portfolioData.profile.email}</span>
                      </a>
                      <a href={`tel:${portfolioData.profile.phone}`}
                         className="flex items-center space-x-3 text-gray-300 hover:text-blue-400 transition-colors">
                        <Phone className="w-5 h-5" />
                        <span>{portfolioData.profile.phone}</span>
                      </a>
                      <div className="flex items-center space-x-3 text-gray-300">
                        <MapPin className="w-5 h-5" />
                        <span>Delhi, India</span>
                      </div>
                    </div>
                  </div>
                  <div className="space-y-6">
                    <h3 className="text-2xl font-semibold text-white mb-6">Connect With Me</h3>
                    <div className="space-y-4">
                      <a href={portfolioData.profile.github} target="_blank" rel="noopener noreferrer"
                         className="flex items-center space-x-3 text-gray-300 hover:text-blue-400 transition-colors">
                        <Github className="w-5 h-5" />
                        <span>GitHub Profile</span>
                        <ExternalLink className="w-4 h-4" />
                      </a>
                      <a href={portfolioData.profile.linkedin} target="_blank" rel="noopener noreferrer"
                         className="flex items-center space-x-3 text-gray-300 hover:text-blue-400 transition-colors">
                        <Linkedin className="w-5 h-5" />
                        <span>LinkedIn Profile</span>
                        <ExternalLink className="w-4 h-4" />
                      </a>
                      <a href={portfolioData.profile.website} target="_blank" rel="noopener noreferrer"
                         className="flex items-center space-x-3 text-gray-300 hover:text-blue-400 transition-colors">
                        <ExternalLink className="w-5 h-5" />
                        <span>Vedic Math Project</span>
                        <ExternalLink className="w-4 h-4" />
                      </a>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 border-t border-gray-800 py-8">
        <div className="container mx-auto px-6 text-center">
          <p className="text-gray-400">
            © 2024 Tanishk Tiwari. Built with React & passion for technology.
          </p>
        </div>
      </footer>
    </div>
  );
};

export default Portfolio;