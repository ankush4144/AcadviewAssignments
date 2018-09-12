#Q.1
pi=3.14
def area(rad):
    print("Area of sphere",4*pi*rad**2)
radius=int(input("Enter radius of sphere"))
area(radius)


#Q.2
def perfect(n):
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n and n!=0):
        return True
    else:
        return False
for i in range(1001):
    ans=perfect(i)
    if(ans==True):
        print("perfect number:",i)
    
#Q.3
num=int(input("Enter number whose multiplication table you want"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#Q.4
def calculate(n,p):
    if(p==1):
        return num
    if(p!=1):
        return(num*calculate(num,p-1))
    
num=int(input("Enter number"))
power=int(input("Enter its power"))
print(calculate(num,power))
