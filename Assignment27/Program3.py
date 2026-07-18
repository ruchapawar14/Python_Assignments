##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 27
##  Question    : 3
##  Date        : 15/07/2026
##################################################################################

class Numbers:

    def __init__(self,Value):
        self.Value = Value

    def ChckPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2,self.Value):
            if(self.Value % i == 0):
                return False

        return True

    def ChckPerfect(self):
        sum = 0
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                sum = sum + i 

        if(sum == self.Value):
            return True
        else:
            return False

    def Factors(self):
        print("Factors are : ")
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                print(i) 

    def SumFactors(self):
        sum = 0
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                sum = sum + i

        return sum

obj1 = Numbers(13)

if(obj1.ChckPrime() == True):
    print(obj1.Value,"is a Prime number")
else:
    print(obj1.Value,"is not Prime")    

if(obj1.ChckPerfect() == True):
    print(obj1.Value,"is a Perfect number")
else:
    print(obj1.Value,"is not Perfect")


obj1.Factors()

print("Sum of factors:", obj1.SumFactors())

print()

obj2 = Numbers(6)

if(obj2.ChckPrime() == True):
    print(obj2.Value,"is a Prime number")
else:
    print(obj2.Value,"is not Prime")    

if(obj2.ChckPerfect() == True):
    print(obj2.Value,"is a Perfect number")
else:
    print(obj2.Value,"is not Perfect")

obj2.Factors()

print("Sum of factors:", obj2.SumFactors())   
##################################################################################
## Output:
## 13 is a Prime number
## 13 is not Perfect
## Factors are : 
## 1
## 13
## Sum of factors: 14
##
## 6 is not Prime
## 6 is a Perfect number
## Factors are : 
## 1
## 2
## 3
## 6
## Sum of factors: 12
##################################################################################