##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 15
##  Question    : 9
##  Description : It is used to find and return the product of all numbers in a 
##                list using reduce() with a lambda function.
##  Date        : 04/07/2026
##################################################################################
from functools import reduce 

Product = lambda No1,No2 : (No1 * No2)
    
def main():
    Data = [1,2,3,4,5,6,7,8,9,10]

    print("Input data is : ",Data)

    RData = reduce(Product,Data)

    print("Product of all numbers is : ",RData)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Input data is :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##  Product of all numbers is :  3628800
##################################################################################