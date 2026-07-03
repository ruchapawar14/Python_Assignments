#################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 10
##  Question    : 2
##  Description : It is used to calculate and print the sum of the first N natural 
##                numbers.
##  Date        : 26/06/2026
##################################################################################
def Sum(No):
    Ans = 0

    for i in range(No + 1):
        Ans = Ans + i

    return Ans
    
def main():
    print("Enter the number : ")
    Value = int(input())
    
    Result = Sum(Value)
    
    print("The sum of first",Value,"natural numbers is",Result)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 5
##  Sum of first 5 natural numbers is : 15
##################################################################################