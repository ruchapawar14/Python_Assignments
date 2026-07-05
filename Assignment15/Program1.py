##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 15
##  Question    : 1
##  Description : It is used to find and return the square of each number in a 
##                list using map() with a lambda function.
##  Date        : 04/07/2026
##################################################################################

Square = lambda No : (No * No)

def main():
    Data = [5,8,12,16,20]

    print("Input data is : ",Data)

    MData = list(map(Square, Data))

    print("Square of data :", MData)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Input data is :  [5, 8, 12, 16, 20]
##  Square of data : [25, 64, 144, 256, 400]
##################################################################################