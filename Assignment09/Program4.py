#################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 9
##  Question    : 4
##  Description : It is used to calculate and print the cube of a number.
##  Date        : 26/06/2026
##################################################################################
def Cube(No):
    cube = (No*No*No)
    return cube
    
def main():
    print("Enter the number : ")
    Value = int(input())

    Result = Cube(Value)

    print("Cube of",Value,"is",Result)
    
if __name__ == "__main__":
    main()
##################################################################################
##  Output:
##  Enter the number :
##   9
##  Cube of 9 is 729
##################################################################################