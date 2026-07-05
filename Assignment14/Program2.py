##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 14
##  Question    : 2
##  Description : It is used to calculate and return the cube of a given number 
##                using a lambda function.
##  Date        : 03/07/2026
##################################################################################

Cube = lambda No : (No * No * No)

def main():
    Value = int(input("Enter the number : "))

    cube = Cube(Value)

    print("Cube of",Value,"is",cube)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the number : 5
##  Cube of 5 is 125
##
##  Enter the number : 14
##  Cube of 14 is 2744
##################################################################################