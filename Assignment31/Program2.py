##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 31
##  Question    : 2
##  Date        : 22/07/2026
##################################################################################

import schedule
import time

def DisplayMessage(message):
    print(message)

def main():

    message = input("Enter the message : ")

    schedule.every(5).seconds.do(DisplayMessage, message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    
##################################################################################
## Output:
## Enter the message : Keep Coding..   
## Keep Coding..
## Keep Coding..
## Keep Coding..
## Keep Coding..
##################################################################################