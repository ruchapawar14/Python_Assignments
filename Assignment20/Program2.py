##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 20
##  Question    : 2
##  Description : It is used to create two threads that calculate and display the 
##                sum of even factors and odd factors of a given number.
##  Date        : 07/07/2026
##################################################################################
import threading

def SumEven(No):
    Sum = 0

    print("Even factors are :", end=" ")

    for i in range(1, No +1, 1):
        if((No % i == 0) and (i % 2 == 0)):
            print(i, end=" ")
            Sum = Sum + i

    print()
    print("Even sum is : ",Sum)

def SumOdd(No):
    Sum = 0

    print("Even factors are :", end=" ")

    for i in range(1, No+1, 1):
        if((No % i == 0) and (i % 2 != 0)):
            print(i, end=" ")
            Sum = Sum + i

    print()
    print("Odd sum is : ",Sum)
    
def main():
    Value = int(input("Enter the number : "))

    EvenFactor = threading.Thread(target = SumEven, args = (Value,))
    EvenFactor.start()

    OddFactor = threading.Thread(target = SumOdd, args = (Value,))
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()


##################################################################################
##  Output:
##  Enter the number : 18
##  Even factors are : 2 6 18  
##  Even sum is :  26
##  Even factors are : 1 3 9  
##  Odd sum is :  13
##  Exit from main
##################################################################################