############################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 22
##  Question    : 4
##  Date        : 12/07/2026
############################################################################################

import multiprocessing 
import time

def SumPower(No):
    sum = 0

    for i in range(1, No + 1):
        sum = sum + (i ** 5)

    return sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    Result = pobj.map(SumPower, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("The result is : ",Result)
    print(f"The total execution time is : {end_time - start_time : .4f} seconds")

if __name__ == "__main__":
    main()


############################################################################################
##  Output:
##  The result is :  [166667166667083333333333250000000000, 10666682666673333333333333000000000000, 121500121500033749999999999250000000000, 682667178666773333333333332000000000000]
##  The total execution time is :  0.4055 seconds
############################################################################################