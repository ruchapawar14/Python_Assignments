##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 32
##  Question    : 3
##  Date        : 23/07/2026
##################################################################################
    
import os
import schedule
import time

def DisplayFile(FileName):

    if not os.path.exists(FileName):
        print("File does not exist.")
        return False

    try:
        fobj = open(FileName, "r")

        Data = fobj.read()

        if len(Data) == 0:
            print("File is empty.")
            fobj.close()
            return False
        else:
            print(Data)

        fobj.close()
        return True 

    except PermissionError:
        print("Permission denied.")
        return False 

    except OSError:
        print("File cannot be opened.")
        return False

def main():
    FileName = input("Enter the name of file : ")

    schedule.every(1).minutes.do(DisplayFile,FileName)

    print("Reading the data from file...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

