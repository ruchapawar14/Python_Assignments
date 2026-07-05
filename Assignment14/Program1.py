##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 14
##  Question    : 1
##  Description : It is used to calculate and return the square of a given number 
##                using a lambda function.
##  Date        : 03/07/2026
##################################################################################

Square = lambda No : (No * No)

def main():
    Value = int(input("Enter the number : "))

    Square = Square(Value)

    print("Square of",Value,"is",Square)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the number : 5
##  Square of 5 is 25
##
##  Enter the number : 19
##  Square of 19 is 361
##################################################################################