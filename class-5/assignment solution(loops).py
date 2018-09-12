#Q.1- Take 10 integers from user and print it on screen.
list1=[int(input("Enter number")) for i in range(10)]
for i in list1:
    print(i)


#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
#while(True):
    #print("Infinite Loop")
#I HAVE COMMENTED PRINT CODE TO RUN FURTHER CODE


#Q.3- Create a list of integer elements by user input. Make a new list which
#will store square of elements of previous list.
num=int(input("Enter number of elements"))
list1=[int(input("Enter your number")) for i in range(num)]
list2=[i**2 for i in list1]
print(list2)

#Q.4- From a list containing ints, strings and floats, make three lists to
#store them separately 
list1=[21,'hello',12.344,'bye',12,44,34.55]
stringList=[]
floatList=[]
intList=[]
for i in list1:
    if(type(i)==float):
        floatList.append(i)
    elif(type(i)==int):
        intList.append(i)
    elif(type(i)==str):
        stringList.append(i)
print(stringList)
print(floatList)
print(intList)

#Q.5- Using range(1,101), make a list containing only prime numbers. 4
list2=[int(i) for i in range(1,101)]
list1=[]
for i in list2:
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        if(i!=1):
            list1.append(i)
print("list of prime numbers:",list1)


#Q.6- Print the following patterns:
for i in range(4):
    for j in range(1,i+2):
        print("*",end='')
    print()


#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop. 
list1=[int(input("Enter number")) for i in range(int(input("Enter number of elements")))]
num=int(input("Enter number to be searched and deleted"))
for i in list1:
    if(num in list1):
        list1.remove(num)
        print("Number deleted")
        print("Final list",list1)
        break
else:
    print("Number not found")
        
