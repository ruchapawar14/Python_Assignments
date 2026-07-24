##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 28
##  Question    : 3
##  Date        : 23/07/2026
##################################################################################

import sys

def CopyFiles(FileName):

    fobj1 = open(FileName,"r")
    fobj2 = open("Demo.txt","w")

    Data = fobj1.read()

    fobj2.write(Data)

    fobj1.close()
    fobj2.close()

    print(f"Contents of {FileName} copied into Demo.txt")

def main():
    CopyFiles(sys.argv[1])

if __name__ == "__main__":
    main()

