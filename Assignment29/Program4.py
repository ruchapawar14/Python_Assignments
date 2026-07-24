##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 29
##  Question    : 4
##  Date        : 23/07/2026
##################################################################################

import sys

def CompareFiles(File1, File2):
    fobj1 = open(File1,"r")
    fobj2 = open(File2,"r")

    data1 = fobj1.read()
    data2 = fobj2.read()

    fobj1.close()
    fobj2.close()

    if(data1 == data2):
        print("Success")
    else:
        print("Failure")

def main():

    CompareFiles(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

##################################################################################
## Input:
## python3 program4.py ABC.txt Demo.txt 
## Output:
## Success
##################################################################################