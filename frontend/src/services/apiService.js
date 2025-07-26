const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API_BASE = `${BACKEND_URL}/api`;

class ApiService {
  static async request(endpoint, options = {}) {
    try {
      const response = await fetch(`${API_BASE}${endpoint}`, {
        headers: {
          'Content-Type': 'application/json',
          ...options.headers,
        },
        ...options,
      });

      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.message || 'API request failed');
      }

      return data;
    } catch (error) {
      console.error(`API Error for ${endpoint}:`, error);
      throw error;
    }
  }

  // Profile API
  static async getProfile() {
    const response = await this.request('/profile');
    return response.data;
  }

  static async updateProfile(profileData) {
    const response = await this.request('/profile', {
      method: 'PUT',
      body: JSON.stringify(profileData),
    });
    return response;
  }

  // Education API
  static async getEducation() {
    const response = await this.request('/education');
    return response.data;
  }

  // Skills API
  static async getSkills() {
    const response = await this.request('/skills');
    return response.data;
  }

  // Projects API
  static async getProjects(projectType = null) {
    const queryParam = projectType ? `?project_type=${projectType}` : '';
    const response = await this.request(`/projects${queryParam}`);
    return response.data;
  }

  // Achievements API
  static async getAchievements() {
    const response = await this.request('/achievements');
    return response.data;
  }

  // Creative Works API
  static async getCreativeWorks() {
    const response = await this.request('/creative-works');
    return response.data;
  }

  // Photography API
  static async getPhotography() {
    const response = await this.request('/photography');
    return response.data;
  }
}

export default ApiService;