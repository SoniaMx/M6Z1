import sqlite3
conn = sqlite3.connect ("sqlproject.db")
cur = conn.cursor()
cur.execute ("SELECT * FROM  tasks")
rows = cur.fetchall()
print(rows)
row = cur.fetchone()
print(row)

def select_all(conn, projects):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {projects}")
    rows = cur.fetchall()
    return rows
projects = select_all(conn, "projects")
print(projects)

#select where muszę jeszcze lepiej ogarnąć
