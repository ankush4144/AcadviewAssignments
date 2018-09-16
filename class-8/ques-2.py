class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def setAge(self,age):
        self.age=age
    def setMarks(self,marks):
        self.marks=marks
    def display(self):
        print("Name of student : ",self.name)
        print("Roll no. of student",self.rollno)
        print("Age of student : ",self.age)
        print("Marks of student : ",self.marks)


student=Student(input("ENTER NAME OF STUDENT : "),int(input("ENTER ROLL NO : ")))
student.setAge(int(input("Enter age of student : ")))
student.setMarks(int(input("Enter marks of student : ")))
student.display()
