"""Unit tests for API client."""

import pytest
from unittest.mock import MagicMock, patch


def test_api_client_init(mock_module):
    """Test API client initialization."""
    from ansible_collections.stevefulme1.ddn.plugins.module_utils.api_client import ApiClient
    
    client = ApiClient(mock_module)
    assert client.host == "test.example.com"
    assert client.username == "admin"


def test_api_client_headers(mock_module):
    """Test header generation."""
    from ansible_collections.stevefulme1.ddn.plugins.module_utils.api_client import ApiClient
    
    client = ApiClient(mock_module)
    headers = client._get_headers()
    assert "Content-Type" in headers
    assert headers["Content-Type"] == "application/json"
