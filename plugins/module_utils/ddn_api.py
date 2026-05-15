#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, Steven Fulmer <sfulmer@redhat.com>
# Apache-2.0 License

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
from ansible.module_utils.urls import open_url
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError


class DDNAPIClient:
    """Client for DDN Insight REST API interactions."""

    def __init__(self, host, port=443, username=None, password=None, validate_certs=True, timeout=30):
        """
        Initialize DDN API client.

        Args:
            host: DDN Insight API hostname or IP
            port: API port (default: 443)
            username: API username
            password: API password
            validate_certs: Validate SSL certificates (default: True)
            timeout: Request timeout in seconds (default: 30)
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.validate_certs = validate_certs
        self.timeout = timeout
        self.base_url = f"https://{host}:{port}/api/v1"
        self.token = None

    def _get_headers(self):
        """Get request headers with authentication."""
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'
        return headers

    def authenticate(self):
        """
        Authenticate with DDN Insight API and obtain token.

        Returns:
            bool: True if authentication successful

        Raises:
            Exception: On authentication failure
        """
        url = f"{self.base_url}/auth/login"
        data = {
            'username': self.username,
            'password': self.password
        }

        try:
            response = open_url(
                url,
                method='POST',
                data=json.dumps(data),
                headers={'Content-Type': 'application/json'},
                validate_certs=self.validate_certs,
                timeout=self.timeout
            )
            result = json.loads(response.read())
            self.token = result.get('token')
            return True
        except HTTPError as e:
            error_msg = e.read().decode('utf-8') if hasattr(e, 'read') else str(e)
            raise Exception(f"Authentication failed: {error_msg}")
        except URLError as e:
            raise Exception(f"Connection failed: {str(e)}")

    def request(self, method, endpoint, data=None, params=None):
        """
        Make authenticated API request.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint path (e.g., '/filesystems')
            data: Request body data (for POST/PUT)
            params: URL query parameters

        Returns:
            dict: API response data

        Raises:
            Exception: On request failure
        """
        if not self.token:
            self.authenticate()

        url = f"{self.base_url}{endpoint}"

        if params:
            query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
            url = f"{url}?{query_string}"

        headers = self._get_headers()
        request_data = json.dumps(data) if data else None

        try:
            response = open_url(
                url,
                method=method,
                data=request_data,
                headers=headers,
                validate_certs=self.validate_certs,
                timeout=self.timeout
            )

            if response.getcode() == 204:
                return {}

            return json.loads(response.read())

        except HTTPError as e:
            error_msg = e.read().decode('utf-8') if hasattr(e, 'read') else str(e)
            raise Exception(f"API request failed: {method} {endpoint} - {error_msg}")
        except URLError as e:
            raise Exception(f"Connection failed: {str(e)}")

    def get(self, endpoint, params=None):
        """GET request."""
        return self.request('GET', endpoint, params=params)

    def post(self, endpoint, data=None):
        """POST request."""
        return self.request('POST', endpoint, data=data)

    def put(self, endpoint, data=None):
        """PUT request."""
        return self.request('PUT', endpoint, data=data)

    def delete(self, endpoint):
        """DELETE request."""
        return self.request('DELETE', endpoint)

    # Filesystem operations
    def get_filesystems(self):
        """Get all filesystems."""
        return self.get('/filesystems')

    def get_filesystem(self, name):
        """Get specific filesystem."""
        return self.get(f'/filesystems/{name}')

    def create_filesystem(self, data):
        """Create filesystem."""
        return self.post('/filesystems', data=data)

    def update_filesystem(self, name, data):
        """Update filesystem."""
        return self.put(f'/filesystems/{name}', data=data)

    def delete_filesystem(self, name):
        """Delete filesystem."""
        return self.delete(f'/filesystems/{name}')

    # Storage pool operations
    def get_storage_pools(self):
        """Get all storage pools."""
        return self.get('/storage-pools')

    def get_storage_pool(self, name):
        """Get specific storage pool."""
        return self.get(f'/storage-pools/{name}')

    def create_storage_pool(self, data):
        """Create storage pool."""
        return self.post('/storage-pools', data=data)

    def update_storage_pool(self, name, data):
        """Update storage pool."""
        return self.put(f'/storage-pools/{name}', data=data)

    def delete_storage_pool(self, name):
        """Delete storage pool."""
        return self.delete(f'/storage-pools/{name}')

    # Quota operations
    def get_quotas(self, filesystem):
        """Get quotas for filesystem."""
        return self.get(f'/filesystems/{filesystem}/quotas')

    def get_quota(self, filesystem, quota_type, name):
        """Get specific quota."""
        return self.get(f'/filesystems/{filesystem}/quotas/{quota_type}/{name}')

    def set_quota(self, filesystem, quota_type, name, data):
        """Set quota."""
        return self.put(f'/filesystems/{filesystem}/quotas/{quota_type}/{name}', data=data)

    def delete_quota(self, filesystem, quota_type, name):
        """Delete quota."""
        return self.delete(f'/filesystems/{filesystem}/quotas/{quota_type}/{name}')

    # Snapshot operations
    def get_snapshots(self, filesystem):
        """Get snapshots for filesystem."""
        return self.get(f'/filesystems/{filesystem}/snapshots')

    def get_snapshot(self, filesystem, name):
        """Get specific snapshot."""
        return self.get(f'/filesystems/{filesystem}/snapshots/{name}')

    def create_snapshot(self, filesystem, data):
        """Create snapshot."""
        return self.post(f'/filesystems/{filesystem}/snapshots', data=data)

    def delete_snapshot(self, filesystem, name):
        """Delete snapshot."""
        return self.delete(f'/filesystems/{filesystem}/snapshots/{name}')

    # Health check operations
    def run_health_check(self, data=None):
        """Execute health check."""
        return self.post('/health/check', data=data or {})

    def get_health_status(self):
        """Get current health status."""
        return self.get('/health/status')

    # Cluster operations
    def get_cluster_info(self):
        """Get cluster topology and configuration."""
        return self.get('/cluster/info')
