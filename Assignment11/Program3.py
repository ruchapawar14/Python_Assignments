##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 11
##  Question    : 3
##  Description : It is used to calculate and print the sum of the digits of a 
##                number.
##  Date        : 26/06/2026
##################################################################################

def SumDigits(No):
    digits = 0
    sum = 0

    while(No != 0):
        Digit = No % 10
        sum = sum + Digit
        No = No // 10

    return sum

def main():
    Value = int(input("Enter the number : "))

    Result = SumDigits(Value)

    print("The Sum of digits is :",Result)


if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 1234
##  The Sum of digits is : 10
##################################################################################