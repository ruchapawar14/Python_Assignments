##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 15
##  Question    : 3
##  Description : It is used to find and return all odd numbers from a list 
##                using filter() with a lambda function.
##  Date        : 04/07/2026
##################################################################################

CheckOdd =lambda No : (No % 2 != 0)
    
def main():
    Data = [13,12,81,10,11,20]

    print("Input data is : ",Data)

    FData = list(filter(CheckOdd,Data))

    print("Odd numbers from list are : ",FData)


if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Input data is :  [13, 12, 81, 10, 11, 20]
##  Odd numbers from list are :  [13, 81, 11]
##################################################################################