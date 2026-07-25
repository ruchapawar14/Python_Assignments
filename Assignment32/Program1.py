##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 32
##  Question    : 1
##  Date        : 22/07/2026
##################################################################################

import schedule
import time 
import datetime

def CreateFile():

    current = datetime.datetime.now()

    file = ("File_" + current.strftime("%d_%m_%Y %I_%M_%S") + ".txt")

    fobj = open(file,"w")

    fobj.write(" File Name : "+ file +"\n")
    fobj.write("Creation date : "+ current.strftime("%d_%m_%Y")+"\n")
    fobj.write("Creation time : "+ current.strftime("%H_%M_%S %p")+"\n")

    fobj.close()

def main():

    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    
