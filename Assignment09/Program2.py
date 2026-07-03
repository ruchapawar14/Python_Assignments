#################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 9
##  Question    : 2
##  Description : It is used to compare two numbers and print the greater number.
##  Date        : 26/06/2026
##################################################################################
def ChkGreater(No1,No2):
    if(No1 > No2):
        return No1
    else:
        return No2
    
def main():
    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Result = ChkGreater(Value1,Value2)

    print(Result,"is greater")

if __name__ == "__main__":
    main()
##################################################################################
##  Output:
##  Enter the first number : 
##  20
##  Enter the second number : 
##  10
##  20 is Greater
##################################################################################