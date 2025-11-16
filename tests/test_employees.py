import unittest
import sys
import os
from datetime import date

# Add parent directory to path to import app modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.database import Base, get_db
from app.models import Employee

# Create test database
TEST_DATABASE_URL = "sqlite:///./test_employees.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    """Override database dependency for testing"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

class TestEmployeesAPI(unittest.TestCase):
    """Integration tests for Employees CRUD API"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test database and client once for all tests"""
        Base.metadata.create_all(bind=engine)
        cls.client = TestClient(app)
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test database after all tests"""
        Base.metadata.drop_all(bind=engine)
        engine.dispose()  # Close all connections
        try:
            if os.path.exists("test_employees.db"):
                os.remove("test_employees.db")
        except PermissionError:
            pass  # File will be cleaned up later
    
    def setUp(self):
        """Clear database before each test"""
        db = TestingSessionLocal()
        db.query(Employee).delete()
        db.commit()
        db.close()
    
    def test_01_create_employee(self):
        """Test CREATE - Create a new employee"""
        employee_data = {
            "first_name": "John",
            "last_name": "Doe",
            "age": 30,
            "department": "Engineering",
            "salary": 75000.00,
            "hire_date": "2023-01-15"
        }
        
        response = self.client.post("/employees/", json=employee_data)
        
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["first_name"], "John")
        self.assertEqual(data["last_name"], "Doe")
        self.assertEqual(data["age"], 30)
        self.assertEqual(data["department"], "Engineering")
        self.assertEqual(data["salary"], 75000.00)
        self.assertIn("id", data)
    
    def test_02_create_employee_invalid_data(self):
        """Test CREATE - Invalid employee data"""
        invalid_data = {
            "first_name": "",  # Empty name
            "last_name": "Doe",
            "age": 30,
            "department": "Engineering",
            "salary": 75000.00,
            "hire_date": "2023-01-15"
        }
        
        response = self.client.post("/employees/", json=invalid_data)
        self.assertEqual(response.status_code, 422)  # Validation error
    
    def test_03_get_all_employees_empty(self):
        """Test READ - Get all employees when database is empty"""
        response = self.client.get("/employees/")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
    
    def test_04_get_all_employees(self):
        """Test READ - Get all employees"""
        # Create test employees
        employees = [
            {
                "first_name": "Alice",
                "last_name": "Smith",
                "age": 28,
                "department": "Marketing",
                "salary": 65000.00,
                "hire_date": "2022-03-10"
            },
            {
                "first_name": "Bob",
                "last_name": "Johnson",
                "age": 35,
                "department": "Sales",
                "salary": 70000.00,
                "hire_date": "2021-06-20"
            }
        ]
        
        for emp in employees:
            self.client.post("/employees/", json=emp)
        
        response = self.client.get("/employees/")
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["first_name"], "Alice")
        self.assertEqual(data[1]["first_name"], "Bob")
    
    def test_05_get_employees_with_pagination(self):
        """Test READ - Get employees with pagination"""
        # Create 5 test employees
        for i in range(5):
            employee = {
                "first_name": f"Employee{i}",
                "last_name": f"Test{i}",
                "age": 25 + i,
                "department": "IT",
                "salary": 50000.00 + (i * 1000),
                "hire_date": "2023-01-01"
            }
            self.client.post("/employees/", json=employee)
        
        # Test pagination
        response = self.client.get("/employees/?skip=0&limit=2")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        
        response = self.client.get("/employees/?skip=2&limit=2")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
    
    def test_06_get_employee_by_id(self):
        """Test READ - Get specific employee by ID"""
        # Create employee
        employee_data = {
            "first_name": "Jane",
            "last_name": "Wilson",
            "age": 32,
            "department": "HR",
            "salary": 68000.00,
            "hire_date": "2022-08-15"
        }
        
        create_response = self.client.post("/employees/", json=employee_data)
        employee_id = create_response.json()["id"]
        
        # Get employee by ID
        response = self.client.get(f"/employees/{employee_id}")
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], employee_id)
        self.assertEqual(data["first_name"], "Jane")
        self.assertEqual(data["last_name"], "Wilson")
    
    def test_07_get_employee_not_found(self):
        """Test READ - Get non-existent employee"""
        response = self.client.get("/employees/9999")
        
        self.assertEqual(response.status_code, 404)
        self.assertIn("not found", response.json()["detail"].lower())
    
    def test_08_update_employee(self):
        """Test UPDATE - Update employee data"""
        # Create employee
        employee_data = {
            "first_name": "Mike",
            "last_name": "Brown",
            "age": 40,
            "department": "Finance",
            "salary": 80000.00,
            "hire_date": "2020-01-10"
        }
        
        create_response = self.client.post("/employees/", json=employee_data)
        employee_id = create_response.json()["id"]
        
        # Update employee
        update_data = {
            "salary": 90000.00,
            "department": "Senior Finance"
        }
        
        response = self.client.put(f"/employees/{employee_id}", json=update_data)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["salary"], 90000.00)
        self.assertEqual(data["department"], "Senior Finance")
        self.assertEqual(data["first_name"], "Mike")  # Unchanged fields remain
    
    def test_09_update_employee_not_found(self):
        """Test UPDATE - Update non-existent employee"""
        update_data = {"salary": 100000.00}
        
        response = self.client.put("/employees/9999", json=update_data)
        
        self.assertEqual(response.status_code, 404)
    
    def test_10_update_employee_partial(self):
        """Test UPDATE - Partial update of employee"""
        # Create employee
        employee_data = {
            "first_name": "Sarah",
            "last_name": "Davis",
            "age": 29,
            "department": "Operations",
            "salary": 72000.00,
            "hire_date": "2021-11-05"
        }
        
        create_response = self.client.post("/employees/", json=employee_data)
        employee_id = create_response.json()["id"]
        
        # Update only age
        update_data = {"age": 30}
        
        response = self.client.put(f"/employees/{employee_id}", json=update_data)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["age"], 30)
        self.assertEqual(data["salary"], 72000.00)  # Unchanged
    
    def test_11_delete_employee(self):
        """Test DELETE - Delete employee"""
        # Create employee
        employee_data = {
            "first_name": "Tom",
            "last_name": "Anderson",
            "age": 45,
            "department": "Legal",
            "salary": 95000.00,
            "hire_date": "2019-04-20"
        }
        
        create_response = self.client.post("/employees/", json=employee_data)
        employee_id = create_response.json()["id"]
        
        # Delete employee
        response = self.client.delete(f"/employees/{employee_id}")
        
        self.assertEqual(response.status_code, 204)
        
        # Verify deletion
        get_response = self.client.get(f"/employees/{employee_id}")
        self.assertEqual(get_response.status_code, 404)
    
    def test_12_delete_employee_not_found(self):
        """Test DELETE - Delete non-existent employee"""
        response = self.client.delete("/employees/9999")
        
        self.assertEqual(response.status_code, 404)
    
    def test_13_root_redirect(self):
        """Test root endpoint redirects to docs"""
        response = self.client.get("/", follow_redirects=False)
        
        self.assertEqual(response.status_code, 307)  # Temporary redirect
        self.assertEqual(response.headers["location"], "/docs")
    
    def test_14_create_multiple_employees(self):
        """Test CREATE - Create multiple employees and verify count"""
        employees = []
        for i in range(10):
            employee_data = {
                "first_name": f"Employee{i}",
                "last_name": f"LastName{i}",
                "age": 25 + i,
                "department": "Testing",
                "salary": 50000.00 + (i * 5000),
                "hire_date": "2023-01-01"
            }
            response = self.client.post("/employees/", json=employee_data)
            self.assertEqual(response.status_code, 201)
            employees.append(response.json())
        
        # Verify all were created
        response = self.client.get("/employees/")
        self.assertEqual(len(response.json()), 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)
