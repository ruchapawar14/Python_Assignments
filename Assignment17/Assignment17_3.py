##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 17
##  Question    : 3
##  Description : It returns the factorial of the given number
##  Date        : 06/07/2026
##################################################################################

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact 

def main():
    Value = int(input("Enter the number : "))

    fact = Factorial(Value)

    print(f"Factorial of {Value} is : {fact}")

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 5
##  Factorial of 5 is :  120
##
##  Enter the number : 16
##  Factorial of 16 is :  20922789888000
##################################################################################