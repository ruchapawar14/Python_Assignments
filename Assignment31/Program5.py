##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 31
##  Question    : 5
##  Date        : 22/07/2026
##################################################################################

import os
import schedule
import time
import datetime

def DirectoryCount(DirectoryName):

    Border = "-"*40
    FileCount = 0
    Current = datetime.datetime.now()

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
       
        FileCount = FileCount + len(FileName)

    print("Total Files :", FileCount)

    fobj = open("MarvellousCountLog.txt", "a")

    fobj.write("Directory Path : " + DirectoryName + "\n")
    fobj.write("Number of files : " + str(FileCount) + "\n")
    fobj.write("Date and Time : " + Current.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    DirectoryName = input("Enter the directory name : ")

    schedule.every(5).minutes.do(DirectoryCount, DirectoryName)

    DirectoryCount(DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

