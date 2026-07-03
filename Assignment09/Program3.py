#################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 9
##  Question    : 3
##  Description : It is used to calculate and print the square of a number.
##  Date        : 26/06/2026
##################################################################################
def Square(No):
    square = (No*No)
    return square
    
def main():
    print("Enter the number : ")
    Value = int(input())

    Result = Square(Value)

    print("Square of",Value,"is",Result)
    
if __name__ == "__main__":
    main()
##################################################################################
##  Output:
##  Enter the number :
##  5
##  Square of 5 is 25
##
##
##  Enter the number :
##  12
##  Square of 12 is 144
##################################################################################