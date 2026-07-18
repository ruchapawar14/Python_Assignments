##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 27
##  Question    : 2
##  Date        : 15/07/2026
##################################################################################

class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"The name of account holder is : {self.Name}")
        print(f"The current balance is : {self.Amount}")

    def Deposit(self,deposit):
        self.Amount = self.Amount + deposit
        print(f"{deposit} deposited Successfully")
        print(f"Current Balance : {self.Amount}")

    def Withdraw(self,amount):

        if(self.Amount >= amount):
            self.Amount = self.Amount - amount
            print(f"{amount} withdrawn Successfully")
            print(f"Current Balance : {self.Amount}")


        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        self.Interest = (self.Amount * BankAccount.ROI) / 100
        return self.Interest

bobj1 =  BankAccount("Rucha",15000)
bobj1.Display()

bobj1.Deposit(1500)
bobj1.Withdraw(1000)
print(f"Interest : {bobj1.CalculateInterest():.2f}")
print()

bobj2 =  BankAccount("Priya",3000)
bobj2.Display()
bobj2.Deposit(700)
bobj2.Withdraw(4000)
print(f"Interest : {bobj2.CalculateInterest():.2f}")


##################################################################################
## Output:
## The name of account holder is : Rucha
## The current balance is : 15000
## 1500 deposited Successfully
## Current Balance : 16500
## 1000 withdrawn Successfully
## Current Balance : 15500
## Interest : 1627.50
## 
## The name of account holder is : Priya
## The current balance is : 3000
## 700 deposited Successfully
## Current Balance : 3700
## Insufficient Balance
## Interest : 388.50
##################################################################################