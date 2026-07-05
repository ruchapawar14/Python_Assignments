##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 14
##  Question    : 9
##  Description : It is used to calculate and return the multiplication of two given 
##                numbers using a lambda function.
##  Date        : 03/07/2026
##################################################################################

Multiplication = lambda No1,No2 : (No1 * No2)

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    mult = Multiplication(Value1,Value2)

    print("The multiplication is :",mult)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the first number : 12
##  Enter the second number : 12
##  The multiplication is : 144
##
##  Enter the first number : 14
##  Enter the second number : 23
##  The multiplication is : 322
##################################################################################