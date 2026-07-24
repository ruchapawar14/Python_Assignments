##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 29
##  Question    : 1
##  Date        : 23/07/2026
##################################################################################

import os

def CheckFile(FileName):

    if os.path.exists(FileName):
        print(f"{FileName} exists in current directory.")
    else:
        print(f"{FileName} not exists in current directory.")

def main():

    FileName = input("Enter the file name : ")

    CheckFile(FileName)

if __name__ == "__main__":
    main()

##################################################################################
## Output:
## Enter the file name : Demo.txt
## Demo.txt exists in current directory.
#################################################################################ś