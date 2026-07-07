##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 19
##  Question    : 2
##  Description : It is used to calculate the multiplication of two numbers 
##                using a lambda function.
##  Date        : 07/07/2026
##################################################################################

Multiplication = lambda No1,No2 : (No1 * No2)

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Multiplication(Value1,Value2)

    print(f"The mutiplication of {Value1} & {Value2} is : {Ret}")

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the first number : 4
##  Enter the second number : 3
##  The mutiplication of 4 & 3 is : 12
##
##  Enter the first number : 6
##  Enter the second number : 3
##  The mutiplication of 6 & 3 is : 18
##################################################################################