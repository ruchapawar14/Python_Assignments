##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 15
##  Question    : 5
##  Description : It is used to find and return the maximum element from a list 
##                using reduce() with a lambda function.
##  Date        : 04/07/2026
##################################################################################
from functools import reduce 

Maximum = lambda No1,No2 : No1 if No1 > No2 else No2
    
def main():
    Data = [7,24,10,84,53,34]

    print("Input data is : ",Data)

    RData = reduce(Maximum,Data)

    print("Maximum element from data is  : ",RData)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Input data is :  [7, 24, 10, 84, 53, 34]
##  Maximum element from data is :  84
##################################################################################