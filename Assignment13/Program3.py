##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 13
##  Question    : 3
##  Description : It is used to check whether a number is a perfect number or not.
##  Date        : 26/06/2026
##################################################################################

def ChkPerfect(No):
    sum = 0
    for i in range(1,No):
        if(No % i == 0):
            sum = sum + i

    if(sum == No):
        return True
    else:
        return False           
    
def main():
    Value = int(input("Enter the number : "))

    Result = ChkPerfect(Value)

    if(Result == True):
        print(Value,"is a perfect number")
    else:
        print(Value,"is not a perfect number")    

if(__name__ == "__main__"):
    main()        

##################################################################################
##  Output:
## Enter the number : 8
## 8 is not a perfect number
##
## Enter the number : 28
## 28 is a perfect number
##################################################################################