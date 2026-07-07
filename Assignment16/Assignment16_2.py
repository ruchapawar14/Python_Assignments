##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 16
##  Question    : 2
##  Description : It is used to check whether the entered number is even or odd.
##  Date        : 04/07/2026
##################################################################################

def ChkNum(No):
    if (No % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")
    
def main():
    Value = int(input("Enter the number : "))

    ChkNum(Value)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the number : 11
##  Odd Number
## 
##  Enter the number : 8
##  Even Number
##################################################################################