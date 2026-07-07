##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 18
##  Question    : 3
##  Description : It is used to accept N elements from the user and find the 
##                minimum element from the list.
##  Date        : 06/07/2026
##################################################################################

def ChkMinimum(Data):
    Min = Data[0]

    for No in Data:
        if(No < Min):
            Min = No

    return Min

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Input elements : ",Data)
    
    min = ChkMinimum(Data)

    print("The minimum element is : ",min)
    
if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number of elements : 4
##  Enter the elements : 
##  13
##  5
##  45
##  7
##  Input elements :  [13, 5, 45, 7]
##  The minimum element is :  5
##################################################################################