##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 13
##  Question    : 1
##  Description : It is used to calculate and print the area of a rectangle.
##  Date        : 26/06/2026
##################################################################################

def Area(Length,Width):
    area = Length * Width
    return area
    

def main():
    Length = int(input("Enter the length : "))
    Width = int(input("Enter the width : "))

    Result = Area(Length,Width)

    print("Area of reactangle is :",Result)
    
if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the length : 10
##  Enter the width : 5
##  Area of Rectangle is : 50.0
##
##  Enter the length : 14
##  Enter the width : 8
##  Area of Rectangle is : 112
##################################################################################