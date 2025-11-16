@echo off
echo Running tests with coverage...
echo.

REM Run tests with coverage
python -m coverage run -m unittest discover -s tests -p "test_*.py" -v

echo.
echo ========================================
echo Coverage Report
echo ========================================
echo.

REM Show coverage report
python -m coverage report -m

echo.
echo Generating HTML coverage report...
python -m coverage html

echo.
echo ========================================
echo HTML report generated in htmlcov/index.html
echo ========================================
echo.

pause
