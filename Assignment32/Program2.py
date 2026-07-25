##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 32
##  Question    : 2
##  Date        : 23/07/2026
##################################################################################

import os
import time
import schedule
import datetime

def FileSize(FileName):

    Border = "-"*60
    timestamp = time.ctime()

    if not os.path.exists(FileName):
        print("File not found")
        return

    size = os.path.getsize(FileName)

    fobj = open("FileSizeLog.txt","a")

    fobj.write("File path : "+ FileName + "\n")
    fobj.write("File size in bytes : "+ str(size) + "bytes" + "\n")
    fobj.write("Date and time : "+ timestamp + "\n")
    fobj.write(Border + "\n")

    fobj.close()
    
def main():

    FileName = input("Enter file path : ")

    schedule.every(30).seconds.do(FileSize,FileName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

