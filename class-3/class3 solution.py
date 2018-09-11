#Q.1- Create a list with user defined inputs.
list1=[]
num=int(input("Enter the number of elements in list"))
list1=[int(input("Enter element")) for i in range(num)]
print(list1)

#Q.2- Add the following list to above created list:
list2=['google','apple','facebook','microsoft','tesla']
list1+=list2
print(list1)

#Count the number of time an object occurs in a list.
list3=[1,2,2,3,3,4,5]
num=int(input("Enter number whose occurence u want to check"))
print("Count of",num,"is",list3.count(num))

#Q.4 - create a list with numbers and sort it in ascending order.
list3=[4,45,1,78,3,46,6,45,8,6]
print("Sorted list",sorted(list3))

#Q.5 Given are two one-dimensional arrays A and B which are sorted in ascending
#order.Write a program to merge them into a single sorted array C that
#contains every item from arrays A and B, in ascending order. [List] 
a=[[1,2,3],[5,23,6],[23,51,3]]
b=[[15,62,23],[53,223,63],[283,591,30]]
c=a+b
for i in range(len(c)):
    c[i]=sorted(c[i])
print(c)

#Q.6 - Count even and odd numbers in that list.
even=0
odd=0
for i in c:
    for j in i:
        if(j%2==0):
            even+=1
        else:
            odd+=1
print("count of even numbers is",even)
print("count of odd numbers is",odd)
