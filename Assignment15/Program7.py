##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 15
##  Question    : 7
##  Description : It is used to find and return all strings having a length greater 
##                than 5 using filter() with a lambda function.
##  Date        : 04/07/2026
##################################################################################

StringLen = lambda Str : len(Str) > 5
    
def main():
    Data = ["Maharashtra","Pune","Rucha","Air","Python","Marvellous"]

    print("Input data is : ",Data)

    FData = list(filter(StringLen,Data))

    print("Data after filter : ",FData)

if __name__ == "__main__":
    main()
    
##################################################################################
##  Output:
##  Input data is :  ['Maharashtra', 'Pune', 'Rucha', 'Air', 'Python', 'Marvellous']
##  Data after filter :  ['Maharashtra', 'Python', 'Marvellous']
##################################################################################