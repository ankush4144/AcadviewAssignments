class calculate():                              #class with all the functions of operations to be performed
    def addition(self,x,y):                     #Function for calculating add
        return x+y
    def subtraction(self,x,y):                  #Function for calculating subtraction
        return x-y
    def multiplication(self,x,y):               #Function for calculating multiplication
        return x*y
    def division(self,x,y):                     #Function for calculating division
        return x/y
    def factorial(self,num):                    #Function for calculating factorial
        if(num==1):
            return 1
        else:
            return num*self.factorial(num-1)
    def raiseToPower(self,base,exponent):       #Function for calculating factorial
        if(exponent==1):
            return base
        else:
            return base*self.raiseToPower(base,exponent-1)
    def floorDivision(self,x,y):
        return x//y
try:
    name=input("ENTER YOUR NAME: ")
    print()
    print()
    print("*******************************************************************************")
    print("\t\t\tWELCOME %s"%(name.upper()))
    print("\t\t\tHOW ARE YOU??")
    print("\t\t\tHOPE YOU ARE FINE!!")
    print("*******************************************************************************")
    
    calculation=calculate()                     #creation of object of calculate class
    choice=10
    while(choice!=0):
        print("Enter the following options")
        print('''1 for addition \n2 for subtraction\n3 for multiplication \n4 for division \n5 for factorial \n6 for raise to power \n7 for floor division\n0 to exit''')
        try:
            choice=int(input("Enter your choice : "))
            if(choice>7 or choice<0):
                raise ValueError
        except ValueError:
            print("*************ERROR: Please Enter Correct Choice*************")
            
        else:
            
                retry=True
                while(retry==True):
                    try:
                        if(choice==1):
                            print("Addition Of Two Numbers : ",calculation.addition(int(input("Enter 1st Number")),int(input("Enter 2nd Number"))))
                        elif(choice==2):
                            print("Subtraction Of Two Numbers : ",calculation.subtraction(int(input("Enter 1st Number")),int(input("Enter 2nd Number"))))
                        elif(choice==3):
                            print("Multiplication Of Two Numbers : ",calculation.multiplication(int(input("Enter 1st Number")),int(input("Enter 2nd Number"))))
                        elif(choice==4):
                            print("Division Of Two Numbers : ",calculation.division(int(input("Enter 1st Number")),int(input("Enter 2nd Number"))))
                        elif(choice==5):
                            print("Factorial of Numbers : ",calculation.factorial(int(input("Enter Number Whose Factorial You Want To Find : "))))
                        elif(choice==6):
                            print("Solution Of Raise To Power : ",calculation.raiseToPower(int(input("Enter Base")),int(input("Enter Exponent"))))
                        elif(choice==7):
                            print("Floor Division Of Two Numbers : ",calculation.floorDivision(int(input("Enter 1st Number")),int(input("Enter 2nd Number"))))
                    except ValueError:
                        print("*************ERROR: Please Enter Correct Values*************")
                        retry=True
                    except ZeroDivisionError:
                        print("*************ERROR: Number Cannot Be Divided By Zero*************")
                        retry=True
                    else:
                        retry=False
except:
        print("****************************PROGRAM TERMINATED BY USER**************************")
print("***************************THANKS FOR USING THE PROGRAM*************************")
                
