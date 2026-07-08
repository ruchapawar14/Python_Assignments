##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 21
##  Question    : 1
##  Description : It is used to create two threads that display the prime numbers 
##                and non-prime numbers from a list of integers.
##  Date        : 07/07/2026
##################################################################################

import threading

def CheckPrime(No):
    if(No <= 1):
        return False

    for i in range(2,No):
        if(No % i == 0):
            return False

    return True

def PrimeNumber(Data):
    Result = list()

    for No in Data:
        if(CheckPrime(No) == True):
            Result.append(No)

    print("The prime numbers are : ",Result)

def NonPrimeNumber(Data):
    Result = list()

    for No in Data:
        if(CheckPrime(No) == False):
            Result.append(No)

    print("The non-prime numbers are : ",Result)

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    t1 = threading.Thread(target = PrimeNumber, args = (Data,))
    t2 = threading.Thread(target = NonPrimeNumber, args = (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if (__name__ == "__main__"):
    main()

##################################################################################
##  Output:
##  Enter the number of elements : 9
##  Enter the elements :
##  5
##  13
##  45
##  4
##  7
##  34
##  2
##  65
##  14
##  The prime numbers are : [5, 13, 7, 2]
##  The non-prime numbers are : [45, 4, 34, 65, 14]
##################################################################################