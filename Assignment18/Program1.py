##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 18
##  Question    : 1
##  Description : It is used to accept N elements from the user and calculate 
##                the addition of all elements in the list.
##  Date        : 06/07/2026
##################################################################################

def Addition(Data):
    Sum = 0

    for No in Data:
        Sum = Sum + No

    return Sum

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Input elements : ",Data)
    
    add = Addition(Data)

    print("The addition of all elements is : ",add)
    
if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number of elements : 6   
##  Enter the elements : 
##  13
##  5
##  45
##  7
##  4
##  56
##  Input elements :  [13, 5, 45, 7, 4, 56]
##  The addition of all elements is :  130
##################################################################################