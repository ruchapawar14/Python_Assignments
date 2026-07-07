##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 17
##  Question    : 9
##  Description : It is used to return the number of digits in the entered number.
##  Date        : 06/07/2026
##################################################################################

def CountDigits(No):
    Count = 0

    while(No != 0):
        Count = Count + 1
        No = No // 10
    
    return Count

def main():
    Value = int(input("Enter the number : "))

    ans = CountDigits(Value)

    print("The number of digits is : ",ans)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 5187934
##  The number of digits is :  7
##
##  Enter the number : 8767543789 
##  The number of digits is :  10
##################################################################################