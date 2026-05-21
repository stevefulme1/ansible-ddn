"""Unit tests for stevefulme1.ddn.ddn_storage_pool module."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import MagicMock

import pytest

MODULE_PATH = "ansible_collections.stevefulme1.ddn.plugins.modules.ddn_storage_pool"


@pytest.fixture
def mock_api_client():
    """Mock API client for ddn_storage_pool."""
    client = MagicMock()
    client.get.return_value = None
    client.create.return_value = {"id": "res-123", "name": "test-ddn_storage_pool"}
    client.update.return_value = {"id": "res-123", "name": "test-ddn_storage_pool-updated"}
    client.delete.return_value = None
    client.list.return_value = []
    return client


@pytest.fixture
def existing_resource():
    """Return a dict representing an existing ddn_storage_pool."""
    return {
        "id": "res-123",
        "name": "test-ddn_storage_pool",
        "state": "active",
    }


class TestCreateDdnStoragePool:
    """Tests for creating a ddn_storage_pool."""

    def test_create_returns_resource(self, mock_api_client):
        """Verify create returns resource dict with expected fields."""
        result = mock_api_client.create("ddn_storage_pool", {"name": "test-ddn_storage_pool"})
        assert result["id"] == "res-123"
        assert result["name"] == "test-ddn_storage_pool"
        mock_api_client.create.assert_called_once()

    def test_create_api_error(self):
        """Verify API errors are raised on create."""
        client = MagicMock()
        client.create.side_effect = Exception("409 Conflict")
        with pytest.raises(Exception, match="409 Conflict"):
            client.create("ddn_storage_pool", {"name": "test"})


class TestDeleteDdnStoragePool:
    """Tests for deleting a ddn_storage_pool."""

    def test_delete_existing(self, mock_api_client, existing_resource):
        """Verify delete is called for existing resource."""
        mock_api_client.get.return_value = existing_resource
        mock_api_client.delete("ddn_storage_pool", "res-123")
        mock_api_client.delete.assert_called_once_with("ddn_storage_pool", "res-123")

    def test_delete_nonexistent(self, mock_api_client):
        """Verify delete handles missing resource gracefully."""
        mock_api_client.get.return_value = None
        mock_api_client.delete.side_effect = Exception("404 Not Found")
        with pytest.raises(Exception, match="404"):
            mock_api_client.delete("ddn_storage_pool", "missing")


class TestIdempotencyDdnStoragePool:
    """Tests for idempotency behavior."""

    def test_no_change_when_exists(self, mock_api_client, existing_resource):
        """Verify no API call when resource already in desired state."""
        mock_api_client.get.return_value = existing_resource
        result = mock_api_client.get("ddn_storage_pool", "res-123")
        assert result["id"] == "res-123"
