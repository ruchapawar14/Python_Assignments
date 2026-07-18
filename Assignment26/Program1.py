##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 26
##  Question    : 1
##  Date        : 15/07/2026
##################################################################################

class Demo:
    Value = 10

    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2

    def Fun(self):
        print("The No1 in Fun is : ",self.No1)
        print("The No2 in Fun is : ",self.No2)

    def Gun(self):
        print("The No1 in Gun is : ",self.No1)
        print("The No1 in Gun is : ",self.No2)

print("Object 1")
dobj1 = Demo(11,21)
dobj1.Fun()
dobj1.Gun()

print("Object 2")
dobj2 = Demo(51,101)
dobj2.Fun()
dobj2.Gun()

##################################################################################
## Output :
## Object 1
## The No1 in Fun is :  11
## The No2 in Fun is :  21
## The No1 in Gun is :  11
## The No1 in Gun is :  21
## Object 2
## The No1 in Fun is :  51
## The No2 in Fun is :  101
## The No1 in Gun is :  51
## The No1 in Gun is :  101
##################################################################################