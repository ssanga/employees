# Employees API

FastAPI CRUD application for managing employees with SQLAlchemy and SQLite.

## Installation

```bash
pip install -r requirements.txt
```

## Project Structure

```
employees/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── employees.py      # Employee endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration settings
│   │   └── database.py        # Database connection
│   ├── models/
│   │   ├── __init__.py
│   │   └── employee.py        # SQLAlchemy models
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── employee.py        # Pydantic schemas
│   ├── __init__.py
│   └── main.py                # FastAPI application
├── tests/
│   └── __init__.py
├── .gitignore
├── requirements.txt
├── README.md
└── employees.db               # SQLite database
```

## Run the API

### Option 1: Using VS Code (Recommended)
Press **F5** to start the API in debug mode. The browser will automatically open at http://localhost:8000/docs

### Option 2: Command Line
```bash
uvicorn app.main:app --reload
```

### Option 3: Batch File
```bash
start_server.bat
```

The root URL (http://localhost:8000/) automatically redirects to the API documentation.

The API will be available at: http://localhost:8000

## API Documentation

Interactive API docs: http://localhost:8000/docs

## Endpoints

- **GET** `/employees/` - Get all employees
- **GET** `/employees/{id}` - Get employee by ID
- **POST** `/employees/` - Create new employee
- **PUT** `/employees/{id}` - Update employee
- **DELETE** `/employees/{id}` - Delete employee

## Example Usage

### Create Employee
```bash
curl -X POST "http://localhost:8000/employees/" -H "Content-Type: application/json" -d "{\"first_name\":\"Jane\",\"last_name\":\"Doe\",\"age\":30,\"department\":\"IT\",\"salary\":70000,\"hire_date\":\"2023-01-15\"}"
```

### Get All Employees
```bash
curl "http://localhost:8000/employees/"
```

### Get Employee by ID
```bash
curl "http://localhost:8000/employees/1"
```

### Update Employee
```bash
curl -X PUT "http://localhost:8000/employees/1" -H "Content-Type: application/json" -d "{\"salary\":80000}"
```

### Delete Employee
```bash
curl -X DELETE "http://localhost:8000/employees/1"
```
