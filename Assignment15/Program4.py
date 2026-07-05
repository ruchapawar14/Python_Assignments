##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 15
##  Question    : 4
##  Description : It is used to find and return the sum of all numbers in a list 
##                using reduce() with a lambda function.
##  Date        : 04/07/2026
##################################################################################
from functools import reduce 

Addition =lambda No1,No2 : (No1 + No2)
    
def main():
    Data = [10,20,30,40,50,60]

    print("Input data is : ",Data)

    RData = reduce(Addition,Data)

    print("Sum of all elements from data is : ",RData)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Input data is :  [10, 20, 30, 40, 50, 60]
##  Sum of all elements from data is :  210
##################################################################################