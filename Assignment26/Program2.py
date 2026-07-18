##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 26
##  Question    : 2
##  Date        : 15/07/2026
##################################################################################

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle : "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("The radius of the circle is :", self.Radius)
        print(f"The area of the circle is :{self.Area:.2f}")
        print(f"The circumference of the circle is : {self.Circumference:.2f}")
        print()


cobj1 = Circle()

cobj1.Accept()
cobj1.CalculateArea()
cobj1.CalculateCircumference()
cobj1.Display()


cobj2 = Circle()

cobj2.Accept()
cobj2.CalculateArea()
cobj2.CalculateCircumference()
cobj2.Display()


##################################################################################
## Output : 
## Enter the radius of the circle : 143.4
## The radius of the circle is : 143.4
## The area of the circle is :64569.58
## The circumference of the circle is : 900.55
##
## Enter the radius of the circle : 67.7
## The radius of the circle is : 67.7
## The area of the circle is :14391.53
## The circumference of the circle is : 425.16
##################################################################################