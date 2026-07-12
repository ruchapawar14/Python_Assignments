##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 22
##  Question    : 2
##  Date        : 12/07/2026
##################################################################################

import os 
import multiprocessing


def Factorial(No):
    print("Process is running with the PID : ",os.getpid())

    Fact = 1
    for i in range(1, No+1):
        Fact = Fact * i

    return Fact

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    print("The input elements are : ",Data)

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial,Data)

    pobj.close()
    pobj.join()

    print("The result is : ")
    print(Result)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number of elements : 4
##  Enter the elements : 
##  10
##  15
##  20
##  25
##  The input elements are :  [10, 15, 20, 25]
##  Process is running with the PID :  1420
##  Process is running with the PID :  1420
##  Process is running with the PID :  1420
##  Process is running with the PID :  1420
##  The result is : 
##  [3628800, 1307674368000, 2432902008176640000, 15511210043330985984000000]
##################################################################################