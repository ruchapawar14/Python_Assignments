##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 23
##  Question    : 2
##  Date        : 12/07/2026
##################################################################################
import multiprocessing
import os

def SumOdd(No):
    sum = 0

    for i in range(1, No + 1, 2):
        sum = sum + i

    return (os.getpid(), No, sum)

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd, Data)

    pobj.close()
    pobj.join()

    for pid, num, sum in Result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Sum of Odd Numbers :", sum)
        print()

if __name__ == "__main__":
    main()


##################################################################################
## Output:
## Process ID : 1389
## Input Number : 1000000
## Sum of Odd Numbers : 250000000000
##
## Process ID : 1391
## Input Number : 2000000
## Sum of Odd Numbers : 1000000000000
##
## Process ID : 1389
## Input Number : 3000000
## Sum of Odd Numbers : 2250000000000
##
## Process ID : 1392
## Input Number : 4000000
## Sum of Odd Numbers : 4000000000000
##################################################################################