##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 29
##  Question    : 2
##  Date        : 23/07/2026
##################################################################################

def Display(FileName):
    fobj = open(FileName, "r")

    print(fobj.read())

    fobj.close()

def main():
    FileName = input("Enter the file name : ")

    Display(FileName)

if __name__ == "__main__":
    main()
##################################################################################
## Output:
## Enter the file name : ABC.txt
## JAY GANESH...
##################################################################################