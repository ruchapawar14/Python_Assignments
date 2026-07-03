##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 12
##  Question    : 3
##  Description : It is used to perform addition, subtraction,
##                multiplication and division of two numbers.
##  Date        : 26/06/2026
##################################################################################

def Calculation(No1,No2):
     sum = No1 + No2
     sub = No1 - No2
     mul = No1 * No2
     div = No1 / No2

     return sum,sub,mul,div
    
def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret1,Ret2,Ret3,Ret4 = Calculation(Value1,Value2)

    print("Addition is :",Ret1)
    print("Subtraction is :",Ret2)
    print("Multiplication is :",Ret3)
    print("Division is :",Ret4)
    
if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter first number : 10
##  Enter second number : 5
##  Addition is : 15
##  Subtraction is : 5
##  Multiplication is : 50
##  Division is : 2.0
##################################################################################