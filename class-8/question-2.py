#l=[1,2,3]
#print(l[3])
#exception is index error

#handing-
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("Index of list is out of range")