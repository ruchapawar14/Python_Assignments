#################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 10
##  Question    : 5
##  Description : It is used to print all odd numbers up to the given number.
##  Date        : 26/06/2026
##################################################################################
def Odd(No):
    for i in range(1, No + 1, 2):
        print(i, end=" ")

def main():
    Value = int(input("Enter the number : "))

    print("Odd numbers upto", Value, "are", end=" ")
    Odd(Value)


if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 10
##  Odd numbers upto 10 are 1 3 5 7 9
###################################################################################