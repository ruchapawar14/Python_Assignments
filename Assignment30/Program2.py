##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 30
##  Question    : 2
##  Date        : 22/07/2026
##################################################################################

import schedule
import time
import datetime

def Display():
    current = datetime.datetime.now()
    print("Current Date and Time : ",current.strftime("%d-%m-%Y %H:%M:%S PM"))

def main():
    schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()
##################################################################################
## Output:
## Current Date and Time :  22-07-2026 12:45:07 PM
## Current Date and Time :  22-07-2026 12:46:08 PM
## Current Date and Time :  22-07-2026 12:47:08 PM
## Current Date and Time :  22-07-2026 12:48:08 PM
##################################################################################