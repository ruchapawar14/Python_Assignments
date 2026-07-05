##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 15
##  Question    : 10
##  Description : It is used to find and return the count of even numbers in a
##                list using filter() with a lambda function.
##  Date        : 04/07/2026
##################################################################################

CountEven= lambda No : (No % 2 == 0)
    
def main():
    Data = [2,10,15,17,22,47,56]

    print("Input data is : ",Data)

    FData = list(filter(CountEven,Data))

    print("Data after filter : ",FData)

    print("Count of even number is : ",len(FData))

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Input data is :  [2, 10, 15, 17, 22, 47, 56]
##  Data after filter :  [2, 10, 22, 56]
##  Count of even number is :  4
##################################################################################