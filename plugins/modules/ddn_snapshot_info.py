#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Steve Fulmer
# Apache-2.0 (see LICENSE)

"""Ansible module: ddn_snapshot_info."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: ddn_snapshot_info
short_description: snapshot_info_DESC
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
"""

EXAMPLES = r"""
- name: Example
  stevefulme1.ddn.ddn_snapshot_info:
    host: insight.example.com
    username: admin
    password: "{{ vault_pass }}"
"""

RETURN = r"""
result:
    description: Operation result.
    returned: always
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
    result = client.list("snapshot_info_RESOURCE", module.params)
    module.exit_json(changed=False, result=result)


if __name__ == "__main__":
    main()
