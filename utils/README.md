# Utilities

This folder contains utility scripts for database management and testing.

## Database Setup

### `create_database.sql`
SQL script to create the employees table structure.

### `init_database.py`
Initialize the database with the table structure and sample data.
```bash
python utils/init_database.py
```

### `seed_employees.py`
Add 100 random employees to the database.
```bash
python utils/seed_employees.py
```

### `check_database.py`
View database statistics and sample records.
```bash
python utils/check_database.py
```

## API Testing

### `paginate_employees.py`
Automatically fetch all employees using pagination.
```bash
python utils/paginate_employees.py
```

### `navigate_employees.py`
Interactive employee navigator with pagination controls.
```bash
python utils/navigate_employees.py
```

Commands:
- `n` - Next page
- `p` - Previous page
- `q` - Quit
- `[number]` - Change page size (e.g., type "5" for 5 records per page)

## Note
Make sure the API is running before using the testing scripts:
```bash
uvicorn app.main:app --reload
```
or press F5 in VS Code.
