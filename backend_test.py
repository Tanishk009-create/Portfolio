#!/usr/bin/env python3
"""
Backend API Testing Script for Portfolio Application
Tests all portfolio API endpoints to ensure they are working correctly.
"""

import requests
import json
import sys
from typing import Dict, Any, List

# Get backend URL from frontend .env file
BACKEND_URL = "https://2dc09a96-0bc2-4cdf-a219-8b1d0c844756.preview.emergentagent.com/api"

class PortfolioAPITester:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.test_results = []
        
    def log_test(self, endpoint: str, success: bool, message: str, data: Any = None):
        """Log test results"""
        result = {
            "endpoint": endpoint,
            "success": success,
            "message": message,
            "data_sample": str(data)[:200] + "..." if data and len(str(data)) > 200 else data
        }
        self.test_results.append(result)
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {endpoint}: {message}")
        
    def test_endpoint(self, endpoint: str, expected_fields: List[str] = None, params: Dict = None) -> Dict[str, Any]:
        """Generic endpoint testing method"""
        try:
            url = f"{self.base_url}{endpoint}"
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code != 200:
                self.log_test(endpoint, False, f"HTTP {response.status_code}: {response.text}")
                return None
                
            data = response.json()
            
            # Check if response has success field
            if "success" not in data:
                self.log_test(endpoint, False, "Response missing 'success' field")
                return None
                
            if not data["success"]:
                self.log_test(endpoint, False, f"API returned success=false: {data.get('message', 'No message')}")
                return None
                
            # Check if response has data field
            if "data" not in data:
                self.log_test(endpoint, False, "Response missing 'data' field")
                return None
                
            response_data = data["data"]
            
            # Check for _id fields (should not be present)
            if self._has_id_fields(response_data):
                self.log_test(endpoint, False, "Response contains MongoDB _id fields")
                return None
                
            # Check expected fields if provided
            if expected_fields and response_data:
                if isinstance(response_data, list) and response_data:
                    sample_item = response_data[0]
                    missing_fields = [field for field in expected_fields if field not in sample_item]
                    if missing_fields:
                        self.log_test(endpoint, False, f"Missing expected fields: {missing_fields}")
                        return None
                elif isinstance(response_data, dict):
                    missing_fields = [field for field in expected_fields if field not in response_data]
                    if missing_fields:
                        self.log_test(endpoint, False, f"Missing expected fields: {missing_fields}")
                        return None
            
            self.log_test(endpoint, True, f"Successfully retrieved {len(response_data) if isinstance(response_data, list) else 'data'}", response_data)
            return response_data
            
        except requests.exceptions.RequestException as e:
            self.log_test(endpoint, False, f"Request failed: {str(e)}")
            return None
        except json.JSONDecodeError as e:
            self.log_test(endpoint, False, f"Invalid JSON response: {str(e)}")
            return None
        except Exception as e:
            self.log_test(endpoint, False, f"Unexpected error: {str(e)}")
            return None
    
    def _has_id_fields(self, data: Any) -> bool:
        """Check if data contains MongoDB _id fields"""
        if isinstance(data, dict):
            if "_id" in data:
                return True
            return any(self._has_id_fields(v) for v in data.values())
        elif isinstance(data, list):
            return any(self._has_id_fields(item) for item in data)
        return False
    
    def test_profile(self):
        """Test GET /api/profile endpoint"""
        print("\n🔍 Testing Profile Endpoint...")
        expected_fields = ["name", "title", "location", "phone", "email", "github", "linkedin", "website", "summary"]
        return self.test_endpoint("/profile", expected_fields)
    
    def test_education(self):
        """Test GET /api/education endpoint"""
        print("\n🔍 Testing Education Endpoint...")
        expected_fields = ["id", "institution", "degree", "duration", "grade", "order"]
        return self.test_endpoint("/education", expected_fields)
    
    def test_skills(self):
        """Test GET /api/skills endpoint"""
        print("\n🔍 Testing Skills Endpoint...")
        data = self.test_endpoint("/skills")
        
        # Additional validation for skills structure
        if data and isinstance(data, dict):
            # Check if skills are properly categorized
            categories = list(data.keys())
            if categories:
                self.log_test("/skills", True, f"Skills properly categorized into: {categories}")
                # Check if each category has items
                for category, items in data.items():
                    if not isinstance(items, list):
                        self.log_test("/skills", False, f"Category '{category}' should contain a list of items")
                        return None
            else:
                self.log_test("/skills", False, "No skill categories found")
                return None
        
        return data
    
    def test_projects(self):
        """Test GET /api/projects endpoint"""
        print("\n🔍 Testing Projects Endpoint...")
        expected_fields = ["id", "title", "date", "description", "technologies", "type", "order"]
        return self.test_endpoint("/projects", expected_fields)
    
    def test_projects_filtered(self):
        """Test GET /api/projects with project_type filter"""
        print("\n🔍 Testing Projects Filtering...")
        
        # First get all projects to see available types
        all_projects = self.test_endpoint("/projects")
        if not all_projects:
            return None
            
        # Get unique project types
        project_types = list(set(project.get("type", "") for project in all_projects if project.get("type")))
        
        if not project_types:
            self.log_test("/projects?project_type=filter", False, "No project types found to test filtering")
            return None
        
        # Test filtering with first available type
        test_type = project_types[0]
        filtered_projects = self.test_endpoint("/projects", params={"project_type": test_type})
        
        if filtered_projects:
            # Verify all returned projects match the filter
            mismatched = [p for p in filtered_projects if p.get("type") != test_type]
            if mismatched:
                self.log_test("/projects?project_type=filter", False, f"Filter failed: found {len(mismatched)} projects not matching type '{test_type}'")
                return None
            else:
                self.log_test("/projects?project_type=filter", True, f"Successfully filtered {len(filtered_projects)} projects of type '{test_type}'")
        
        return filtered_projects
    
    def test_achievements(self):
        """Test GET /api/achievements endpoint"""
        print("\n🔍 Testing Achievements Endpoint...")
        expected_fields = ["id", "title", "description", "date", "order"]
        return self.test_endpoint("/achievements", expected_fields)
    
    def test_creative_works(self):
        """Test GET /api/creative-works endpoint"""
        print("\n🔍 Testing Creative Works Endpoint...")
        expected_fields = ["id", "title", "type", "date", "preview", "fullContent"]
        return self.test_endpoint("/creative-works", expected_fields)
    
    def test_photography(self):
        """Test GET /api/photography endpoint"""
        print("\n🔍 Testing Photography Endpoint...")
        expected_fields = ["id", "title", "image", "description", "order"]
        return self.test_endpoint("/photography", expected_fields)
    
    def run_all_tests(self):
        """Run all API endpoint tests"""
        print(f"🚀 Starting Portfolio API Tests")
        print(f"📡 Backend URL: {self.base_url}")
        print("=" * 60)
        
        # Test all endpoints
        self.test_profile()
        self.test_education()
        self.test_skills()
        self.test_projects()
        self.test_projects_filtered()
        self.test_achievements()
        self.test_creative_works()
        self.test_photography()
        
        # Print summary
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for result in self.test_results if result["success"])
        total = len(self.test_results)
        
        print(f"✅ Passed: {passed}/{total}")
        print(f"❌ Failed: {total - passed}/{total}")
        
        if total - passed > 0:
            print("\n🔍 FAILED TESTS:")
            for result in self.test_results:
                if not result["success"]:
                    print(f"  • {result['endpoint']}: {result['message']}")
        
        print("\n" + "=" * 60)
        return passed == total

def main():
    """Main test execution"""
    tester = PortfolioAPITester(BACKEND_URL)
    success = tester.run_all_tests()
    
    if success:
        print("🎉 All tests passed!")
        sys.exit(0)
    else:
        print("💥 Some tests failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()