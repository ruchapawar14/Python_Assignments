##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 19
##  Question    : 1
##  Description : It is used to calculate the power of two of a given number 
##                using a lambda function.
##  Date        : 07/07/2026
##################################################################################

Power = lambda No : (No ** 2)

def main():
    Value = int(input("Enter the number : "))

    Ret = Power(Value)

    print(f"The power of {Value} is : {Ret}")

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 4
##  The power of 4 is : 16
##
##  Enter the number : 6
##  The power of 6 is : 36
##################################################################################