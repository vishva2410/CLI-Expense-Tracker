
import sqlite3

def connect_db():
    conn = sqlite3.connect('expenses.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()

def add_exp(date, category, amount, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
        ''', (date, category, amount, description))

    conn.commit()
    conn.close()

def view_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM expenses')
    expenses = cursor.fetchall()

    conn.close()
    return expenses

def delete_expense(expense_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))

    conn.commit()
    conn.close()

def total_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT SUM(amount) FROM expenses')
    total = cursor.fetchone()[0]

    conn.close()
    return total if total is not None else 0.0

def category_summary():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    ''')

    summary = cursor.fetchall()

    conn.close()
    return summary
