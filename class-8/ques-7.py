class Shape:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        return self.l*self.b
class rectangle(Shape):
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
        super().__init__(self.l,self.b)
class square(Shape):
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
        super().__init__(self.l,self.b)
sq=square(5,5)
rec=rectangle(3,4)
print("Area of square: ",sq.area())
print("Area of rectangle: ",rec.area())
        
