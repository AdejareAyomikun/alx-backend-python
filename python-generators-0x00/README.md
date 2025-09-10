# Python Generators – Seeding MySQL Database

## Objective
This project sets up a MySQL database **ALX_prodev** with a table `user_data` and populates it from a CSV file.

## Features
- Creates database `ALX_prodev` if it does not exist.
- Creates table `user_data` with fields:
  - `user_id` (UUID, PK, Indexed)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)
- Reads from `user_data.csv` and inserts rows if not already present.

## Functions
- `connect_db()` → connects to MySQL server.
- `create_database(connection)` → creates `ALX_prodev`.
- `connect_to_prodev()` → connects to `ALX_prodev` DB.
- `create_table(connection)` → creates `user_data`.
- `insert_data(connection, data)` → inserts rows from CSV.

## Usage
```bash
./0-main.py
