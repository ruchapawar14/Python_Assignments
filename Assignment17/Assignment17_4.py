##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 17
##  Question    : 4
##  Description : It is used to return the addition of all factors of the 
##                entered number.
##  Date        : 06/07/2026
##################################################################################

def FactorSum(No):
    Sum = 0

    for i in range(1,No):
        if(No % i == 0):
            Sum = Sum + i

    return Sum

def main():
    Value = int(input("Enter the number : "))

    Ret = FactorSum(Value)

    print(f"The addition of factors of {Value} is : {Ret}") 

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 12
##  The addition of factors of 12 is : 16
##
##  Enter the number : 19
##  The addition of factors of 19 is : 1
##################################################################################