##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 13
##  Question    : 5
##  Description : It is used to display the grade based on the marks entered.
##  Date        : 26/06/2026
##################################################################################

def Grade(marks):
    if(marks >= 75):
        print("Grade is : Distinction")
    elif(marks >= 60):
        print("Grade is : First Class")
    elif(marks >= 50):
        print("Grade is : Second Class")
    else:
        print("Grade is : Fail")

def main():
    Value = int(input("Enter the marks : "))

    Grade(Value)

if(__name__ == "__main__"):
    main()


##################################################################################
##  Output:
##  Enter the marks : 92
##  Grade is : Distinction
##
##  Enter the marks : 56
##  Grade is : Second Class
##################################################################################