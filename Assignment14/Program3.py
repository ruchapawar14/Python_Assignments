
##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 14
##  Question    : 3
##  Description : It is used to find and return the maximum of two given numbers
##                using a lambda function.
##  Date        : 03/07/2026
##################################################################################

Maximum = lambda No1,No2 : No1 if No1 > No2 else No2

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Result = Maximum(Value1,Value2)

    print("The maximum number is",Result)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the first number : 56
##  Enter the second number : 74
##  The maximum number is 74
##
##  Enter the first number : 13
##  Enter the second number : 2
##  The maximum number is 13
##################################################################################