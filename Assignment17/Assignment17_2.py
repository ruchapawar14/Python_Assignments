##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 17
##  Question    : 2
##  Description : It is used to display a square * pattern based on the entered 
##                number.
##  Date        : 06/07/2026
##################################################################################

def DisplayPattern(No):
    for i in range(No):
        for j in range(No):
            print("*", end=" ")
        print()

def main():
    Value = int(input("Enter the number : "))

    DisplayPattern(Value)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 5
##  * * * * * 
##  * * * * * 
##  * * * * * 
##  * * * * * 
##  * * * * * 
##################################################################################