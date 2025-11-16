# Coverage Badge Setup

This project uses dynamic coverage badges that update automatically with each push to the main branch.

## Option 1: Dynamic Badge (Recommended)

### Setup Steps

1. **Create a GitHub Gist**
   - Go to https://gist.github.com/
   - Create a new **secret** gist
   - Name it: `employees-coverage.json`
   - Content: `{"schemaVersion": 1}`
   - Save and copy the Gist ID from the URL (e.g., `abc123def456`)

2. **Create a Personal Access Token**
   - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Click "Generate new token (classic)"
   - Name: `GIST_SECRET`
   - Select scope: `gist` (only this one)
   - Generate and copy the token

3. **Add Secret to Repository**
   - Go to your repository → Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `GIST_SECRET`
   - Value: Paste your token
   - Save

4. **Update Files**
   
   In `.github/workflows/tests.yml`, replace:
   ```yaml
   gistID: YOUR_GIST_ID
   ```
   With your actual Gist ID.
   
   In `README.md`, replace:
   ```markdown
   ![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/YOUR_USERNAME/YOUR_GIST_ID/raw/employees-coverage.json)
   ```
   With your actual username and Gist ID.

5. **Push Changes**
   - The badge will update automatically on each push to main branch
   - Badge color changes based on coverage:
     - 🔴 Red: 0-50%
     - 🟡 Yellow: 50-80%
     - 🟢 Green: 80-100%

## Option 2: Static Badge (Simple)

If you don't want to set up dynamic badges, use a static badge:

```markdown
![Coverage](https://img.shields.io/badge/coverage-96.36%25-brightgreen)
```

Update the percentage manually after running tests.

## Option 3: Codecov Badge

If you're using Codecov:

```markdown
[![codecov](https://codecov.io/gh/YOUR_USERNAME/employees/branch/main/graph/badge.svg)](https://codecov.io/gh/YOUR_USERNAME/employees)
```

## Current Coverage

Run locally to check coverage:
```bash
python -m coverage run -m unittest discover -s tests -p "test_*.py" -v
python -m coverage report -m
```

Current coverage: **96.36%**
