##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 17
##  Question    : 10
##  Description : It is used to return the addition of digits in the entered number.
##  Date        : 06/07/2026
##################################################################################

def AddDigits(No):
    Sum = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Value = int(input("Enter the number : "))

    Ans = AddDigits(Value)

    print("The addition of digits is : ",Ans)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 5187934
##  The addition of digits is :  37
## 
##  Enter the number : 987654321
##  The addition of digits is :  45
##################################################################################