##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 23
##  Question    : 3
##  Date        : 12/07/2026
##################################################################################

import multiprocessing
import os

def CountEven(No):
    count = 0

    for i in range(2, No + 1, 2):
        count = count + 1

    return (os.getpid(), No, count)

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountEven, Data)

    pobj.close()
    pobj.join()

    for pid, num, count in Result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Even Number Count :", count)
        print()

if __name__ == "__main__":
    main()

##################################################################################
## Output:
##Process ID : 1407
## Input Number : 1000000
## Even Number Count : 500000
## 
## Process ID : 1405
## Input Number : 2000000
## Even Number Count : 1000000
##
## Process ID : 1408
## Input Number : 3000000
## Even Number Count : 1500000
##
## Process ID : 1407
## Input Number : 4000000
## Even Number Count : 2000000
##################################################################################