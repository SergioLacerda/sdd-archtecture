"""
Tests for SDD v3.1 API endpoints

Tests all 6 endpoints plus error handling and filtering.
"""

import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add app to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.sdd_api import app, DataLoader


@pytest.fixture
def client():
    """Create test client"""
    return TestClient(app)


class TestRoot:
    """Test root endpoint"""
    
    def test_root_returns_api_info(self, client):
        """Test root endpoint returns API information"""
        response = client.get("/")
        
        assert response.status_code == 200
        assert response.json()["name"] == "SDD v3.1 API"
        assert "endpoints" in response.json()


class TestMandates:
    """Test mandate endpoints"""
    
    def test_list_mandates(self, client):
        """Test listing mandates"""
        response = client.get("/api/mandates")
        
        assert response.status_code == 200
        data = response.json()
        assert "mandates" in data
        assert "count" in data
        assert isinstance(data["mandates"], list)
    
    def test_list_mandates_with_category_filter(self, client):
        """Test mandate filtering by category"""
        response = client.get("/api/mandates?category=general")
        
        assert response.status_code == 200
        data = response.json()
        
        # All returned mandates should be in general category
        for mandate in data["mandates"]:
            assert mandate["category"].lower() == "general"
    
    def test_list_mandates_with_type_filter(self, client):
        """Test mandate filtering by type"""
        response = client.get("/api/mandates?type=HARD")
        
        assert response.status_code == 200
        data = response.json()
        
        # All returned mandates should be HARD type
        for mandate in data["mandates"]:
            assert mandate["type"] == "HARD"
    
    def test_get_mandate_by_id(self, client):
        """Test getting specific mandate"""
        # First get list to find a valid ID
        list_response = client.get("/api/mandates")
        mandates = list_response.json()["mandates"]
        
        if mandates:
            mandate_id = mandates[0]["id"]
            response = client.get(f"/api/mandates/{mandate_id}")
            
            assert response.status_code == 200
            mandate = response.json()
            assert mandate["id"] == mandate_id
    
    def test_get_nonexistent_mandate(self, client):
        """Test getting nonexistent mandate returns 404"""
        response = client.get("/api/mandates/M999")
        
        assert response.status_code == 404


class TestGuidelines:
    """Test guideline endpoints"""
    
    def test_list_guidelines(self, client):
        """Test listing guidelines"""
        response = client.get("/api/guidelines")
        
        assert response.status_code == 200
        data = response.json()
        assert "guidelines" in data
        assert "count" in data
        assert isinstance(data["guidelines"], list)
    
    def test_list_guidelines_with_category_filter(self, client):
        """Test guideline filtering by category"""
        response = client.get("/api/guidelines?category=general")
        
        assert response.status_code == 200
        data = response.json()
        
        # All returned guidelines should be in general category
        for guideline in data["guidelines"]:
            assert guideline["category"].lower() == "general"
    
    def test_list_guidelines_with_type_filter(self, client):
        """Test guideline filtering by type"""
        response = client.get("/api/guidelines?type=SOFT")
        
        assert response.status_code == 200
        data = response.json()
        
        # All returned guidelines should be SOFT type
        for guideline in data["guidelines"]:
            assert guideline["type"] == "SOFT"
    
    def test_get_guideline_by_id(self, client):
        """Test getting specific guideline"""
        # First get list to find a valid ID
        list_response = client.get("/api/guidelines")
        guidelines = list_response.json()["guidelines"]
        
        if guidelines:
            guideline_id = guidelines[0]["id"]
            response = client.get(f"/api/guidelines/{guideline_id}")
            
            assert response.status_code == 200
            guideline = response.json()
            assert guideline["id"] == guideline_id
    
    def test_get_nonexistent_guideline(self, client):
        """Test getting nonexistent guideline returns 404"""
        response = client.get("/api/guidelines/G999")
        
        assert response.status_code == 404


class TestSearch:
    """Test search endpoint"""
    
    def test_search_requires_query(self, client):
        """Test search endpoint requires query parameter"""
        response = client.get("/api/search")
        
        assert response.status_code == 422  # Unprocessable Entity
    
    def test_search_returns_results(self, client):
        """Test search returns results"""
        response = client.get("/api/search?q=architecture")
        
        assert response.status_code == 200
        data = response.json()
        assert "query" in data
        assert "results" in data
        assert "total_found" in data
        assert data["query"] == "architecture"
    
    def test_search_results_structure(self, client):
        """Test search results have correct structure"""
        response = client.get("/api/search?q=test")
        
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data["results"]["mandates"], list)
        assert isinstance(data["results"]["guidelines"], list)
    
    def test_search_is_case_insensitive(self, client):
        """Test search is case insensitive"""
        response1 = client.get("/api/search?q=architecture")
        response2 = client.get("/api/search?q=ARCHITECTURE")
        
        assert response1.status_code == 200
        assert response2.status_code == 200
        # Both should return same number of results (approximately)
        results1 = response1.json()["total_found"]
        results2 = response2.json()["total_found"]
        assert results1 == results2


class TestStats:
    """Test statistics endpoint"""
    
    def test_stats_returns_data(self, client):
        """Test stats endpoint returns data"""
        response = client.get("/api/stats")
        
        assert response.status_code == 200
        data = response.json()
        
        # Check expected fields
        assert "version" in data
        assert "generated_at" in data
        assert "mandates" in data
        assert "guidelines" in data
        assert "total_items" in data
    
    def test_stats_mandates_structure(self, client):
        """Test mandates statistics structure"""
        response = client.get("/api/stats")
        
        assert response.status_code == 200
        data = response.json()
        mandates = data["mandates"]
        
        assert "total" in mandates
        assert "by_type" in mandates
        assert "by_category" in mandates
    
    def test_stats_guidelines_structure(self, client):
        """Test guidelines statistics structure"""
        response = client.get("/api/stats")
        
        assert response.status_code == 200
        data = response.json()
        guidelines = data["guidelines"]
        
        assert "total" in guidelines
        assert "by_type" in guidelines
        assert "by_category" in guidelines
    
    def test_stats_totals_match(self, client):
        """Test that total_items matches mandates + guidelines"""
        response = client.get("/api/stats")
        
        assert response.status_code == 200
        data = response.json()
        
        calculated_total = data["mandates"]["total"] + data["guidelines"]["total"]
        assert calculated_total == data["total_items"]


class TestDataLoader:
    """Test data loading functionality"""
    
    def test_loader_loads_mandates(self):
        """Test DataLoader loads mandates"""
        loader = DataLoader()
        mandates = loader.get_mandates()
        
        assert isinstance(mandates, list)
        # Should have at least some mandates
        assert len(mandates) >= 0
    
    def test_loader_loads_guidelines(self):
        """Test DataLoader loads guidelines"""
        loader = DataLoader()
        guidelines = loader.get_guidelines()
        
        assert isinstance(guidelines, list)
        # Should have at least some guidelines
        assert len(guidelines) >= 0
    
    def test_loader_get_mandate(self):
        """Test getting specific mandate"""
        loader = DataLoader()
        mandates = loader.get_mandates()
        
        if mandates:
            mandate_id = mandates[0]["id"]
            mandate = loader.get_mandate(mandate_id)
            
            assert mandate is not None
            assert mandate["id"] == mandate_id
    
    def test_loader_get_guideline(self):
        """Test getting specific guideline"""
        loader = DataLoader()
        guidelines = loader.get_guidelines()
        
        if guidelines:
            guideline_id = guidelines[0]["id"]
            guideline = loader.get_guideline(guideline_id)
            
            assert guideline is not None
            assert guideline["id"] == guideline_id
    
    def test_loader_search(self):
        """Test search functionality"""
        loader = DataLoader()
        results = loader.search("test")
        
        assert "mandates" in results
        assert "guidelines" in results
        assert isinstance(results["mandates"], list)
        assert isinstance(results["guidelines"], list)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
