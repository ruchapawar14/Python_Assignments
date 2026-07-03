#################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 10
##  Question    : 1
##  Description : It is used to print the multiplication table of a given number.
##  Date        : 26/06/2026
##################################################################################
def Table(No):
    for i in range(1,11):
        print(No * i, end=" ")

def main():
    Value = int(input("Enter the number : "))
    Table(Value)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
## Enter the number : 4
## 4 8 12 16 20 24 28 32 36 40
##################################################################################