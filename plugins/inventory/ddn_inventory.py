#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Steve Fulmer
# Apache-2.0 (see LICENSE)

"""DDN dynamic inventory plugin."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
name: ddn_inventory
plugin_type: inventory
short_description: DDN Insight dynamic inventory
version_added: "1.0.0"
description:
    - Dynamically discovers DDN storage infrastructure.
options:
    plugin:
        description: Token that ensures this is a source file for the plugin.
        required: true
        choices: ['stevefulme1.ddn.ddn_inventory']
    host:
        description: DDN Insight API host.
        required: true
        type: str
    username:
        description: API username.
        type: str
    password:
        description: API password.
        type: str
"""

from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.errors import AnsibleError


class InventoryModule(BaseInventoryPlugin):
    """DDN dynamic inventory plugin."""

    NAME = "stevefulme1.ddn.ddn_inventory"

    def verify_file(self, path):
        """Verify inventory file."""
        return path.endswith(("ddn_inventory.yml", "ddn_inventory.yaml"))

    def parse(self, inventory, loader, path, cache=True):
        """Parse inventory."""
        super(InventoryModule, self).parse(inventory, loader, path, cache)
        self._read_config_data(path)

        try:
            host = self.get_option("host")
            self.inventory.add_group("ddn_storage")
            self.inventory.add_host(host, group="ddn_storage")
            self.inventory.set_variable(host, "ansible_host", host)
        except Exception as e:
            raise AnsibleError(f"Failed to parse inventory: {str(e)}")
