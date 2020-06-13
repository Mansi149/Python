"""
PROBLEM 58
Write a program to print the output of the following poblem statement :-
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.
Write a python code to insert records to a MongoDB (Atlas Cloud) database 
named db_University with collection named univ_coll for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch. ?
"""

import pymongo

Student = pymongo.MongoStudent("url")

mydb = Student.university_db  

def add_student(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    student_unique = mydb.university_coll.find_one({"Student Roll Number ": Student_Roll_no})
    if student_unique:
        return "Student already exists"
    else:
        mydb.forsk_coll.insert_one(
                {
                "Roll Number" : Student_Roll_no,
                "Name" : Student_Name,
                "Age" : Student_Age,
                "Branch" : Student_Branch
                })
        return "Student added successfully"
    
add_student(1234, 'Aditya Kumar', 19, 'CSE')
add_student(1235, 'Mansi Pareek', 19, 'CSE')
add_student(1236, 'Vaishnav Khatri', 20, 'EE')
add_student(1237, 'Saksham Singh', 19, 'ME')
add_student(1238, 'Yuvraj Ahuja', 18, 'CE')

def fetch_all_student():
    user = mydb.university_coll.find()
    for i in user:
        print (i)

fetch_all_student()
Student.close()
