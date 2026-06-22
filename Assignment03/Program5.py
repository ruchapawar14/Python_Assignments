########################################################
##  Author     : Rucha Hanumant Pawar
##  Assignment : 3
##  Question   : 6
##  Date       : 22/06/2026
########################################################
from sys import getsizeof

def main():
    Value = int(input("Enter the value : ")) 

    print("Data type is : ",type(Value))
    print("Memory address is : ",id(Value))
    print("Size in bytes is : ",getsizeof(Value))

if __name__ == "__main__":
    main()

########################################################
## Output :
## Enter the value : 14
## Data type is : <class 'int'>
## Memory address is : 4322259072
## Size in bytes is : 28
########################################################