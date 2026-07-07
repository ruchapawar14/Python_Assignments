##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 16
##  Question    : 7
##  Description : It is used to check whether the entered number is divisible by 5.
##  Date        : 04/07/2026
##################################################################################

def ChkDivisible(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    Ret = ChkDivisible(Value)

    if(Ret == True):
        print("Divisible by 5")
    else:
        print("Not divisible by 5")

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the number : 8
##  Not divisible by 5
##
##  Enter the number : 25
##  Divisible by 5
##################################################################################