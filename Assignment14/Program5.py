##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 14
##  Question    : 5
##  Description : It is used to check whether a given number is even 
##                using a lambda function.
##  Date        : 03/07/2026
##################################################################################

CheckEven = lambda No : (No % 2 == 0)       
    
def main():
    Value = int(input("Enter the number : "))       

    even = CheckEven(Value)                  

    if(even == True):
        print("It is an even number")
    else:
        print("It is not and even number")

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the number : 12
##  It is an even number
##
##  Enter the number : 65
##  It is not and even number
##################################################################################