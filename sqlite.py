import sqlite3
from sqlite3 import Error



def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn,create_table_sql):
    try:
        c=conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_data(self):
    cur=conn.cursor()
    cur.execute("INSERT INTO student_data VALUES(NULL,?,?,?,?)",(self.name.get(),self.roll.get(),self.dob.get(),self.gen.get()))
    conn.commit()
    conn.close()
    

    
#############################main
def main():
    login_table="""
            CREATE TABLE IF NOT EXISTS login(
            user TEXT NOT NULL,
            pass TEXT NOT NULL
            )
            """
    student_table="""
                CREATE TABLE IF NOT EXISTS student_data(
                id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                roll TEXT NOT NULL,
                dob TEXT NOT NULL,
                gender TEXT NOT NULL
                )
            """
    database=r"C:\Users\sia\Documents\GitHub\student_management\database.db"
    conn=create_connection(database)
    if conn is not None:
        create_table(conn,login_table)
        create_table(conn,student_table)
    else:
        print("error!")
if __name__=="__main__":
    main()
