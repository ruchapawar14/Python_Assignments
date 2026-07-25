##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 31
##  Question    : 1
##  Date        : 22/07/2026
##################################################################################

import schedule
import time

def Display(message):
    print(message)

def main():

    message = input("Enter message : ")
    interval = int(input("Enter interval in seconds : "))

    if interval <= 0:
        print("Interval must be greater than zero.")
        return

    schedule.every(interval).seconds.do(Display, message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
##################################################################################
## Output:
## Enter message : Jay Ganesh
## Enter interval in seconds : 5
## Jay Ganesh
## Jay Ganesh
## Jay Ganesh
## Jay Ganesh
## Jay Ganesh
##################################################################################