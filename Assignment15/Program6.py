##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 15
##  Question    : 6
##  Description : It is used to find and return the minimum element from a list
##                using reduce() with a lambda function.
##  Date        : 04/07/2026
##################################################################################
from functools import reduce 

Minimum = lambda No1,No2 : No1 if No1 < No2 else No2
    
def main():
    Data = [74,24,10,29,53,34]

    print("Input data is : ",Data)

    RData = reduce(Minimum,Data)

    print("Minimum element from data is : ",RData)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Input data is :  [74, 24, 10, 29, 53, 34]
##  Minimum element from data is :  10
##################################################################################