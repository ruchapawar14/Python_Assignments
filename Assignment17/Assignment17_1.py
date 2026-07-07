##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 17
##  Question    : 1
##  Description : It is used to perform addition, subtraction, multiplication 
##                and division using functions from the Arithmetic module.
##  Date        : 06/07/2026
##################################################################################

from Arithmetic import * 

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ans = Add(Value1,Value2)
    print("The addition is : ",Ans)

    Ans = Sub(Value1,Value2)
    print("The subtraction is : ",Ans)

    Ans = Mult(Value1,Value2)
    print("The multiplication is : ",Ans)

    Ans = Div(Value1,Value2)
    print("The division is : ",Ans)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the first number : 20
##  Enter the second number : 10
##  The addition is :  30
##  The subtraction is :  10
##  The multiplication is :  200
##  The division is :  2.0
##################################################################################