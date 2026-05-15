"""Unit tests for ddn_filesystem module."""

from unittest.mock import MagicMock, patch


class TestCreate:
    def test_create_returns_resource(self):
        mock_client = MagicMock()
        mock_client.create.return_value = {"id": "123", "name": "test"}
        result = mock_client.create("filesystem", {"name": "test"})
        assert result["id"] == "123"
        mock_client.create.assert_called_once()


class TestDelete:
    def test_delete_calls_api(self):
        mock_client = MagicMock()
        mock_client.delete.return_value = None
        mock_client.delete("filesystem", "123")
        mock_client.delete.assert_called_once_with("filesystem", "123")


class TestList:
    def test_list_returns_items(self):
        mock_client = MagicMock()
        mock_client.list.return_value = [{"id": "1"}, {"id": "2"}]
        result = mock_client.list("filesystem")
        assert len(result) == 2


class TestGet:
    def test_get_returns_single(self):
        mock_client = MagicMock()
        mock_client.get.return_value = {"id": "123", "name": "test"}
        result = mock_client.get("filesystem", "123")
        assert result["name"] == "test"

    def test_get_not_found(self):
        mock_client = MagicMock()
        mock_client.get.return_value = None
        result = mock_client.get("filesystem", "nonexistent")
        assert result is None
