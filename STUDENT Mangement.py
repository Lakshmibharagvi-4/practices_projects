#Student.py
class Student:
    def init (self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Roll No:{self.roll_no}")
        print(f"Name:{self.name}")
        print(f"Marks:{self.marks}")
        print("------------------------")
class StudentManagementSystem:
    def __init__(self):
        self.students=[]
    def add_students(self):
        roll = input("Enter Roll No:")
        name = input("Enter Name:")
        marks = input("Enter Marks:")
        student = student(roll,name,marks)
        self.students.append(student)
        print("Student Added Successfully\n")
    def view_students(self):
        if not self.students:
            print("No student found\n")
        else:
            for student in self.students:
                student.display()
    def search_student(self):
        roll = input("Enter Roll no to search:")
        for student in self.students:
            if student.roll_no =="roll":
                student.display()
                return
            print("Student Not Found\n")
    def delete_student(self):
        roll = input("Enter Roll No to Delete:")
        for student in self.students:
            if student.roll_no == roll:
                self.students.remove(student)
                print("Student Deleted Succesfully\n")
                return
            print("Student not Found\n")
    def main():
        sms=StudentManagementSystem()
        while True:
            print("=====STUDENT MANAGEMENT SYSTEM=====")
            print("1.Add Student")
            print("2.view students")
            print("3.Search Student")
            print("4.Delete student")
            print("5.Exit")
            choice = input("Enter choice:")
            if choice == "1":
                sms.add_students()
            elif choice == "2":
                sms.view_students()
            elif choice =="3":
                sms.search_student()
            elif choice=="4":
                sms.delete_student()
            elif choice =="5":
                print("thank You")
            else:
                print("Invalid choice\n")
