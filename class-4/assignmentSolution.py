#Q.1- Reverse the whole list using list methods.
list1=[32,43,5,423]
print(list(reversed(list1)))

#Q.2- Print all the uppercase letters from a string.
string='HeLLo world'
for i in string:
    if(i.isupper()):
        print(i)

#Q.3- Split the user input on comma's and store the
#values in a list as integers.
str1=input("Enter list seperated by commas")
str1=str1.split(',')
list1=[]
for i in str1:
    list1.append(int(i))
print(list1)

#Q.4- Check whether a string is palindromic or not.
string=input("Enter string")
if(string==string[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")

#Q.5- Make a deepcopy of a list and write the
#difference between shallow copy and deep copy.
import copy
list1 =[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
list2 = copy.copy(list1)

print("Output of Shallow Copy : ")
list2[1][2] = 9
print(list1)
print(list2)

print("Output of Deep Copy : ")
list3 = copy.deepcopy(list1)
list3[0][1] = 23
print(list1)
print(list3)

