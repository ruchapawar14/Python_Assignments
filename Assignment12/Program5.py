##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 12
##  Question    : 5
##  Description : It is used to print numbers in reverse order from the given 
##                number to 1.
##  Date        : 26/06/2026
##################################################################################
def Display(No):
    for i in range(No,0, -1):
        print(i,end=" ")
    
def main():
    Value = int(input("Enter the number : "))

    Display(Value)
       
if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 5
##  5 4 3 2 1
##
##  Enter the number : 9
##  9 8 7 6 5 4 3 2 1
##################################################################################