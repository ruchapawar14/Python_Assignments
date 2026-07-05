##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 15
##  Question    : 8
##  Description : It is used to find and return all numbers divisible by both 3 
##                and 5 using filter() with a lambda function.
##  Date        : 04/07/2026
##################################################################################

ChkDivision = lambda No : (No % 3 == 0) and (No % 5 == 0)
    
def main():
    Data = [15,30,33,45,90,3,12,20,75,33,60]

    print("Input data is : ",Data)

    FData = list(filter(ChkDivision,Data))

    print("Numbers divisible by 3 & 5 are : ",FData)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Input data is :  [15, 30, 33, 45, 90, 3, 12, 20, 75, 33, 60]
##  Numbers divisible by 3 & 5 are :  [15, 30, 45, 90, 75, 60]
##################################################################################