##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 30
##  Question    : 4
##  Date        : 22/07/2026
##################################################################################
import time
import schedule

def Display():
    print("Namskar..")

def main():
    schedule.every().day.at("09:00").do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    
