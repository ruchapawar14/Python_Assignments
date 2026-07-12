############################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 22
##  Question    : 3
##  Date        : 12/07/2026
############################################################################################

import multiprocessing

def CountPrime(No):
    count = 0

    for i in range(2,No+1):
        prime = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False

        if prime == True:
            count = count + 1

    return count

def main():
    Data = [10000, 20000, 30000, 40000]

    pobj = multiprocessing.Pool()
    Result = pobj.map(CountPrime, Data)

    pobj.close()
    pobj.join()

    print("The Prime Count is : ")
    print(Result)

if __name__ == "__main__":
    main()

############################################################################################
##  Output:
##  The Prime Count is : 
##  [1229, 2262, 3245, 4203]
############################################################################################