try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("Division by zero not possible")
    
#exception is zerodivision