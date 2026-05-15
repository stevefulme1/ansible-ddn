#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Steve Fulmer
# Apache-2.0 (see LICENSE)

"""Ansible module: ddn_cluster."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: ddn_cluster
short_description: DDN cluster information
description:
    - DDN cluster information in Ddn.
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
    cluster_id:
        description: Unique identifier of the cluster.
        type: str
    name:
        description: Display name of the cluster.
        type: str
"""

EXAMPLES = r"""
- name: Create a cluster
  stevefulme1.ddn.ddn_cluster:
    name: my-cluster
    state: present

- name: Delete a cluster
  stevefulme1.ddn.ddn_cluster:
    cluster_id: "example-id"
    state: absent
"""

RETURN = r"""
cluster:
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
            cluster_id=dict(type="str"),
            name=dict(type="str"),
            host=dict(type="str", required=True),
            username=dict(type="str"),
            password=dict(type="str", no_log=True),
            api_key=dict(type="str", no_log=True),
            validate_certs=dict(type="bool", default=True),
        ),
        supports_check_mode=True,
        required_if=[
            ("state", "absent", ("cluster_id",)),
        ],
    )

    if not HAS_CLIENT:
        module.fail_json(msg="Required Python libraries not found.")

    client = ApiClient(module)
    state = module.params["state"]
    resource_id = module.params.get("cluster_id")

    if state == "present":
        if resource_id:
            result = client.update("cluster", resource_id, module.params)
        else:
            if module.check_mode:
                module.exit_json(changed=True)
            result = client.create("cluster", module.params)
        module.exit_json(changed=True, cluster=result)
    else:
        if module.check_mode:
            module.exit_json(changed=True)
        client.delete("cluster", resource_id)
        module.exit_json(changed=True)


if __name__ == "__main__":
    main()
