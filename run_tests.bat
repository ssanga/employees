@echo off
echo Running Employee API Tests...
echo.
python -m unittest tests.test_employees -v
echo.
pause
