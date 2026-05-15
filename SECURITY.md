# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in this collection, please report it privately to minimize potential harm.

### How to Report

Send security reports to: **sfulmer@redhat.com**

Please include:
- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact and severity assessment
- Suggested fix (if available)

### Response Timeline

- **Initial Response**: Within 48 hours of report
- **Status Update**: Within 7 days with assessment
- **Fix Timeline**: Critical issues prioritized for immediate patching

### Security Best Practices

When using this collection:

1. **Credential Management**
   - Always use Ansible Vault for sensitive data (passwords, API keys)
   - Never commit credentials to version control
   - Rotate credentials regularly

2. **Network Security**
   - Use TLS/SSL for all API communications
   - Set `validate_certs: true` in production (default)
   - Restrict network access to DDN Insight API endpoints

3. **Authentication**
   - Use dedicated service accounts with minimum required privileges
   - Implement role-based access control (RBAC) for API users
   - Monitor API access logs for suspicious activity

4. **Module Usage**
   - Review module documentation for security implications
   - Test changes in non-production environments first
   - Use check mode (`--check`) to preview changes

5. **Updates**
   - Keep the collection updated to latest version
   - Monitor security advisories and changelog
   - Subscribe to GitHub security alerts

### Disclosure Policy

Discovered vulnerabilities will be:
1. Confirmed and assessed for severity
2. Fixed in a security patch release
3. Publicly disclosed after patch availability
4. Credited to reporter (if desired)

### Security Considerations

This collection interacts with DDN Storage infrastructure. Key security aspects:

- **API Credentials**: Modules require authentication to DDN Insight API
- **State Changes**: Modules can modify storage configuration (filesystems, quotas, etc.)
- **Data Access**: Modules may access sensitive storage metadata
- **Network Exposure**: EDA webhook plugin opens network listener

Always follow the principle of least privilege and implement defense-in-depth strategies.

## Contact

For general security questions: sfulmer@redhat.com

For urgent security issues: Use email subject line "URGENT: Security Issue in ansible-ddn"
