#################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 10
##  Question    : 1
##  Description : It is used to print all even numbers up to the given number.
##  Date        : 26/06/2026
##################################################################################
def Even(No):

    for i in range(1,(No+1)):
        if(i % 2 == 0):
            print(i, end=" ")
  
def main():
    Value = int(input("Enter the number : "))

    print("Even number upto",Value,"are",end=" ")
    Even(Value)


if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number : 10
##  Even number upto 10 are 2 4 6 8 10
##################################################################################