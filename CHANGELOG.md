# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0]

### Added

- 50 modules covering full DDN Storage (EXAScaler/Lustre) platform API
- CRUD + info module for every resource type
- EDA source plugins for event-driven automation
- Unit tests and CI pipeline

## [1.0.0-initial] - 2026-05-15

### Added
- Initial release of stevefulme1.ddn collection
- Core modules for DDN Storage automation:
  - `ddn_filesystem` - Lustre filesystem management
  - `ddn_filesystem_info` - Filesystem information retrieval
  - `ddn_storage_pool` - Storage pool management
  - `ddn_storage_pool_info` - Storage pool information
  - `ddn_quota` - User and group quota management
  - `ddn_quota_info` - Quota information retrieval
  - `ddn_snapshot` - Filesystem snapshot management
  - `ddn_snapshot_info` - Snapshot information
  - `ddn_health_check` - Health diagnostics execution
  - `ddn_health_check_info` - Health check results
  - `ddn_cluster_info` - Cluster topology information
- Module utilities:
  - `ddn_api.py` - DDN Insight REST API client
- Documentation fragments:
  - `ddn_auth.py` - Common authentication options
- Inventory plugin:
  - `ddn_inventory` - Dynamic inventory from DDN Insight API
- Event-Driven Ansible (EDA) plugins:
  - `webhook` - Webhook event source for DDN alerts
  - `metrics` - LustrePerfMon metrics polling source
- Example EDA rulebook for automated responses
- Unit test framework with pytest
- CI/CD workflow for linting, sanity, and unit tests
- Comprehensive documentation (README, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT)
- Apache-2.0 license

### Requirements
- Ansible >= 2.16.0
- Python >= 3.11
- DDN Insight API access

[1.0.0]: https://github.com/stevefulme1/ansible-ddn/releases/tag/v1.0.0
