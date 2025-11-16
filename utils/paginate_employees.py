import requests

BASE_URL = "http://localhost:8000"
PAGE_SIZE = 20  # Number of employees per page

def paginate_employees():
    """Fetch all employees using pagination"""
    
    all_employees = []
    skip = 0
    page = 1
    
    print(f"Fetching employees with pagination (page size: {PAGE_SIZE})\n")
    
    while True:
        # Make request with pagination parameters
        response = requests.get(
            f"{BASE_URL}/employees/",
            params={"skip": skip, "limit": PAGE_SIZE}
        )
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
        
        employees = response.json()
        
        # If no more employees, break
        if not employees:
            break
        
        # Display page info
        print(f"Page {page} - Retrieved {len(employees)} employees (skip={skip})")
        
        # Show first 3 employees of this page
        for i, emp in enumerate(employees[:3], 1):
            print(f"  {i}. {emp['first_name']} {emp['last_name']} - {emp['department']} (${emp['salary']:,.2f})")
        
        if len(employees) > 3:
            print(f"  ... and {len(employees) - 3} more")
        print()
        
        # Add to total list
        all_employees.extend(employees)
        
        # If we got fewer employees than the page size, we're done
        if len(employees) < PAGE_SIZE:
            break
        
        # Move to next page
        skip += PAGE_SIZE
        page += 1
    
    print(f"{'='*60}")
    print(f"Total employees fetched: {len(all_employees)}")
    print(f"Total pages: {page}")
    
    # Show some statistics
    if all_employees:
        departments = {}
        total_salary = 0
        
        for emp in all_employees:
            dept = emp['department']
            departments[dept] = departments.get(dept, 0) + 1
            total_salary += emp['salary']
        
        print(f"\nDepartment distribution:")
        for dept, count in sorted(departments.items(), key=lambda x: x[1], reverse=True):
            print(f"  {dept}: {count}")
        
        print(f"\nAverage salary: ${total_salary / len(all_employees):,.2f}")
    
    return all_employees

if __name__ == "__main__":
    try:
        employees = paginate_employees()
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to API. Make sure the server is running:")
        print("  uvicorn app.main:app --reload")
        print("  or press F5 in VS Code")
