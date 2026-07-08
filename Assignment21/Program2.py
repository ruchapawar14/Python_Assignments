##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 21
##  Question    : 2
##  Description : It is used to create two threads that find and display the 
##                maximum and minimum elements from a list.
##  Date        : 07/07/2026
##################################################################################

import threading

def Maximum(Data):
    Max = Data[0]
    for No in Data:
        if(No > Max):
            Max = No
    print("The maximum number is : ",Max)        
 
def Minimum(Data):
    Min = Data[0]
    for No in Data:
        if(No < Min):
            Min = No
    print("The minimum number is : ",Min)        
         
def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")
    for i in range(Size):
        No = int(input())
        Data.append(No)

    Max = threading.Thread(target = Maximum, args = (Data,))
    Min = threading.Thread(target = Minimum, args = (Data,))

    Max.start()
    Min.start()

    Max.join()
    Min.join()

if (__name__ == "__main__"):
    main()


##################################################################################
##  Output:
##  Enter the number of elements : 7
##  Enter the elements :
##  13
##  45
##  87
##  9
##  34
##  27
##  10
##  The maximum number is : 87
##  The minimum number is : 9
##################################################################################