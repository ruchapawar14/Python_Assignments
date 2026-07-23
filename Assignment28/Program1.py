##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 28
##  Question    : 1
##  Date        : 23/07/2026
##################################################################################

def CountLines(filename):
    file =  open(filename, "r")

    Count = 0
    for line in file:
        Count = Count + 1

    file.close()
    return Count 

def main():
    Name = input("Enter the file name : ")

    Result = CountLines(Name)
    print(f"The total number of lines in {Name} are : {Result}")

if __name__ == "__main__":
    main()

##################################################################################
## Output:
## Enter the file name : Demo.txt
## The total number of lines in Demo.txt are : 3
#################################################################################ś