##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 32
##  Question    : 5
##  Date        : 25/07/2026
##################################################################################
import os
import schedule
import time

def DeleteEmptyFiles(DirectoryName):

    if not os.path.isdir(DirectoryName):
        print("Directory does not exists")
        return

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):

        for fname in FileName:

            FilePath = os.path.join(FolderName, fname)

            try:
                if os.path.getsize(FilePath) == 0:

                    os.remove(FilePath)

                    fobj = open("DeleteLog.txt", "a")
                    fobj.write(FilePath + "\n")
                    fobj.close()

                    print(FilePath, "Deleted successfully")

            except PermissionError:
                print("Permission denied :", FilePath)


def main():

    DirectoryName = input("Enter the directory name : ")

    schedule.every(5).seconds.do(DeleteEmptyFiles, DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()