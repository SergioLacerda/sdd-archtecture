"""
RTK (Runtime Telemetry Kit) - Deduplication Module

Version: 3.1.0-dev
Status: Under Development (Phase 8)

Provides intelligent pattern-based deduplication for telemetry events with
60-70% overhead reduction and O(1) pattern matching performance.

Example:
    >>> from sdd_rtk import deduplicate_event
    >>> 
    >>> event = {
    ...     "timestamp": "2026-04-21T14:30:00Z",
    ...     "service": "sdd-api",
    ...     "status": 200
    ... }
    >>> 
    >>> compressed = deduplicate_event(event)
    >>> print(compressed)
    {'timestamp': '$TS001', 'service': '$SRV01', 'status': '$ST001'}
"""

from .engine import (
    DeduplicationEngine,
    PatternRegistry,
    CompressionMetrics,
    deduplicate_event,
    get_engine,
    get_compression_metrics,
    reset_metrics,
)

__version__ = "3.1.0-dev"
__author__ = "SDD Development Team"
__all__ = [
    "DeduplicationEngine",
    "PatternRegistry",
    "CompressionMetrics",
    "deduplicate_event",
    "get_engine",
    "get_compression_metrics",
    "reset_metrics",
]
