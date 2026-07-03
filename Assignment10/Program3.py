#################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 10
##  Question    : 3
##  Description : It is used to calculate and print the factorial of a number.
##  Date        : 26/06/2026
##################################################################################
def Factorial(No):
    fact = 1

    for i in range(1, No + 1):
        fact = fact * i

    return fact

def main():
    print("Enter the number : ")
    Value = int(input())

    Result= Factorial(Value)

    print("Factorial of",Value,"is",Result)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 
##  5
##  Factorial of 5 is 120
##################################################################################