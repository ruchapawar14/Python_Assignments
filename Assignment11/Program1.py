##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 11
##  Question    : 1
##  Description : It is used to check whether a number is prime or not.
##  Date        : 26/06/2026
##################################################################################
def ChkPrime(No):
    if(No <= 1):
        return False
    elif(No == 2):
        return True
    else:
        for i in range(2,(No + 1)):
            if(No % i == 0):
                return False
            else:
                return True
    
def main():
    Value = int(input("Enter the number : "))    

    Result = ChkPrime(Value)

    if(Result == True):
        print(Value,"is prime number")
    else:
        print(Value,"is not prime number")

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 11
##  11 is prime number
##
##  Enter the number : 20
##  20 is not prime number

##################################################################################