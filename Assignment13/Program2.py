##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 13
##  Question    : 2
##  Description : It is used to calculate and print the area of a circle.
##  Date        : 26/06/2026
##################################################################################

def Area(Radius):
    pi = 3.14
    area = pi * Radius * Radius
    return area

def main():
    Radius = int(input("Enter the radius: "))

    area= Area(Radius)

    print("Area of circle is : ",area)
    
if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the radius : 5
##  Area of Circle is : 78.5
##
##  Enter the radius : 14
##  Area of Circle is : 615.44
##################################################################################