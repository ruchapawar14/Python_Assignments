##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 18
##  Question    : 4
##  Description : It is used to accept N elements from the user and count the 
##                frequency of a specified element in the list.
##  Date        : 06/07/2026
##################################################################################

def Frequency(Data, Value):
    Count = 0

    for No in Data:
        if(No == Value):
            Count = Count + 1

    return Count

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    print("Input elements :", Data)

    Value = int(input("Enter the element to check its frequency : "))

    Ret = Frequency(Data, Value)

    print(f"Frequency of {Value} is : {Ret}")

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number of elements : 11
##  Enter the elements : 
##  13
##  5
##  45
##  7
##  4
##  56
##  5
##  34
##  2
##  5
##  65
##  Input elements : [13, 5, 45, 7, 4, 56, 5, 34, 2, 5, 65]
##  Enter the element to check its frequency : 5
##  Frequency of 5 is : 3
##################################################################################