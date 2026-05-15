"""Pytest configuration for unit tests."""

import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_module():
    """Mock Ansible module."""
    module = MagicMock()
    module.params = {
        "host": "test.example.com",
        "username": "admin",
        "password": "password",
        "validate_certs": True,
    }
    module.check_mode = False
    return module


@pytest.fixture
def mock_api_client(mocker):
    """Mock API client."""
    client = mocker.patch("ansible_collections.stevefulme1.ddn.plugins.module_utils.api_client.ApiClient")
    client.return_value.list.return_value = []
    client.return_value.get.return_value = {}
    client.return_value.create.return_value = {}
    client.return_value.update.return_value = {}
    client.return_value.delete.return_value = {}
    return client
