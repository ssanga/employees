-- Create employees table
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL,
    hire_date DATE NOT NULL
);

-- Insert sample data
INSERT INTO employees (first_name, last_name, age, department, salary, hire_date) VALUES
    ('John', 'Smith', 35, 'Engineering', 75000.00, '2020-03-15'),
    ('Sarah', 'Johnson', 28, 'Marketing', 62000.00, '2021-06-01'),
    ('Michael', 'Williams', 42, 'Engineering', 95000.00, '2018-01-10'),
    ('Emily', 'Brown', 31, 'Human Resources', 58000.00, '2019-11-20'),
    ('David', 'Jones', 39, 'Sales', 68000.00, '2020-07-08');
