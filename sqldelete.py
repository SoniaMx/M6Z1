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

def delete_project(conn, project_id):
   """
   Delete a project by project id
   :param conn: Connection object
   :param project_id: id of the project to delete
   """
   sql = 'DELETE FROM projects WHERE id = ?'
   cur = conn.cursor()
   cur.execute(sql, (project_id,))
   conn.commit()

if __name__ == "__main__":
   conn = create_connection("sqlproject.db")

   project = ("Onboarding", "2020-05-13 00:00:00", "2020-05-14 00:00:00")
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

   print(f"Added project ID: {pr_id}, Added task ID: {task_id}")

   delete_project(conn, pr_id)
   print(f"Deleted project with ID: {pr_id}")

   conn.close()