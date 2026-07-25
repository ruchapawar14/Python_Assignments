##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 30
##  Question    : 5
##  Date        : 22/07/2026
##################################################################################

import schedule
import time
import datetime

def Display():
    current = datetime.datetime.now()

    fobj = open("Marvellous.txt", "a")
    fobj.write("Task executed at : " + current.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    fobj.close()
def main():
    schedule.every(5).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()
    
##################################################################################
## Output:
## Task executed at : 22-07-2026 02:24:31 PM
## Task executed at : 22-07-2026 02:29:31 PM
## Task executed at : 22-07-2026 02:34:31 PM
## Task executed at : 22-07-2026 02:39:31 PM
## Task executed at : 22-07-2026 02:44:31 PM
##################################################################################