# Changelog

## [2.1.2] - 2026-05-18

### Security
- Added `no_log: true` to all `password` and `api_key` role arguments to prevent credential exposure in logs
- Changed EDA webhook default listen address from `0.0.0.0` to `127.0.0.1` to prevent unintended network exposure
- Added payload size limit (1 MB) to EDA webhook event source

## [2.1.1] - 2026-05-18

### Security
- Prevent credential leak in API request bodies — connection params (host, username, password, api_key, validate_certs) are now stripped before create/update payloads are sent to the remote API
- Add timeout=30 to all HTTP methods to prevent indefinite hangs
- Harden .gitignore to exclude secrets, credentials, and IDE artifacts

## [2.0.0] - 2026-05-17

### Added
- Idempotency: get-before-write with state comparison in 22 modules
- Pagination support (limit/offset) for all _info modules
- Pre-commit and linting configuration

### Fixed
- Role README files added for Galaxy compliance
- Galaxy import validation issues resolved

### Security
- Bumped requests>=2.32.5 to fix CVE-2023-32681, CVE-2024-35195
- Use urlencode for API query parameters

## [1.2.0] - 2026-05-15

### Added
- 50 modules covering full DDN Storage (EXAScaler/Lustre) platform API
- 10 Day-2 operation roles
- Dynamic inventory plugin
- EDA source plugins for event-driven automation

## [1.0.1] - 2026-05-15

### Fixed
- Module documentation rendering on Galaxy
- Module DOCUMENTATION: added all argument_spec params

## [1.0.0] - 2026-05-15

### Added
- Initial release with filesystem, storage pool, quota, snapshot, and health check modules
- EDA source plugins (webhook, metrics)
- Inventory plugin
- Unit tests and CI pipeline
