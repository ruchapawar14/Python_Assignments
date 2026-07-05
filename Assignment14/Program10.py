##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 14
##  Question    : 10
##  Description : It is used to find and return the largest among three given numbers
##                using a lambda function.
##  Date        : 03/07/2026
##################################################################################

ChkLargest = lambda No1,No2,No3 : No1 if (No1 >= No2 and No1 >= No3) else (No2 if No2 >= No3 else No3)

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))
    Value3 = int(input("Enter the third number : "))


    Result = ChkLargest(Value1,Value2,Value3)

    print("The largest number is",Result)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the first number : 120
##  Enter the second number : 149
##  Enter the third number : 203
##  The largest number is 203
##################################################################################