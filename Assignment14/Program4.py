##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 14
##  Question    : 4
##  Description : It is used to find and return the minimum of two given numbers
##                using a lambda function.
##  Date        : 03/07/2026
##################################################################################

Minimum = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Result = Minimum(Value1,Value2)

    print("The minimum number is",Result)

if __name__ == "__main__":
    main()
    



##################################################################################
##  Output:
##  Enter the first number : 16
##  Enter the second number : 19
##  The minimum number is 16
##
##  Enter the first number : 256
##  Enter the second number : 485
##  The minimum number is 256
##################################################################################