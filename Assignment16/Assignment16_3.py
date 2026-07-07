##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 16
##  Question    : 3
##  Description : It is used to return the addition of the given 2 numbers
##  Date        : 04/07/2026
##################################################################################
def Add(No1,No2):
    sum = No1 + No2
    retuen sum

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ans = Add(Value1,Value2)

    print("Addition is : ",Ans)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter first number : 11
##  Enter second number : 5
##  Addition is :  16
##################################################################################