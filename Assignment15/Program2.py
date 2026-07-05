##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 15
##  Question    : 2
##  Description : It is used to find and return all even numbers from a list 
##                using filter() with a lambda function.
##  Date        : 04/07/2026
##################################################################################

CheckEven =lambda No : (No % 2 == 0)
    
def main():
    Data = [13,12,8,10,11,20]

    print("Input data is : ",Data)

    FData = list(filter(CheckEven,Data))

    print("Even numbers from list are  : ",FData)


if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Input data is :  [13, 12, 8, 10, 11, 20]
##  Even numbers from list are  :  [12, 8, 10, 20]
##################################################################################