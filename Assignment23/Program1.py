##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 23
##  Question    : 1
##  Date        : 12/07/2026
##################################################################################

import multiprocessing
import os

def SumEven(No):
    sum = 0

    for i in range(2, No + 1, 2):
        sum = sum + i

    return (os.getpid(), No, sum)

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumEven, Data)

    pobj.close()
    pobj.join()

    for pid, num, sum in Result:
        print("The process ID is :", pid)
        print("The input element is :", num)
        print("The sum of even numbers is :", sum)
        print()

if __name__ == "__main__":
    main()
##################################################################################
## Output:
## The process ID is : 1360
## The input element is : 1000000
## The sum of even numbers is : 250000500000
##
## The process ID is : 1360
## The input element is : 2000000
## The sum of even numbers is : 1000001000000
##
## The process ID is : 1363
## The input element is : 3000000
## The sum of even numbers is : 2250001500000
## 
## The process ID is : 1359
## The input element is : 4000000
## The sum of even numbers is : 4000002000000
##################################################################################