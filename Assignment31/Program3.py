
##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 31
##  Question    : 3
##  Date        : 22/07/2026
##################################################################################

import os
import time
import schedule
import datetime

def DirectoryScan(DirectoryName):

    FileCount = 0
    DirectoryCount = 0
    current = datetime.datetime.now()

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        FileCount = FileCount + len(FileName)
        DirectoryCount = DirectoryCount + len(SubFolder)

    print("Directory Scanned : ",DirectoryName)
    print("Total Files : ",FileCount)
    print("Total Subdirectories : ",DirectoryCount)
    print("Scan Time :", current.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():

    DirectoryName = input("Enter directory name : ")

    schedule.every(1).minutes.do(DirectoryScan,DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

##################################################################################
## Output:
## Enter directory name : /users/rucha14/Desktop/Python/Automation
## Directory Scanned :  /users/rucha14/Desktop/Python/Automation
## Total Files :  57
## Total Subdirectories :  4
## Scan Time : 22-07-2026 03:46:51 PM
##################################################################################