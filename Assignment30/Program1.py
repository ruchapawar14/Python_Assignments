##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 30
##  Question    : 1
##  Date        : 22/07/2026
##################################################################################

import time
import schedule

def Display():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
##################################################################################
## Output:
## Jay Ganesh...
## Jay Ganesh...
## Jay Ganesh...
## Jay Ganesh...
## Jay Ganesh...
## Jay Ganesh...
## Jay Ganesh...
##################################################################################