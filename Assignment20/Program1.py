##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 20
##  Question    : 1
##  Description : It is used to create two separate threads to display the first 
##                10 even numbers and the first 10 odd numbers.
##  Date        : 07/07/2026
##################################################################################

import threading

def DisplayEven():
    print("Even numbers : ")
    for i in range(2,21,2):
        print(i, end=" ")
    print()

def DisplayOdd():
    print("Odd numbers : ")
    for i in range(1,20,2):
        print(i, end=" ")
    print()

def main():
    Even = threading.Thread(target = DisplayEven)
    Even.start()

    print()

    Odd = threading.Thread(target = DisplayOdd)
    Odd.start()

    Even.join()
    Odd.join()

if (__name__ == "__main__"):
    main()

##################################################################################
##  Output:
##  Even numbers : 
##  2 4 6 8 10 12 14 16 18 20 
##
##  Odd numbers : 
##  1 3 5 7 9 11 13 15 17 19 
##################################################################################