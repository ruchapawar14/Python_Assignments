#########################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 22
##  Question    : 1
##  Description : It is used to calculate the sum of squares from 1 to N for each 
##                number in a list using Pool.map() and multiprocessing.
##  Date        : 12/07/2026
#########################################################################################

import multiprocessing

def SumSquare(No):
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + (i * i)

    return Sum

def main():
    Data = [1000000,2000000,3000000,4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare,Data)

    pobj.close()
    pobj.join()

    print("The result is : ")
    print(Result)

if __name__ == "__main__":
    main()

#########################################################################################
##  Output:
##  The result is : 
##  [333333833333500000, 2666668666667000000, 9000004500000500000, 21333341333334000000]
#########################################################################################