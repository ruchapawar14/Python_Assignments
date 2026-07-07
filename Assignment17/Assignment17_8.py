##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 17
##  Question    : 8
##  Description : It is used to display a right-angled number pattern based on 
##                the entered number.
##  Date        : 06/07/2026
##################################################################################

def Display(No):
    for i in range(1, No + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 5
##  1	
##  1 2 
##  1 2 3 
##  1 2 3 4 
##  1 2 3 4 5 
##################################################################################