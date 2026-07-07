##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 19
##  Question    : 3
##  Description : It is used to filter numbers between 70 and 90, increase each 
##                number by 10 using map(), and return the product of all elements
##                using reduce().
##  Date        : 07/07/2026
##################################################################################

from functools import reduce

ChkRange = lambda No : (No >= 70) and (No <= 90)
AddTen = lambda No : (No + 10)
Product = lambda No1,No2 : (No1 * No2)

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        No = int(input())
        Data.append(No)

    print("Input elements : ",Data)

    FData = list(filter(ChkRange,Data))
    print("List after filter : ",FData)

    MData = list(map(AddTen, FData))
    print("List after map : ",MData)

    RData = reduce(Product,MData)
    print("Output of reduce : ",RData)

if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter the number of elements : 12
##  Enter the elements : 
##  4
##  34
##  36
##  76
##  68
##  24
##  89
##  23
##  86
##  90
##  45
##  70
##  Input elements :  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
##  List after filter :  [76, 89, 86, 90, 70]
##  List after map :  [86, 99, 96, 100, 80]
##  Output of reduce :  6538752000
##################################################################################