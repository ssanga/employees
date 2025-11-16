import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Total count
cursor.execute("SELECT COUNT(*) FROM employees")
total = cursor.fetchone()[0]
print(f"Total employees: {total}\n")

# Show first 10 employees
cursor.execute("SELECT id, first_name, last_name, department, salary FROM employees LIMIT 10")
print("First 10 employees:")
print(f"{'ID':<5} {'Name':<25} {'Department':<25} {'Salary':<12}")
print("-" * 70)
for row in cursor.fetchall():
    print(f"{row[0]:<5} {row[1] + ' ' + row[2]:<25} {row[3]:<25} ${row[4]:>10,.2f}")

# Show last 10 employees
cursor.execute("SELECT id, first_name, last_name, department, salary FROM employees ORDER BY id DESC LIMIT 10")
print("\nLast 10 employees:")
print(f"{'ID':<5} {'Name':<25} {'Department':<25} {'Salary':<12}")
print("-" * 70)
for row in cursor.fetchall():
    print(f"{row[0]:<5} {row[1] + ' ' + row[2]:<25} {row[3]:<25} ${row[4]:>10,.2f}")

# Salary statistics
cursor.execute("SELECT MIN(salary), MAX(salary), AVG(salary) FROM employees")
min_sal, max_sal, avg_sal = cursor.fetchone()
print(f"\nSalary Statistics:")
print(f"  Minimum: ${min_sal:,.2f}")
print(f"  Maximum: ${max_sal:,.2f}")
print(f"  Average: ${avg_sal:,.2f}")

conn.close()
