##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 14
##  Question    : 6
##  Description : It is used to check whether a given number is odd
##                using a lambda function.
##  Date        : 03/07/2026
##################################################################################

CheckOdd = lambda No : (No % 2 != 0)       
    
def main():
    Value = int(input("Enter the number : "))       

    odd = CheckOdd(Value)                  

    if(odd == True):
        print("It is an odd number")
    else:
        print("It is not and odd number")

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 11
##  It is an odd number
##
##  Enter the number : 82
##  It is not and odd number
##################################################################################