##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 23
##  Question    : 5
##  Date        : 12/07/2026
##################################################################################

import multiprocessing
import os

def Factorial(No):
    fact = 1

    for i in range(1, No + 1):
        fact = fact * i

    return (os.getpid(), No, fact)

def main():
    Data = [10, 15, 20, 25]

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    for pid, num, fact in Result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Factorial :", fact)
        print()

if __name__ == "__main__":
    main()

##################################################################################
## Output:
## Process ID : 1453
## Input Number : 10
## Factorial : 3628800
##
## Process ID : 1453
## Input Number : 15
## Factorial : 1307674368000
##
## Process ID : 1453
## Input Number : 20
## Factorial : 2432902008176640000
##
## Process ID : 1453
## Input Number : 25
## Factorial : 15511210043330985984000000
##################################################################################