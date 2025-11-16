import sqlite3
import random
from datetime import datetime, timedelta

# Lists for generating random data
first_names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Barbara", "David", "Elizabeth", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
    "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Donald", "Ashley",
    "Steven", "Kimberly", "Paul", "Emily", "Andrew", "Donna", "Joshua", "Michelle",
    "Kenneth", "Dorothy", "Kevin", "Carol", "Brian", "Amanda", "George", "Melissa",
    "Edward", "Deborah", "Ronald", "Stephanie", "Timothy", "Rebecca", "Jason", "Sharon",
    "Jeffrey", "Laura", "Ryan", "Cynthia", "Jacob", "Kathleen", "Gary", "Amy",
    "Nicholas", "Shirley", "Eric", "Angela", "Jonathan", "Helen", "Stephen", "Anna",
    "Larry", "Brenda", "Justin", "Pamela", "Scott", "Nicole", "Brandon", "Emma",
    "Benjamin", "Samantha", "Samuel", "Katherine", "Raymond", "Christine", "Gregory", "Debra",
    "Frank", "Rachel", "Alexander", "Catherine", "Patrick", "Carolyn", "Jack", "Janet",
    "Dennis", "Ruth", "Jerry", "Maria", "Tyler", "Heather", "Aaron", "Diane"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas",
    "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White",
    "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young",
    "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker",
    "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy",
    "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey",
    "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza",
    "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers",
    "Long", "Ross", "Foster", "Jimenez", "Powell", "Jenkins", "Perry", "Russell"
]

departments = [
    "Engineering", "Marketing", "Sales", "Human Resources", "Finance",
    "Operations", "Customer Support", "Product Management", "IT",
    "Legal", "Research and Development", "Quality Assurance"
]

def random_date(start_year=2015, end_year=2024):
    """Generate a random hire date"""
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

def generate_employees(count=100):
    """Generate random employee data"""
    employees = []
    for _ in range(count):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        age = random.randint(22, 65)
        department = random.choice(departments)
        salary = round(random.uniform(45000, 150000), 2)
        hire_date = random_date()
        
        employees.append((first_name, last_name, age, department, salary, hire_date))
    
    return employees

def seed_database(num_employees=100):
    """Add employees to the database"""
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    
    # Check current count
    cursor.execute("SELECT COUNT(*) FROM employees")
    current_count = cursor.fetchone()[0]
    print(f"Current employees in database: {current_count}")
    
    # Generate and insert new employees
    print(f"\nGenerating {num_employees} new employees...")
    employees = generate_employees(num_employees)
    
    cursor.executemany(
        "INSERT INTO employees (first_name, last_name, age, department, salary, hire_date) VALUES (?, ?, ?, ?, ?, ?)",
        employees
    )
    
    conn.commit()
    
    # Verify insertion
    cursor.execute("SELECT COUNT(*) FROM employees")
    new_count = cursor.fetchone()[0]
    print(f"✓ Successfully added {new_count - current_count} employees")
    print(f"Total employees in database: {new_count}")
    
    # Show some statistics
    cursor.execute("SELECT department, COUNT(*) as count FROM employees GROUP BY department ORDER BY count DESC")
    print("\nEmployees by department:")
    for dept, count in cursor.fetchall():
        print(f"  {dept}: {count}")
    
    cursor.execute("SELECT AVG(salary) FROM employees")
    avg_salary = cursor.fetchone()[0]
    print(f"\nAverage salary: ${avg_salary:,.2f}")
    
    conn.close()

if __name__ == "__main__":
    seed_database(100)
