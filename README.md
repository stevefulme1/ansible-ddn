# Ansible Collection - stevefulme1.ddn

Ansible Collection for automating DDN Storage (DataDirect Networks) infrastructure, including Lustre filesystem management, storage pools, quotas, snapshots, and health monitoring via the DDN Insight API.

## Description

This collection provides comprehensive automation for DDN Storage systems, enabling infrastructure-as-code workflows for high-performance computing (HPC) storage environments. It supports managing Lustre filesystems, storage pools, user/group quotas, snapshots, and cluster health diagnostics through the DDN Insight REST API.

## Requirements

- Ansible >= 2.16.0
- Python >= 3.11
- DDN Insight API access
- Network connectivity to DDN management interface

## Installation

### From Ansible Galaxy

```bash
ansible-galaxy collection install stevefulme1.ddn
```

### From Source

```bash
git clone https://github.com/stevefulme1/ansible-ddn.git
cd ansible-ddn
ansible-galaxy collection build
ansible-galaxy collection install stevefulme1-ddn-*.tar.gz
```

## Modules

### Filesystem Management
- `ddn_filesystem` - Create, modify, or delete Lustre filesystems
- `ddn_filesystem_info` - Retrieve filesystem information and status

### Storage Pool Management
- `ddn_storage_pool` - Manage storage pools
- `ddn_storage_pool_info` - Query storage pool details

### Quota Management
- `ddn_quota` - Configure user and group quotas
- `ddn_quota_info` - Retrieve quota information

### Snapshot Management
- `ddn_snapshot` - Create, delete, or manage filesystem snapshots
- `ddn_snapshot_info` - Query snapshot details

### Health and Diagnostics
- `ddn_health_check` - Execute health diagnostics
- `ddn_health_check_info` - Retrieve health check results
- `ddn_cluster_info` - Get cluster topology and configuration

## Inventory Plugin

The `ddn_inventory` plugin dynamically discovers DDN storage infrastructure from the Insight API.

## Event-Driven Ansible (EDA) Plugins

- `webhook` - Receive DDN alerts and events via webhook
- `metrics` - Poll LustrePerfMon metrics for threshold-based automation

## Example Playbook

```yaml
---
- name: Manage DDN Storage
  hosts: localhost
  gather_facts: false
  collections:
    - stevefulme1.ddn
  
  tasks:
    - name: Get cluster information
      ddn_cluster_info:
        host: insight.example.com
        username: admin
        password: "{{ vault_ddn_password }}"
      register: cluster
    
    - name: Create Lustre filesystem
      ddn_filesystem:
        host: insight.example.com
        username: admin
        password: "{{ vault_ddn_password }}"
        name: scratch
        state: present
        capacity: 100TB
        stripe_count: 4
        stripe_size: 1M
      register: result
    
    - name: Set user quota
      ddn_quota:
        host: insight.example.com
        username: admin
        password: "{{ vault_ddn_password }}"
        filesystem: scratch
        user: jdoe
        soft_limit: 10TB
        hard_limit: 15TB
        state: present
    
    - name: Create snapshot
      ddn_snapshot:
        host: insight.example.com
        username: admin
        password: "{{ vault_ddn_password }}"
        filesystem: scratch
        name: "snapshot_{{ ansible_date_time.date }}"
        state: present
    
    - name: Check cluster health
      ddn_health_check:
        host: insight.example.com
        username: admin
        password: "{{ vault_ddn_password }}"
      register: health
    
    - name: Display health status
      debug:
        var: health.status
```

## EDA Rulebook Example

```yaml
---
- name: DDN Storage Automation
  hosts: all
  sources:
    - stevefulme1.ddn.metrics:
        host: insight.example.com
        username: admin
        password: "{{ vault_ddn_password }}"
        interval: 60
        metrics:
          - filesystem_capacity
          - iops
          - throughput
  
  rules:
    - name: Alert on high capacity usage
      condition: event.filesystem_capacity_used_percent > 90
      action:
        run_playbook:
          name: capacity_alert.yml
```

## Module Documentation

All modules include comprehensive documentation accessible via `ansible-doc`:

```bash
ansible-doc stevefulme1.ddn.ddn_filesystem
ansible-doc stevefulme1.ddn.ddn_quota
ansible-doc stevefulme1.ddn.ddn_snapshot
```

## Authentication

All modules support the following authentication parameters:

- `host` - DDN Insight API hostname or IP
- `port` - API port (default: 443)
- `username` - API username
- `password` - API password
- `validate_certs` - Validate SSL certificates (default: true)

Use Ansible Vault to protect credentials:

```bash
ansible-vault create group_vars/all/vault.yml
```

## Testing

Run the test suite:

```bash
# Unit tests
pytest tests/unit

# Sanity tests
ansible-test sanity --docker

# Integration tests (requires DDN environment)
ansible-test integration --docker
```

## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Security

Report security issues to sfulmer@redhat.com. See [SECURITY.md](SECURITY.md) for details.

## License

Apache-2.0

## Support

- GitHub Issues: https://github.com/stevefulme1/ansible-ddn/issues
- Documentation: https://github.com/stevefulme1/ansible-ddn/blob/main/README.md

## Authors

- Steven Fulmer <sfulmer@redhat.com>

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.
