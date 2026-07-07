##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 18
##  Question    : 5
##  Description : It is used to accept N elements from the user and calculate the 
##                addition of all prime numbers in list using a user-defined module.
##  Date        : 06/07/2026
##################################################################################

import MarvellousNum as mn

def PrimeSum(Data):
    Sum = 0

    for No in Data:
        if(mn.ChkPrime(No) == True):
            Sum = Sum + No

    return Sum


def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Input elements are :", Data)

    Result = PrimeSum(Data)

    print("The addition of prime numbers is :", Result)


if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number of elements : 11
##  Enter the elements : 
##  13
##  5
##  45
##  7
##  4
##  56
##  10
##  34
##  2
##  5
##  8
##  Input elements are : [13, 5, 45, 7, 4, 56, 10, 34, 2, 5, 8]
##  The addition of prime numbers is : 32
##################################################################################