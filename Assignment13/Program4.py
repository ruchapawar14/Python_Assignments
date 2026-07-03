##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 13
##  Question    : 4
##  Description : It is used to convert a decimal number into its binary equivalent.
##  Date        : 26/06/2026
##################################################################################

def Binary(num):
    binary_num = 0
    place = 1

    while (num != 0):
        rem = num % 2
        binary_num = binary_num + rem * place
        place = place * 10
        num = num // 2

    return binary_num    
    
def main():
    Value = int(input("Enter the number : "))

    Result = Binary(Value)

    print("Binary number of ",Value,"is",Result)   

if(__name__ == "__main__"):
    main() 

##################################################################################
##  Output:
##  Enter the number : 16
##  Binary number of  16 is 10000
##
##  Enter the number : 59
##  Binary number of  59 is 111011
##################################################################################