import requests
import json

BASE_URL = "http://localhost:8000"

def test_api():
    print("Testing Employees API\n")
    
    # Test 1: Get all employees
    print("1. GET all employees:")
    response = requests.get(f"{BASE_URL}/employees/")
    print(f"   Status: {response.status_code}")
    print(f"   Employees: {len(response.json())}")
    print()
    
    # Test 2: Get employee by ID
    print("2. GET employee by ID (1):")
    response = requests.get(f"{BASE_URL}/employees/1")
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        emp = response.json()
        print(f"   Name: {emp['first_name']} {emp['last_name']}")
    print()
    
    # Test 3: Create new employee
    print("3. POST - Create new employee:")
    new_employee = {
        "first_name": "Alice",
        "last_name": "Martinez",
        "age": 29,
        "department": "Finance",
        "salary": 72000.00,
        "hire_date": "2023-09-15"
    }
    response = requests.post(f"{BASE_URL}/employees/", json=new_employee)
    print(f"   Status: {response.status_code}")
    if response.status_code == 201:
        created = response.json()
        print(f"   Created ID: {created['id']}")
        new_id = created['id']
    print()
    
    # Test 4: Update employee
    print(f"4. PUT - Update employee salary:")
    update_data = {"salary": 78000.00}
    response = requests.put(f"{BASE_URL}/employees/{new_id}", json=update_data)
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        updated = response.json()
        print(f"   New salary: ${updated['salary']:,.2f}")
    print()
    
    # Test 5: Delete employee
    print(f"5. DELETE - Delete employee:")
    response = requests.delete(f"{BASE_URL}/employees/{new_id}")
    print(f"   Status: {response.status_code}")
    print()
    
    print("✓ All tests completed!")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to API. Make sure the server is running:")
        print("  uvicorn main:app --reload")
