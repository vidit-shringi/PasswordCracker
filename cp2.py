import tkinter as tk
import pandas as pd
import numpy as np
import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="students"
)

# Create a cursor object
mycursor = mydb.cursor()

# Create a table to store student data
mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, grade INT)")

# Define a function to add a new student
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    val = (name, age, grade)
    mycursor.execute(sql, val)
    mydb.commit()
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

# Define a function to delete a student
def delete_student():
    id = id_entry.get()
    sql = "DELETE FROM students WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    id_entry.delete(0, tk.END)

# Define a function to update student information
def update_student():
    id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    sql = "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s"
    val = (name, age, grade, id)
    mycursor.execute(sql, val)
    mydb.commit()
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

# Define a function to display student information
def display_students():
    df = pd.read_sql("SELECT * FROM students", mydb)
    students = df.to_numpy()
    for i in range(len(students)):
        for j in range(len(students[i])):
            tk.Label(window, text=students[i][j]).grid(row=i+1, column=j)

# Create the GUI
window = tk.Tk()
window.title("Student Management System")

# Add labels and entry fields
tk.Label(window, text="ID").grid(row=0, column=0)
id_entry = tk.Entry(window)
id_entry.grid(row=0, column=1)
tk.Label(window, text="Name").grid(row=1, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=1)
tk.Label(window, text="Age").grid(row=2, column=0)
age_entry = tk.Entry(window)
age_entry.grid(row=2, column=1)
tk.Label(window, text="Grade").grid(row=3, column=0)
grade_entry = tk.Entry(window)
grade_entry.grid(row=3, column=1)

# Add buttons
tk.Button(window, text="Add Student", command=add_student).grid(row=4, column=0)
tk.Button(window, text="Delete Student", command=delete_student).grid(row=4, column=1)
tk.Button(window, text="Update Student", command=update_student).grid(row=4, column=2)
tk.Button(window, text="Display Students", command=display_students).grid(row=5, column=1)

# Start the GUI
window.mainloop()
