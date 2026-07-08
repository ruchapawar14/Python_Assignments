##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 21
##  Question    : 4
##  Description : It is used to create two threads that calculate the sum and 
##                product of elements from a list and display the results in the 
##                main thread.
##  Date        : 07/07/2026
##################################################################################

import threading

def Summation(Data):
    Sum = 0
    for No in Data:
        Sum = Sum + No
    print("The Sum of all elements is : ",Sum)        
 
def Multiplication(Data):
    mult = 1
    for No in Data:
        mult = mult * No
    print("The product of all elemets is : ",mult)        
         
def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    t1 = threading.Thread(target = Summation, args = (Data,))
    t2= threading.Thread(target = Multiplication, args = (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if (__name__ == "__main__"):
    main()

##################################################################################
##  Output:
##  Enter the number of elements : 6
##  Enter the elements :
##  12
##  2
##  5
##  6
##  8
##  9
##  The Sum of all elements is : 42
##  The Product of all elements is : 51840
##################################################################################