##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 18
##  Question    : 2
##  Description : It is used to accept N elements from the user and find the 
##                maximum element from the list.
##  Date        : 06/07/2026
##################################################################################

def ChkMaximum(Data):
    Max = 0

    for No in Data:
        if(No > Max):
            Max = No

    return Max

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Input elements : ",Data)
    
    max = ChkMaximum(Data)

    print("The maximum element is : ",max)
    
if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number of elements : 7
##  Enter the elements : 
##  13
##  5
##  45
##  7
##  4
##  56
##  34
##  Input elements :  [13, 5, 45, 7, 4, 56, 34]
##  The maximum element is :  56
##################################################################################