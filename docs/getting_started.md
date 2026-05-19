# Getting Started with stevefulme1.ddn

Ansible Collection for DDN Storage (DataDirect Networks) automation

## Installation

```bash
ansible-galaxy collection install stevefulme1.ddn
```

## Requirements

- Ansible >= 2.16
- Python >= 3.12

## Authentication

Most modules require authentication credentials. Set these as variables
in your playbook, inventory, or Ansible Vault:

```yaml
vars:
  api_url: "https://your-service.example.com"
  api_token: "{{ vault_api_token }}"
  validate_certs: true
```

Store sensitive credentials in Ansible Vault:

```bash
ansible-vault encrypt_string 'your-token-here' --name 'vault_api_token'
```

## Quick Example

```yaml
---
- name: Example playbook
  hosts: localhost
  connection: local
  gather_facts: false
  collections:
    - stevefulme1.ddn
  tasks:
    - name: Get info
      stevefulme1.ddn.ddn_alert:
        api_url: "{{ api_url }}"
        api_token: "{{ api_token }}"
      register: result

    - name: Show result
      ansible.builtin.debug:
        var: result
```

## Collection Contents

- **Modules**: 50
- **Roles**: 10
- **EDA plugins**: 2

## Next Steps

- Browse the module documentation: `ansible-doc stevefulme1.ddn.<module_name>`
- Check the [README](../README.md) for the full module and role list
- Review [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute
