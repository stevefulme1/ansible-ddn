# Contributing to ansible-ddn

Thank you for your interest in contributing to the DDN Storage Ansible Collection.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Ansible version, Python version, collection version
- DDN Insight API version (if applicable)
- Error messages or logs

### Suggesting Enhancements

For feature requests:
- Describe the use case and problem being solved
- Provide example playbook or workflow
- Consider backward compatibility

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Update documentation
7. Commit with descriptive message
8. Push to your fork
9. Open a pull request

## Development Setup

### Prerequisites

- Python 3.11 or later
- Ansible 2.16.0 or later
- Git
- Docker (for testing)

### Local Development

```bash
# Clone repository
git clone https://github.com/stevefulme1/ansible-ddn.git
cd ansible-ddn

# Install development dependencies
pip install -r requirements.txt

# Run tests
pytest tests/unit
ansible-test sanity --docker
```

## Code Standards

### Python Code

- Follow PEP 8 style guide
- Use type hints where appropriate
- Maximum line length: 120 characters
- Docstrings for all public functions and classes

### Ansible Modules

- Include full DOCUMENTATION, EXAMPLES, and RETURN blocks
- Support check mode (`supports_check_mode=True`)
- Handle errors gracefully with meaningful messages
- Use module_utils for shared code
- Follow Ansible module development best practices

### Testing Requirements

All contributions must include:

1. **Unit Tests**
   - Test all module functionality
   - Mock API interactions
   - Achieve >80% code coverage
   - Located in `tests/unit/plugins/modules/`

2. **Sanity Tests**
   - Pass `ansible-test sanity`
   - No pylint errors
   - No ansible-lint warnings

3. **Documentation**
   - Update README.md if adding features
   - Update CHANGELOG.md with changes
   - Add module documentation examples

### Running Tests

```bash
# Unit tests
pytest tests/unit -v

# Code coverage
pytest tests/unit --cov=plugins --cov-report=html

# Sanity tests
ansible-test sanity --docker default

# Specific Python version
ansible-test sanity --docker default --python 3.11

# Linting
ansible-lint
flake8 plugins/
```

## Documentation

- Module documentation uses Ansible doc fragments
- README.md provides collection overview and examples
- CHANGELOG.md follows Keep a Changelog format
- Code comments explain complex logic

## Commit Message Guidelines

Use clear, descriptive commit messages:

```
Add ddn_filesystem module for Lustre management

- Implement create, modify, delete operations
- Support stripe configuration
- Add comprehensive error handling
- Include unit tests and documentation
```

## Code Review Process

1. Maintainers review all pull requests
2. CI must pass (lint, sanity, unit tests)
3. At least one maintainer approval required
4. Changes may be requested for code quality or design
5. Merge when approved and CI passes

## Versioning

This project uses Semantic Versioning (SemVer):
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes (backward compatible)

## License

By contributing, you agree that your contributions will be licensed under the Apache-2.0 License.

## Questions?

- Open an issue for questions
- Check existing issues and documentation first
- Be respectful and constructive

## Maintainers

- Steven Fulmer (@stevefulme1)

Thank you for contributing!
