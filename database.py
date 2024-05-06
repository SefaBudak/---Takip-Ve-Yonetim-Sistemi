import sqlite3

def create_table():
    with sqlite3.connect('Employees.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employees (
                id TEXT PRIMARY KEY,
                name TEXT,
                role TEXT,
                gender TEXT,
                status TEXT)''')

def fetch_employees():
    with sqlite3.connect('Employees.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Employees')
        employees = cursor.fetchall()
    return employees

def insert_employee(employee_id, employee_name, employee_role, employee_gender, employee_status):
    with sqlite3.connect('Employees.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Employees (id, name, role, gender, status) VALUES (?, ?, ?, ?, ?)',
                       (employee_id, employee_name, employee_role, employee_gender, employee_status))

def delete_employee(employee_id):
    with sqlite3.connect('Employees.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Employees WHERE id = ?', (employee_id,))

def update_employee(new_name, new_role, new_gender, new_status, employee_id):
    with sqlite3.connect('Employees.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Employees SET name = ?, role = ?, gender = ?, status = ? WHERE id = ?",
                       (new_name, new_role, new_gender, new_status, employee_id))

def id_exists(employee_id):
    with sqlite3.connect('Employees.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM Employees WHERE id = ?', (employee_id,))
        result = cursor.fetchone()
    return result[0] > 0

create_table()
