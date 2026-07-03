##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 11
##  Question    : 1
##  Description : It is used to check whether a number is a palindrome or not.
##  Date        : 26/06/2026
##################################################################################

def ChkPalindrome(No):
    num = No
    reverse = 0

    while(No != 0):
        digit = No % 10
        reverse = (reverse * 10) + digit
        No = No // 10

    if(reverse == num):
        return True
        
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    Result = ChkPalindrome(Value)

    if(Result == True):
        print(Value,"is a palindrome number")
    else:
        print(Value,"is not a palindrome number")


if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 121
##  121 is a palindrome number
##
##  Enter the number : 456
##  456 is not a palindrome number
##################################################################################