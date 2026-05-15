#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Steve Fulmer
# Apache-2.0 (see LICENSE)

"""Ansible module: ddn_snapshot."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: ddn_snapshot
short_description: Manage DDN filesystem snapshots
description:
    - Manage DDN filesystem snapshots in Ddn.
    - Supports create, update, and delete operations.
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
options:
    state:
        description: Desired state of the resource.
        type: str
        default: present
        choices: [present, absent]
    snapshot_id:
        description: Unique identifier of the snapshot.
        type: str
    name:
        description: Display name of the snapshot.
        type: str
"""

EXAMPLES = r"""
- name: Create a snapshot
  stevefulme1.ddn.ddn_snapshot:
    name: my-snapshot
    state: present

- name: Delete a snapshot
  stevefulme1.ddn.ddn_snapshot:
    snapshot_id: "example-id"
    state: absent
"""

RETURN = r"""
snapshot:
    description: Resource details.
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
            snapshot_id=dict(type="str"),
            name=dict(type="str"),
            host=dict(type="str", required=True),
            username=dict(type="str"),
            password=dict(type="str", no_log=True),
            api_key=dict(type="str", no_log=True),
            validate_certs=dict(type="bool", default=True),
        ),
        supports_check_mode=True,
        required_if=[
            ("state", "absent", ("snapshot_id",)),
        ],
    )

    if not HAS_CLIENT:
        module.fail_json(msg="Required Python libraries not found.")

    client = ApiClient(module)
    state = module.params["state"]
    resource_id = module.params.get("snapshot_id")

    if state == "present":
        if resource_id:
            result = client.update("snapshot", resource_id, module.params)
        else:
            if module.check_mode:
                module.exit_json(changed=True)
            result = client.create("snapshot", module.params)
        module.exit_json(changed=True, snapshot=result)
    else:
        if module.check_mode:
            module.exit_json(changed=True)
        client.delete("snapshot", resource_id)
        module.exit_json(changed=True)


if __name__ == "__main__":
    main()
