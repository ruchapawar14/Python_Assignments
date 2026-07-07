##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 16
##  Question    : 6
##  Description : It is used to check whether the entered number is positive, 
##                negative, or zero.
##  Date        : 04/07/2026
###
###############################################################################

def ChkPositive(No):
    if(No > 0):
        print("Positive Number")
    elif(No < 0):
        print("Negative Number")
    else:
        print("Zero")

def main():
    Value = int(input("Enter the number : "))

    ChkPositive(Value)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the number : 11
##  Positive Number
##
##  Enter the number : -8
##  Negative Number
##
##  Enter the number : 0
##  Zero
##################################################################################