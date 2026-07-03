##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 12
##  Question    : 4
##  Description : It is used to print numbers from 1 up to the given number.
##  Date        : 26/06/2026
##################################################################################
def Display(No):
    for i in range(1, No + 1):
        print(i,end=" ")
    
def main():
    Value = int(input("Enter the number : "))

    print("Numbers from 1 to",Value, "are :", end=" ")

    Display(Value)
       
if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 5
##  Numbers from 1 to 5 are : 1 2 3 4 5
##
##  Enter the number : 12
##  Numbers from 1 to 12 are : 1 2 3 4 5 6 7 8 9 10 11 12
##################################################################################