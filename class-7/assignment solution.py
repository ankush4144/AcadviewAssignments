#Q.1
dict={input("Enter key:"):input("Enter value:") for i in range(int(input("Enter number of key value pairs : ")))}
for i in dict.keys():
    print(i)



#Q.2
dict={}
num=int(input("Enter number of students:"))
for i in range(num):
    z=input("Enter name of student:")
    dict[z]={input("Enter name of subject: "):int(input("Enter marks: ")) for j in range(2)}
search=input("Enter name of student whose marks u want to display")
for i,j in dict.items():
    if(i==search):
        print("Student Found")
        print("Marks of student : ",j)
    else:
        print("Student not in list")

