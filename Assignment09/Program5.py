#################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 9
##  Question    : 5
##  Description : It is used to check whether a number is divisible by both 3 and 5.
##  Date        : 26/06/2026
##################################################################################
def ChkDivisible(No):
    if((No % 3 == 0) and (No % 5 == 0)):
        return True
    else:
        return False
    
def main():
    print("Enter the number : ")
    Value = int(input())
    
    Result = ChkDivisible(Value)

    if(Result == True):
        print(Value,"is divisible by 3 & 5")
    else:
        print(Value,"is not divisible by 3 & 5")
    
if __name__ == "__main__":
    main()
##################################################################################
##  Output:
##  Enter the number : 
##  15
##  15 is divisible by 3 and 5
##
##  Enter the number : 
##  2
##  2 is not divisible by 3 and 5
##################################################################################