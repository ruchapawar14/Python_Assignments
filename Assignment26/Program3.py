##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 26
##  Question    : 3
##  Date        : 15/07/2026
##################################################################################

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the first number : "))
        self.Value2 = int(input("Enter the second number : "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        div = 0
        try:
            div = self.Value1 / self.Value2
        except ZeroDivisionError as zobj:
            print("Exception is occured due to second operand is zero")
        return div

aobj1 = Arithmetic()

aobj1.Accept()
print("The addition is : ",aobj1.Addition())
print("The subtraction is : ",aobj1.Subtraction())
print("The multiplication is : ",aobj1.Multiplication())
print("The division is : ",aobj1.Division())
print()

aobj2 = Arithmetic()

aobj2.Accept()
print("The addition is : ",aobj2.Addition())
print("The subtraction is : ",aobj2.Subtraction())
print("The multiplication is : ",aobj2.Multiplication())
print("The division is : ",aobj2.Division())

##################################################################################
## Output :
## Enter the first number : 15
## Enter the second number : 5
## The addition is :  20
## The subtraction is :  10
## The multiplication is :  75
## The division is :  3.0
##
## Enter the first number : 30
## Enter the second number : 0
## The addition is :  30
## The subtraction is :  30
## The multiplication is :  0
## Exception is occured due to second operand is zero
## The division is :  0
##################################################################################