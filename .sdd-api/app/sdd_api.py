"""
FastAPI Backend for SDD v3.1 Web Dashboard

Provides REST API endpoints for accessing SDD v3.0 mandates and guidelines
with full-text search, filtering, and statistics.

Endpoints:
- GET /api/mandates           - List all mandates
- GET /api/mandates/{id}      - Get mandate details
- GET /api/guidelines         - List all guidelines  
- GET /api/guidelines/{id}    - Get guideline details
- GET /api/search             - Full-text search
- GET /api/stats              - Statistics and metrics
"""

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Dict, Any
import json
import re
from pathlib import Path
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Mandate:
    """Mandate data model"""
    id: str
    type: str
    title: str
    description: str
    category: str
    rationale: Optional[str] = None
    validation_commands: Optional[List[str]] = None


@dataclass
class Guideline:
    """Guideline data model"""
    id: str
    type: str
    title: str
    category: str
    description: Optional[str] = None
    examples: Optional[List[str]] = None


class DataLoader:
    """Loads mandate and guideline data from DSL files"""
    
    def __init__(self, data_dir: str = ".sdd-core/CANONICAL"):
        self.data_dir = Path(data_dir)
        self.mandates: List[Dict[str, Any]] = []
        self.guidelines: List[Dict[str, Any]] = []
        self._load_data()
    
    def _load_data(self):
        """Load mandates and guidelines from files"""
        self._load_mandates()
        self._load_guidelines()
    
    def _load_mandates(self):
        """Load mandates from mandate.spec"""
        mandate_file = self.data_dir / "mandate.spec"
        
        if not mandate_file.exists():
            # Fallback: try from .sdd-guidelines
            mandate_file = Path(".sdd-guidelines/mandate.spec")
        
        if not mandate_file.exists():
            # Fallback: use empty list for testing
            self.mandates = []
            return
        
        try:
            with open(mandate_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse mandate blocks using regex
            pattern = r'mandate\s+(M\d+)\s*\{([^}]+)\}'
            for match in re.finditer(pattern, content, re.DOTALL):
                mandate_id = match.group(1)
                body = match.group(2)
                
                mandate = {
                    "id": mandate_id,
                    "type": self._extract_field(body, "type", "HARD"),
                    "title": self._extract_field(body, "title", ""),
                    "description": self._extract_field(body, "description", ""),
                    "category": self._extract_field(body, "category", "general"),
                    "rationale": self._extract_field(body, "rationale"),
                }
                self.mandates.append(mandate)
        except Exception as e:
            print(f"Error loading mandates: {e}")
            self.mandates = []
    
    def _load_guidelines(self):
        """Load guidelines from guidelines.dsl"""
        guidelines_file = Path(".sdd-guidelines/guidelines.dsl")
        
        if not guidelines_file.exists():
            self.guidelines = []
            return
        
        try:
            with open(guidelines_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse guideline blocks using regex
            pattern = r'guideline\s+(G\d+)\s*\{([^}]+)\}'
            for match in re.finditer(pattern, content, re.DOTALL):
                guideline_id = match.group(1)
                body = match.group(2)
                
                guideline = {
                    "id": guideline_id,
                    "type": self._extract_field(body, "type", "SOFT"),
                    "title": self._extract_field(body, "title", ""),
                    "description": self._extract_field(body, "description"),
                    "category": self._extract_field(body, "category", "general"),
                }
                self.guidelines.append(guideline)
        except Exception as e:
            print(f"Error loading guidelines: {e}")
            self.guidelines = []
    
    @staticmethod
    def _extract_field(text: str, field_name: str, default: Optional[str] = None) -> Optional[str]:
        """Extract field value from DSL block"""
        # Try quoted value first
        pattern = f'{field_name}\\s*:\\s*"([^"]*)(?:"|$)'
        match = re.search(pattern, text, re.DOTALL)
        if match:
            value = match.group(1).strip()
            return value if value else default
        
        # Try unquoted value
        pattern = f'{field_name}\\s*:\\s*([^,}}\\n]*?)(?=,|}}|\\n)'
        match = re.search(pattern, text)
        if match:
            value = match.group(1).strip()
            return value if value else default
        
        return default
    
    def get_mandates(self) -> List[Dict[str, Any]]:
        """Get all mandates"""
        return self.mandates
    
    def get_mandate(self, mandate_id: str) -> Optional[Dict[str, Any]]:
        """Get mandate by ID"""
        for mandate in self.mandates:
            if mandate["id"] == mandate_id:
                return mandate
        return None
    
    def get_guidelines(self) -> List[Dict[str, Any]]:
        """Get all guidelines"""
        return self.guidelines
    
    def get_guideline(self, guideline_id: str) -> Optional[Dict[str, Any]]:
        """Get guideline by ID"""
        for guideline in self.guidelines:
            if guideline["id"] == guideline_id:
                return guideline
        return None
    
    def search(self, query: str) -> Dict[str, List[Dict[str, Any]]]:
        """Search mandates and guidelines by query"""
        query_lower = query.lower()
        
        results = {
            "mandates": [],
            "guidelines": []
        }
        
        # Search mandates
        for mandate in self.mandates:
            title = mandate.get("title", "") or ""
            description = mandate.get("description", "") or ""
            category = mandate.get("category", "") or ""
            
            if (query_lower in title.lower() or
                query_lower in description.lower() or
                query_lower in category.lower()):
                results["mandates"].append(mandate)
        
        # Search guidelines
        for guideline in self.guidelines:
            title = guideline.get("title", "") or ""
            description = guideline.get("description", "") or ""
            category = guideline.get("category", "") or ""
            
            if (query_lower in title.lower() or
                query_lower in description.lower() or
                query_lower in category.lower()):
                results["guidelines"].append(guideline)
        
        return results


# Create FastAPI app
app = FastAPI(
    title="SDD v3.1 API",
    description="REST API for SDD v3.0 mandates and guidelines",
    version="3.1.0-dev"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize data loader
loader = DataLoader()


@app.get("/api/mandates", tags=["Mandates"])
async def list_mandates(
    category: Optional[str] = Query(None, description="Filter by category"),
    type_filter: Optional[str] = Query(None, alias="type", description="Filter by type (HARD/SOFT)")
):
    """Get all mandates with optional filtering"""
    mandates = loader.get_mandates()
    
    # Apply filters
    if category:
        mandates = [m for m in mandates if m["category"].lower() == category.lower()]
    
    if type_filter:
        mandates = [m for m in mandates if m["type"].lower() == type_filter.lower()]
    
    return {
        "mandates": mandates,
        "count": len(mandates)
    }


@app.get("/api/mandates/{mandate_id}", tags=["Mandates"])
async def get_mandate(mandate_id: str):
    """Get mandate by ID"""
    mandate = loader.get_mandate(mandate_id)
    
    if mandate is None:
        raise HTTPException(status_code=404, detail=f"Mandate {mandate_id} not found")
    
    return mandate


@app.get("/api/guidelines", tags=["Guidelines"])
async def list_guidelines(
    category: Optional[str] = Query(None, description="Filter by category"),
    type_filter: Optional[str] = Query(None, alias="type", description="Filter by type (HARD/SOFT)")
):
    """Get all guidelines with optional filtering"""
    guidelines = loader.get_guidelines()
    
    # Apply filters
    if category:
        guidelines = [g for g in guidelines if g["category"].lower() == category.lower()]
    
    if type_filter:
        guidelines = [g for g in guidelines if g["type"].lower() == type_filter.lower()]
    
    return {
        "guidelines": guidelines,
        "count": len(guidelines)
    }


@app.get("/api/guidelines/{guideline_id}", tags=["Guidelines"])
async def get_guideline(guideline_id: str):
    """Get guideline by ID"""
    guideline = loader.get_guideline(guideline_id)
    
    if guideline is None:
        raise HTTPException(status_code=404, detail=f"Guideline {guideline_id} not found")
    
    return guideline


@app.get("/api/search", tags=["Search"])
async def search(q: str = Query(..., description="Search query", min_length=1)):
    """Full-text search across mandates and guidelines"""
    results = loader.search(q)
    
    return {
        "query": q,
        "results": results,
        "total_found": len(results["mandates"]) + len(results["guidelines"])
    }


@app.get("/api/stats", tags=["Statistics"])
async def get_stats():
    """Get statistics and metrics"""
    mandates = loader.get_mandates()
    guidelines = loader.get_guidelines()
    
    # Calculate category breakdown
    mandate_categories = {}
    for m in mandates:
        cat = m.get("category", "general")
        mandate_categories[cat] = mandate_categories.get(cat, 0) + 1
    
    guideline_categories = {}
    for g in guidelines:
        cat = g.get("category", "general")
        guideline_categories[cat] = guideline_categories.get(cat, 0) + 1
    
    return {
        "version": "3.1.0-dev",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "mandates": {
            "total": len(mandates),
            "by_type": {
                "HARD": len([m for m in mandates if m.get("type") == "HARD"]),
                "SOFT": len([m for m in mandates if m.get("type") == "SOFT"]),
            },
            "by_category": mandate_categories
        },
        "guidelines": {
            "total": len(guidelines),
            "by_type": {
                "HARD": len([g for g in guidelines if g.get("type") == "HARD"]),
                "SOFT": len([g for g in guidelines if g.get("type") == "SOFT"]),
            },
            "by_category": guideline_categories
        },
        "total_items": len(mandates) + len(guidelines)
    }


@app.get("/", tags=["Root"])
async def root():
    """API root - returns API information"""
    return {
        "name": "SDD v3.1 API",
        "version": "3.1.0-dev",
        "description": "REST API for SDD v3.0 mandates and guidelines",
        "endpoints": {
            "mandates": "/api/mandates",
            "mandate_detail": "/api/mandates/{id}",
            "guidelines": "/api/guidelines",
            "guideline_detail": "/api/guidelines/{id}",
            "search": "/api/search?q=query",
            "stats": "/api/stats",
            "docs": "/docs",
            "openapi": "/openapi.json"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
