import sqlite3

def create_connection():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, roll TEXT)''')
    conn.commit()
    return conn

def add_student(conn, name, age, roll):
    c = conn.cursor()
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (name, age, roll))
    conn.commit()

def view_students(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    for row in c.fetchall():
        print(row)
