##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 11
##  Question    : 2
##  Description : It is used to count and print the number of digits in a given 
##                number.
##  Date        : 26/06/2026
##################################################################################

def Digits(No):
    digits = 0

    if(No == 0):
        return 1

    while(No != 0):
        digits = digits + 1
        No = No // 10 

    return digits 

def main():
    Value = int(input("Enter the number : "))

    Result = Digits(Value)

    print("The number of digits is :",Result)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 42584
##  The number of digits is : 5
##
##  Enter the number : 12
##  The number of digits is : 2
##################################################################################