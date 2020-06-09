"""
PROBLEM 56
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.?
"""

import sqlite3

con = sqlite3.connect ( 'university.db' )
c = con.cursor()

c.execute ("""CREATE TABLE students(
          Roll_number INTEGER,
          Full_name  TEXT,
          Age INTEGER, 
          Branch TEXT
          )"""
          )
con.commit()

c.execute("INSERT INTO students VALUES (01,'Mansi Pareek', 19, 'CSE')")
c.execute("INSERT INTO students VALUES (02,'Aditya Kumar', 19, 'CSE')")
c.execute("INSERT INTO students VALUES (03,'Shashank Singh';, 18, 'EE')")
c.execute("INSERT INTO students VALUES (04,'Mihir Kansara', 20, 'ME')")
c.execute("INSERT INTO students VALUES (05,'Riya Bhawnani', 18, 'CE')")
c.execute("INSERT INTO students VALUES (06,'Jayesh Singh', 19, 'CSE')")
c.execute("INSERT INTO students VALUES (07,'Khushboo Rathore', 18, 'CE')")
c.execute("INSERT INTO students VALUES (08,'Kshitij Mittal', 20, 'EC')")
c.execute("INSERT INTO students VALUES (09,'Pooja Rathore', 18, 'EE')")
c.execute("INSERT INTO students VALUES (10,'Nayna Pareek', 17, 'ME')")
con.commit()

c.execute("SELECT * FROM students")

from pandas import DataFrame
df = DataFrame(c.fetchall())  
df.columnS = ["Roll No.","Full Name","Age","Branch"]
print(df)

con.close()
