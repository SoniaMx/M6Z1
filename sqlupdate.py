import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)


def update_task_status(conn, task_id, new_status):
    sql = '''UPDATE tasks
             SET status = ?
             WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (new_status, task_id))
    conn.commit()


if __name__ == "__main__":
    conn = create_connection("sqlproject.db")
    if conn:
        update_task_status(conn, 1, "completed")
        conn.close()
