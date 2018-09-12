#Q.1- Take an input year from user and decide whether it is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("leap year")
       else:
           print("not a leap year")
   else:
       print("leap year")
else:
   print("not a leap year")

#Q.2- Take length and breadth input from user and check
#whether the dimensions are of square or rectangle.
length=int(input("Enter length"))
breadth=int(input("Enter breadth"))
if(length==breadth):
    print("Its a square")
else:
    print("Its a rectangle")


#Q.3- Take the input age of 3 people and
#determine oldest and youngest among them.
list1=[input("Enter age") for i in range(3)]
print("youngest man's age",min(list1))
print("oldest man's age",max(list1))

#Q.4- Ask user to enter age, sex ( M or F ), marital
#status ( Y or N ) and then using following rules print their place of service.
age=int(input("Enter age"))
sex=input("Enter sex (M or F)")
maritalStatus=input("Enter marital status")
if(sex=='F'):
    print("SHE CAN WORK IN URBAN AREAS ONLY")
elif(sex=='M' and age>=20 and age<=40):
    print("HE CAN WORK ANYWHERE")
elif(sex=='M' and age>=40 and age<=60):
    print("HE CAN WORK IN URBAN AREAS ONLY")
else:
    print("ERROR")

#Q.5- A shop will give discount of 10% if the cost of purchased quantity is
#more than 1000.Ask user for quantity Suppose, one unit will cost 100.
#Judge and print total cost for user.
quantity=int(input("Enter quantity"))
total_cost=quantity*100
if(total_cost>1000):
    total_cost-=total_cost*0.1
print("Total cost is:",total_cost)
