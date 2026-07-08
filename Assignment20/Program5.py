#################################################################################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 20
##  Question    : 5
##  Description : It is used to create two threads that display numbers from 1 to 50 and from 50 to 1 in reverse order.
##  Date        : 07/07/2026
#################################################################################################################################################


import threading

def Display():  
    print("The numbers from 1 to 50 are :")
 
    for i in range(1,51,1):
        print(i, end=" ")
    print()

def Reverse():
    print("The numbers from 50 to 1 are :")

    for i in range(50,0,-1):
        print(i, end=" ")
    print()

def main():
    thread1 = threading.Thread(target = Display)
    thread1.start()
    thread1.join()

    thread2 = threading.Thread(target = Reverse)
    thread2.start()
    thread2.join()

if (__name__ == "__main__"):
    main()
#################################################################################################################################################
##  Output:
##  The numbers from 1 to 50 are :
##  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 
##  The numbers from 50 to 1 are :
##  50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 

#################################################################################################################################################