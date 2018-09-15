#ImportError
try:
	import anushkaSharma
except ImportError:
	print("Nahi Vo Virat Ki hai")


#ValueError	
try:
    print(int('a'))
except ValueError:
    print("Exception Of ValueError Is Raised")


#IndexError    
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("Index of list is out of range")