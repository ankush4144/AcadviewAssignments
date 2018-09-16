pi=3.14
class circle:
    def __init__(self,radius):
        self.r=radius
    def getArea(self):
        return pi*self.r*self.r
    def getCircumference(self):
        return 2*pi*self.r

calculate=circle(int(input("Enter radius of circle")))
print("Area of circle : ",calculate.getArea())
print("Circumference of circle : ",calculate.getCircumference())
