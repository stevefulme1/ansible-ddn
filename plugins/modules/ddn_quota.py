#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Steve Fulmer
# Apache-2.0 (see LICENSE)
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module: ddn_quota."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: ddn_quota
short_description: Manage DDN filesystem quotas
description:
    - Manage user and group quotas on DDN filesystems.
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
options:
    state:
        description: Desired state of the resource.
        type: str
        default: present
        choices: [present, absent]
    host:
        description: API host address.
        type: str
        required: true
    username:
        description: Authentication username.
        type: str
    password:
        description: Authentication password.
        type: str
        no_log: true
    api_key:
        description: API key for authentication.
        type: str
        no_log: true
    validate_certs:
        description: Whether to validate SSL certificates.
        type: bool
        default: true
"""

EXAMPLES = r"""
- name: Set user quota
  stevefulme1.ddn.ddn_quota:
    host: insight.example.com
    username: admin
    password: "{{ vault_pass }}"
    filesystem: scratch
    name: jdoe
    soft_limit: 10TB
    hard_limit: 15TB
"""

RETURN = r"""
quota:
    description: Quota details.
    returned: on success
    type: dict
"""

from ansible.module_utils.basic import AnsibleModule

try:
    from ansible_collections.stevefulme1.ddn.plugins.module_utils.api_client import ApiClient
    HAS_CLIENT = True
except ImportError:
    HAS_CLIENT = False


def main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type="str", default="present", choices=["present", "absent"]),
            filesystem=dict(type="str", required=True),
            quota_type=dict(type="str", default="user", choices=["user", "group"]),
            name=dict(type="str", required=True),
            soft_limit=dict(type="str"),
            hard_limit=dict(type="str"),
            host=dict(type="str", required=True),
            username=dict(type="str"),
            password=dict(type="str", no_log=True),
            api_key=dict(type="str", no_log=True),
            validate_certs=dict(type="bool", default=True),
        ),
        supports_check_mode=True,
    )

    if not HAS_CLIENT:
        module.fail_json(msg="Required Python libraries not found.")

    client = ApiClient(module)
    state = module.params["state"]
    
    if state == "present":
        result = client.create("quota", module.params)
        module.exit_json(changed=True, quota=result)
    else:
        client.delete("quota", module.params["name"])
        module.exit_json(changed=True)


if __name__ == "__main__":
    main()
