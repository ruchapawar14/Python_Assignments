##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 28
##  Question    : 3
##  Date        : 23/07/2026
##################################################################################

def DisplayFile(filename):
    fd = open(filename,"r")

    print(fd.read())

    fd.close()

def main():
    filename = input("Enter the file name : ")

    DisplayFile(filename)

if __name__ == "__main__":
    main()
##################################################################################
## Output:
## Enter the file name : Demo.txt
## Jay Ganesh.....
## Hello from Pune
## Rucha Hanumant Pawar
##################################################################################