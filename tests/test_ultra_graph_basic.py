"""Tests for ultra-graph-basic."""

import pytest
from ultra_graph_basic import basic


class TestBasic:
    """Test suite for basic."""

    def test_basic(self):
        """Test basic usage."""
        result = basic("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            basic("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = basic(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
