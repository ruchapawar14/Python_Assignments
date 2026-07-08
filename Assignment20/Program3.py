##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 20
##  Question    : 3
##  Description : It is used to create two threads that calculate and display the 
##                sum of even elements and odd elements from a list of integers.
##  Date        : 07/07/2026
##################################################################################

import threading

def SumEven(Data):
    Sum = 0

    print("Even elements are :", end=" ")

    for No in Data:
        if(No % 2 == 0):
            print(No, end=" ")
            Sum = Sum + No
    
    print()
    print("Sum of even elements is : ",Sum)

def SumOdd(Data):
    Sum = 0

    print("Odd elements are :", end=" ")

    for No in Data:
        if(No % 2 != 0):
            print(No, end=" ")
            Sum = Sum + No

    print()
    print("Sum of odd elements is : ",Sum)

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    print("Input elements are : ",Data)

    EvenList = threading.Thread(target = SumEven, args= (Data,))
    EvenList.start()

    OddList = threading.Thread(target = SumOdd, args = (Data,))
    OddList.start()

    EvenList.join()
    OddList.join()

if (__name__ == "__main__"):
    main()

##################################################################################
##  Output:
##  Enter the number of elements : 8
##  Enter the elements : 
##  11
##  24
##  37
##  48
##  59
##  62
##  73
##  84
##  Input elements are :  [11, 24, 37, 48, 59, 62, 73, 84]
##  Even elements are : 24 48 62 84 
##  Sum of even elements is :  218
##  Odd elements are : 11 37 59 73 
##  Sum of odd elements is :  180
##################################################################################