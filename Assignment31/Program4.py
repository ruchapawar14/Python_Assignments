##################################################################################
## Author      : Rucha Hanumant Pawar
## Assignment  : 31
## Question    : 4
## Date        : 22/07/2026
##################################################################################

import schedule
import time 
import datetime

def CreateLog():

    current = datetime.datetime.now()

    File = ("MarvellousLog_" + current.strftime("%d_%m_%Y %I_%M_%S %p") + ".txt")

    fobj = open(File,"w")

    fobj.write("Log file created successfully"+"\n")
    fobj.write("Creation Time : ")
    fobj.write(current.strftime("%d_%m_%Y %H_%M_%S %p"))

def main():

    schedule.every(10).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    