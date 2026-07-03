##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 12
##  Question    : 2
##  Description : It is used to print all the factors of a given number.
##  Date        : 26/06/2026
##################################################################################

def Factors(No):
    for i in range(1,No + 1):
        if(No % i == 0):
            print(i,end = " ")
    
def main():
    Value = int(input("Enter the number : "))

    print("Factors of",Value,"are :", end=" ")

    Result = Factors(Value)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 12
##  Factors of 12 are : 1 2 3 4 6 12
##
##  Enter the number : 34
##  Factors of 34 are : 1 2 17 34
##################################################################################