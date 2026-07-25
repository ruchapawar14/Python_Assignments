##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 30
##  Question    : 3
##  Date        : 22/07/2026
##################################################################################

import time
import schedule

def Display():
    print("Coding Kar..!")

def main():
    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    
##################################################################################
## Output:
## Coding Kar..!
## Coding Kar..!
## Coding Kar..!
##################################################################################