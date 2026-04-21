# SDD v3.1 API - FastAPI Backend

REST API for SDD v3.0 mandates and guidelines with search, filtering, and statistics.

**Status:** ✅ Phase 8 Workstream 3 (Week 2-3)

## Overview

The SDD API provides 6 RESTful endpoints for accessing SDD v3.0 content:

- **Mandates API**: List, filter, and retrieve mandates
- **Guidelines API**: List, filter, and retrieve guidelines
- **Search API**: Full-text search across all content
- **Statistics API**: Aggregated metrics and breakdown

## Quick Start

### Installation

```bash
# Install dependencies
pip install fastapi uvicorn

# Or use requirements.txt
pip install -r requirements.txt
```

### Running the Server

```bash
# Development server (auto-reload)
uvicorn .sdd-api.app.sdd_api:app --reload --host 0.0.0.0 --port 8000

# Production server
uvicorn .sdd-api.app.sdd_api:app --host 0.0.0.0 --port 8000 --workers 4
```

### Interactive Documentation

Once running, access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## API Endpoints

### 1. List Mandates

```
GET /api/mandates
```

Query Parameters:
- `category` (optional): Filter by category (e.g., `general`, `architecture`)
- `type` (optional): Filter by type (`HARD` or `SOFT`)

Response:
```json
{
  "mandates": [
    {
      "id": "M001",
      "type": "HARD",
      "title": "Clean Architecture",
      "description": "...",
      "category": "architecture",
      "rationale": "...",
      "validation_commands": ["pytest", "mypy"]
    }
  ],
  "count": 2
}
```

### 2. Get Mandate by ID

```
GET /api/mandates/{mandate_id}
```

Example: `GET /api/mandates/M001`

Response:
```json
{
  "id": "M001",
  "type": "HARD",
  "title": "Clean Architecture",
  "description": "...",
  "category": "architecture"
}
```

### 3. List Guidelines

```
GET /api/guidelines
```

Query Parameters:
- `category` (optional): Filter by category
- `type` (optional): Filter by type

Response:
```json
{
  "guidelines": [
    {
      "id": "G01",
      "type": "SOFT",
      "title": "Use Type Hints",
      "description": "...",
      "category": "general",
      "examples": ["Example 1", "Example 2"]
    }
  ],
  "count": 150
}
```

### 4. Get Guideline by ID

```
GET /api/guidelines/{guideline_id}
```

Example: `GET /api/guidelines/G01`

### 5. Full-Text Search

```
GET /api/search?q={query}
```

Query Parameters:
- `q` (required): Search query

Response:
```json
{
  "query": "architecture",
  "results": {
    "mandates": [...],
    "guidelines": [...]
  },
  "total_found": 15
}
```

### 6. Statistics

```
GET /api/stats
```

Response:
```json
{
  "version": "3.1.0-dev",
  "generated_at": "2026-04-22T10:30:00Z",
  "mandates": {
    "total": 2,
    "by_type": {
      "HARD": 2,
      "SOFT": 0
    },
    "by_category": {
      "architecture": 1,
      "general": 1
    }
  },
  "guidelines": {
    "total": 150,
    "by_type": {
      "HARD": 0,
      "SOFT": 150
    },
    "by_category": {
      "general": 119,
      "git": 18,
      "documentation": 5,
      "testing": 4,
      "naming": 2,
      "code-style": 1,
      "performance": 1
    }
  },
  "total_items": 152
}
```

## Examples

### Get all mandates
```bash
curl http://localhost:8000/api/mandates
```

### Filter mandates by category
```bash
curl http://localhost:8000/api/mandates?category=architecture
```

### Filter mandates by type
```bash
curl http://localhost:8000/api/mandates?type=HARD
```

### Get specific mandate
```bash
curl http://localhost:8000/api/mandates/M001
```

### Get all guidelines
```bash
curl http://localhost:8000/api/guidelines
```

### Search for content
```bash
curl http://localhost:8000/api/search?q=architecture
```

### Get statistics
```bash
curl http://localhost:8000/api/stats
```

## Architecture

### Components

```
.sdd-api/
├── __init__.py                 # Module init
├── README.md                   # This file
├── app/
│   ├── __init__.py
│   └── sdd_api.py              # Main FastAPI app (600+ lines)
└── tests/
    ├── __init__.py
    └── test_api.py             # Test suite (400+ lines)
```

### Data Loading

The `DataLoader` class:
1. Reads `.sdd-core/CANONICAL/mandate.spec`
2. Reads `.sdd-guidelines/guidelines.dsl`
3. Parses DSL format using regex
4. Maintains in-memory dictionaries
5. Provides search and filtering

### Performance Targets

- **Response Time**: <100ms per endpoint
- **Concurrent Users**: 100+
- **Data Loading**: <1s startup
- **Search**: O(n) over n items

## Testing

Run test suite:

```bash
# All tests
pytest .sdd-api/tests/

# With coverage
pytest .sdd-api/tests/ --cov=.sdd-api.app

# Specific test
pytest .sdd-api/tests/test_api.py::TestMandates::test_list_mandates
```

### Test Coverage

- **TestRoot** (1 test): Root endpoint
- **TestMandates** (5 tests): Mandate endpoints + filtering
- **TestGuidelines** (5 tests): Guideline endpoints + filtering
- **TestSearch** (4 tests): Search functionality
- **TestStats** (4 tests): Statistics endpoint
- **TestDataLoader** (5 tests): Data loading functionality

**Target:** >85% code coverage

## Integration

### Phase 8 Dependencies

1. **DSL Compiler** (Phase 8.2): Pre-compiles DSL for faster loading
2. **Web Dashboard** (Phase 8.3): Consumes these endpoints
3. **RTK Telemetry** (Phase 8.1): Logs API metrics
4. **Extension Framework** (Phase 8.4): Extends with custom endpoints

### Future Features (Week 3+)

- [ ] Caching layer (Redis)
- [ ] Rate limiting
- [ ] Authentication/Authorization
- [ ] Compiled binary endpoint (MessagePack)
- [ ] Export to PDF/JSON/CSV
- [ ] Pagination
- [ ] Sorting options

## CORS Configuration

The API includes CORS middleware that allows:
- All origins: `*`
- All methods: `GET, POST, PUT, DELETE, OPTIONS`
- All headers: `*`

For production, restrict to specific origins:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://dashboard.example.com"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
```

## Error Handling

All endpoints return appropriate HTTP status codes:

- `200 OK`: Successful request
- `404 Not Found`: Item not found (mandate/guideline)
- `422 Unprocessable Entity`: Invalid query parameters
- `500 Internal Server Error`: Server error

Example error response:

```json
{
  "detail": "Mandate M999 not found"
}
```

## Environment Variables

None required for basic operation. Can be configured:

```bash
# Data directory (default: .sdd-core/CANONICAL)
export SDD_DATA_DIR=/path/to/data

# Port (default: 8000)
export SDD_API_PORT=8000

# Host (default: 0.0.0.0)
export SDD_API_HOST=127.0.0.1
```

## Dependencies

- `fastapi>=0.95.0`: Web framework
- `uvicorn>=0.21.0`: ASGI server
- `pytest>=7.0`: Testing framework
- `httpx`: Test client (included with FastAPI)

## File Structure

```
.sdd-api/
├── app/
│   └── sdd_api.py              # 600+ lines
│       - FastAPI app definition
│       - DataLoader class
│       - 6 endpoint handlers
│       - CORS configuration
│       - Error handling
├── tests/
│   └── test_api.py             # 400+ lines
│       - 24 test cases
│       - Endpoint testing
│       - Filtering tests
│       - Error handling tests
│       - Data loader tests
└── README.md                   # This file
```

## Next Steps (Phase 8 Week 3)

1. **Test on Real Data** ✅ (This week)
   - Run full test suite
   - Verify response times <100ms
   - Load test with 100+ concurrent users

2. **Dashboard Integration** (Next)
   - Create React/Vue frontend
   - Consume all 6 endpoints
   - Implement search UI

3. **Caching** (Optional)
   - Add Redis layer
   - Cache search results
   - Cache statistics

4. **Binary Endpoint** (Phase 8 Week 4)
   - Add compiled MessagePack format
   - Reduce bandwidth 65%

## References

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **SDD v3.0**: [Migration Guide](../.sdd-migration/MIGRATION_v2_to_v3.md)
- **Phase 8 Planning**: [../.sdd-migration/PHASE_8_PLANNING.md](../.sdd-migration/PHASE_8_PLANNING.md)
- **DSL Compiler**: [../.sdd-compiler/README.md](../.sdd-compiler/README.md)

## Author

SDD Development Team - Phase 8 Workstream 3 (Web API)

**Timeline:** Week 2-3 of Phase 8 (April 22 - May 6, 2026)

## License

Part of SDD v3.1 Release
