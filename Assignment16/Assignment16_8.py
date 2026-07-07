##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 16
##  Question    : 8
##  Description : It is used to display the * symbol the specified number of times.
##  Date        : 04/07/2026
##################################################################################

def Display(No):
    for i in range(No):
        print("*", end=" ")

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the number : 5
##  * * * * * 
##################################################################################