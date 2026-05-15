# -*- coding: utf-8 -*-
# Copyright 2026 Steve Fulmer
# Apache-2.0 (see LICENSE)

"""DDN Insight API client."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
from ansible.module_utils.urls import open_url
from ansible.module_utils.six.moves.urllib.error import HTTPError


class ApiClient:
    """Client for DDN Insight REST API."""

    def __init__(self, module):
        """Initialize API client from module params."""
        self.module = module
        self.host = module.params.get("host")
        self.username = module.params.get("username")
        self.password = module.params.get("password")
        self.api_key = module.params.get("api_key")
        self.validate_certs = module.params.get("validate_certs", True)
        self.base_url = f"https://{self.host}/api/v1"
        self.token = None

    def _get_headers(self):
        """Get request headers."""
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        elif self.api_key:
            headers["X-API-Key"] = self.api_key
        return headers

    def authenticate(self):
        """Authenticate and get token."""
        if self.api_key or self.token:
            return

        url = f"{self.base_url}/auth/login"
        data = json.dumps({"username": self.username, "password": self.password})

        try:
            response = open_url(
                url,
                method="POST",
                data=data,
                headers={"Content-Type": "application/json"},
                validate_certs=self.validate_certs,
            )
            result = json.loads(response.read())
            self.token = result.get("token")
        except HTTPError as e:
            self.module.fail_json(msg=f"Authentication failed: {str(e)}")

    def request(self, method, path, data=None):
        """Make API request."""
        self.authenticate()
        url = f"{self.base_url}{path}"

        try:
            response = open_url(
                url,
                method=method,
                data=json.dumps(data) if data else None,
                headers=self._get_headers(),
                validate_certs=self.validate_certs,
            )
            if response.getcode() == 204:
                return {}
            return json.loads(response.read())
        except HTTPError as e:
            self.module.fail_json(msg=f"API request failed: {str(e)}")

    def list(self, resource_type, params=None):
        """List resources."""
        return self.request("GET", f"/{resource_type}s")

    def get(self, resource_type, resource_id):
        """Get resource."""
        return self.request("GET", f"/{resource_type}s/{resource_id}")

    def create(self, resource_type, data):
        """Create resource."""
        return self.request("POST", f"/{resource_type}s", data=data)

    def update(self, resource_type, resource_id, data):
        """Update resource."""
        return self.request("PUT", f"/{resource_type}s/{resource_id}", data=data)

    def delete(self, resource_type, resource_id):
        """Delete resource."""
        return self.request("DELETE", f"/{resource_type}s/{resource_id}")
