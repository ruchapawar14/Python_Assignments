##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 17
##  Question    : 6
##  Description : It is used to display * pattern based on the entered number.
##  Date        : 06/07/2026
##################################################################################

def Display(No):
    for i in range(No, 0, -1):
        for j in range(i):
                print("*", end=" ")
        print()

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 5
##  * * * * * 
##  * * * * 
##  * * * 
##  * * 
##  * 
##################################################################################