class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f() 
print a.g(), b.g() 


#output:
#"Error" if run in python 3


#output:
#AB
#AB if run in python 2
