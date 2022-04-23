import sqlite3

conn = sqlite3.connect('studentPortal.db')
cur = conn.cursor()

def init():
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id integer primary key,
            name text,
            type_of_user text);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS courses (
            id integer primary key,
            name text
            teacher text);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS grades (
            course_id integer,
            student_id integer,
            grade integer);""")

def addUser(user_name, type_of_user):
    cur.execute("INSERT INTO users(name, type_of_user) VALUES('" + user_name + "', '" + type_of_user + "')")
    
def deleteUser(user_id):
    cur.execute("DELETE FROM users WHERE id = " + str(user_id))
    
def addGradeForStudemt(grades_course_id, grades_student_id, grade):
    cur.execute("INSERT INTO grades(course_id, student_id, grade) VALUES('" + grades_course_id + "', '" + grades_student_id + "')'")
    
conn.commit()
conn.close()

conn = sqlite3.connect('studentPortal.db')
cur = conn.cursor()

print("USERS")
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
  print(row)

print("COURSES")
cur.execute("SELECT * FROM courses")
rows = cur.fetchall()
for row in rows:
  print(row)

print("GRADES")
cur.execute("SELECT * FROM grades")
rows = cur.fetchall()
for row in rows:
  print(row)

conn.close()
