import sqlite3

def create_connection(db_file):
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

def add_project(conn, project):
   sql = '''INSERT INTO projects(nazwa, start_date, end_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, project)
   conn.commit()
   return cur.lastrowid

def add_task(conn, task):
   sql = '''INSERT INTO tasks(project_id, nazwa, opis, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, task)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
   project = ("Onboarding", "2020-05-13 00:00:00", "2020-05-14 00:00:00")

   conn = create_connection("sqlproject.db")
   pr_id = add_project(conn, project)

   task = (
       pr_id,
       "prezentacja",
       "zrób prezentację w powerpoint",
       "to do",
       "2020-05-12 12:00:00",
       "2020-05-13 15:00:00"
   )

   task_id = add_task(conn, task)

   print(pr_id, task_id)
   conn.commit()
   conn.close()