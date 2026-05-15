#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, Steven Fulmer <sfulmer@redhat.com>
# Apache-2.0 License

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment:
    """Documentation fragment for DDN authentication options."""

    DOCUMENTATION = r'''
options:
    host:
        description:
            - DDN Insight API hostname or IP address.
        type: str
        required: true
    port:
        description:
            - DDN Insight API port.
        type: int
        default: 443
    username:
        description:
            - Username for DDN Insight API authentication.
        type: str
        required: true
    password:
        description:
            - Password for DDN Insight API authentication.
        type: str
        required: true
        no_log: true
    validate_certs:
        description:
            - Whether to validate SSL certificates.
            - Set to C(false) only in development/testing environments.
        type: bool
        default: true
    timeout:
        description:
            - API request timeout in seconds.
        type: int
        default: 30
notes:
    - Requires network connectivity to DDN Insight API endpoint.
    - Use Ansible Vault to protect sensitive credentials.
    - API credentials require appropriate permissions for operations.
'''
