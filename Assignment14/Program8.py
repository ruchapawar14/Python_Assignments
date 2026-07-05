##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 14
##  Question    : 8
##  Description : It is used to calculate and return the addition of two given numbers
##                using a lambda function.
##  Date        : 03/07/2026
##################################################################################
 
Addition = lambda No1,No2 : (No1 + No2)

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    add = Addition(Value1,Value2)

    print("The addition is :",add)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the first number : 11
##  Enter the second number : 21
##  The addition is : 32
##
##  Enter the first number : 420
##  Enter the second number : 312
##  The addition is : 732
##################################################################################