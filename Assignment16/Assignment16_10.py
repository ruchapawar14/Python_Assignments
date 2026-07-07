##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 16
##  Question    : 10
##  Description : It is used to display the length of the entered name.
##  Date        : 04/07/2026
##################################################################################

def ChkLength(Name):
    return len(Name)

def main():
    Value = input("Enter the name : ")

    Ret = ChkLength(Value)

    print("Length of",Value,"is : ",Ret)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Enter the name : Marvellous 
##  Length of Marvellous is :  10
##
##  Enter the name : MACHINE LEARNING
##  Length of MACHINE LEARNING is :  16
##################################################################################