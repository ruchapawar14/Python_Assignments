##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 14
##  Question    : 7
##  Description : It is used to check whether a given number is divisible by 5  
##                using a lambda function.
##  Date        : 03/07/2026
##################################################################################

ChkDivisible = lambda No: (No % 5 == 0)

def main():
    Value = int(input("Enter the number : "))

    div = ChkDivisible(Value)

    if(div == True):
        print("The number is divisible by 5.")
    else:
        print("The number is not divisible by 5.")

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the number : 45
##  The number is divisible by 5.
##
##  Enter the number : 56
##  The number is not divisible by 5.
##################################################################################