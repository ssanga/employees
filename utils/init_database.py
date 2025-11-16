import sqlite3

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Read and execute SQL file
with open('create_database.sql', 'r') as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)

# Commit changes
conn.commit()

# Verify the table was created
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employees'")
table_exists = cursor.fetchone()

if table_exists:
    print("✓ Table 'employees' created successfully!")
    
    # Show table structure
    cursor.execute("PRAGMA table_info(employees)")
    columns = cursor.fetchall()
    print("\nTable structure:")
    for col in columns:
        print(f"  - {col[1]} ({col[2]})")
    
    # Show sample data
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    print(f"\n✓ Inserted {len(rows)} sample records")
    print("\nSample data:")
    for row in rows:
        print(f"  ID: {row[0]}, Name: {row[1]} {row[2]}, Age: {row[3]}, Dept: {row[4]}, Salary: ${row[5]:,.2f}, Hired: {row[6]}")
else:
    print("✗ Error creating table")

# Close connection
conn.close()
