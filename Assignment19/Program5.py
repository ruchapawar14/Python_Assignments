##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 19
##  Question    : 5
##  Description : It is used to filter prime numbers, multiply each prime number
##                by 2 using map(), and return the maximum number using reduce().
##  Date        : 07/07/2026
##################################################################################

from functools import reduce

def CheckPrime(No):
    if(No <= 1):
        return False
    for i in range(2,No):
        if(No % i == 0):
            return False
    return True

Multiplication = lambda No : (No * 2)

Maximum = lambda No1,No2 : No1 if(No1 > No2) else No2

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    print("Input elements : ",Data)

    FData = list(filter(CheckPrime,Data))
    print("List after filter : ",FData)

    MData = list(map(Multiplication,FData))
    print("List after map : ",MData)

    RData = reduce(Maximum,MData)
    print("Output of reduce : ",RData)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number of elements : 8
##  Enter the elements : 
##  2
##  70
##  11
##  10
##  17
##  23
##  31
##  77
##  Input elements :  [2, 70, 11, 10, 17, 23, 31, 77]
##  List after filter :  [2, 11, 17, 23, 31]
##  List after map :  [4, 22, 34, 46, 62]
##  Output of reduce :  62
##################################################################################