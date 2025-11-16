import requests

BASE_URL = "http://localhost:8000"

def display_employees(employees, page, skip):
    """Display employees in a formatted table"""
    print(f"\n{'='*80}")
    print(f"Page {page} (showing records {skip + 1} to {skip + len(employees)})")
    print(f"{'='*80}")
    print(f"{'ID':<5} {'Name':<25} {'Age':<5} {'Department':<20} {'Salary':<12}")
    print("-" * 80)
    
    for emp in employees:
        name = f"{emp['first_name']} {emp['last_name']}"
        print(f"{emp['id']:<5} {name:<25} {emp['age']:<5} {emp['department']:<20} ${emp['salary']:>10,.2f}")
    
    print("-" * 80)

def navigate_employees_interactive():
    """Navigate through employees interactively"""
    
    page_size = 10
    skip = 0
    page = 1
    
    print("Employee Navigator")
    print("Commands: [n]ext, [p]revious, [q]uit, [number] to set page size")
    
    while True:
        # Fetch current page
        response = requests.get(
            f"{BASE_URL}/employees/",
            params={"skip": skip, "limit": page_size}
        )
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
        
        employees = response.json()
        
        if not employees:
            print("\nNo more employees to display.")
            skip = max(0, skip - page_size)
            continue
        
        # Display current page
        display_employees(employees, page, skip)
        
        # Get user input
        command = input(f"\nCommand (n/p/q or page size): ").strip().lower()
        
        if command == 'q':
            print("Exiting...")
            break
        elif command == 'n':
            if len(employees) == page_size:
                skip += page_size
                page += 1
            else:
                print("Already at the last page!")
        elif command == 'p':
            if skip > 0:
                skip = max(0, skip - page_size)
                page -= 1
            else:
                print("Already at the first page!")
        elif command.isdigit():
            new_size = int(command)
            if 1 <= new_size <= 100:
                page_size = new_size
                skip = 0
                page = 1
                print(f"Page size changed to {page_size}")
            else:
                print("Page size must be between 1 and 100")
        else:
            print("Invalid command. Use n (next), p (previous), q (quit), or a number for page size")

if __name__ == "__main__":
    try:
        navigate_employees_interactive()
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to API. Make sure the server is running:")
        print("  uvicorn app.main:app --reload")
        print("  or press F5 in VS Code")
    except KeyboardInterrupt:
        print("\n\nExiting...")
