########################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 19
##  Question    : 4
##  Description : It is used to filter even numbers, calculate their squares using 
##                map(), and return the addition of all squared numbers using reduce().
##  Date        : 07/07/2026
#######################################################################################

from functools import reduce

Even = lambda No : (No % 2 == 0)
Square = lambda No : (No * No)
Addition = lambda No1,No2 : (No1 + No2)

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    print("Input elements : ",Data)

    FData = list(filter(Even,Data))
    print("List after filter : ",FData)

    MData = list(map(Square,FData))
    print("List after map : ",MData)

    RData = reduce(Addition,MData)
    print("Output of reduce : ",RData)

if __name__ == "__main__":
    main()

########################################################################################
##  Output:
##  Enter the number of elements : 10
##  Enter the elements : 
##  5
##  2
##  3
##  4
##  3
##  4
##  1
##  2
##  8
##  10
##  Input elements :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
##  List after filter :  [2, 4, 4, 2, 8, 10]
##  List after map :  [4, 16, 16, 4, 64, 100]
##  Output of reduce :  204
########################################################################################