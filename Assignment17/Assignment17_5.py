##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 17
##  Question    : 5
##  Description : It is used to check whether the entered number is a prime 
##                number or not.
##  Date        : 06/07/2026
##################################################################################

def ChkPrime(No):
    if(No <= 1):
        return False

    for i in range(2,No):
        if(No % i == 0):
            return False

    return True

def main():
    Value = int(input("Enter the number : "))

    Ret = ChkPrime(Value)

    if(Ret == True):
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 5
##  It is a prime number
##
##  Enter the number : 8
##  It is not a prime number
##################################################################################