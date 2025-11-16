# GitHub Actions

## Tests and Coverage Workflow

This workflow automatically runs tests and generates coverage reports on every push and pull request to `main` and `develop` branches.

### Features

- **Python 3.12**: Tests run on Python 3.12
- **Code coverage**: Generates coverage reports using `coverage.py`
- **Codecov integration**: Uploads coverage to Codecov (optional)
- **PR comments**: Automatically comments coverage on pull requests
- **Caching**: Caches pip dependencies for faster builds

### Workflow Triggers

- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

### Steps

1. Checkout code
2. Set up Python environment
3. Cache pip dependencies
4. Install dependencies
5. Run tests with coverage
6. Generate coverage report
7. Upload to Codecov (optional)
8. Comment coverage on PR (for pull requests)

### Local Testing

Run tests with coverage locally:

```bash
# Windows
run_tests_coverage.bat

# Linux/Mac
python -m coverage run -m unittest discover -s tests -p "test_*.py" -v
python -m coverage report -m
python -m coverage html
```

### Coverage Badge

To add a coverage badge to your README, use Codecov or Coveralls:

```markdown
[![codecov](https://codecov.io/gh/YOUR_USERNAME/YOUR_REPO/branch/main/graph/badge.svg)](https://codecov.io/gh/YOUR_USERNAME/YOUR_REPO)
```

### Configuration

Coverage settings are configured in `.coveragerc` file.
