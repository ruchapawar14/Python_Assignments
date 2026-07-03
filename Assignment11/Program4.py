##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 11
##  Question    : 4
##  Description : It is used to reverse and print a given number.
##  Date        : 26/06/2026
##################################################################################

def ReverseNumber(No):
    reverse = 0

    while(No != 0):
        digit = No % 10
        reverse = (reverse * 10) + digit
        No = No // 10

    return reverse

def main():
    Value = int(input("Enter the number : "))

    Result = ReverseNumber(Value)

    print("The reverse number is :", Result)    

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 1234
##  The reverse number is : 4321
##################################################################################