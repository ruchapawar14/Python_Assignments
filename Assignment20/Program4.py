##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 20
##  Question    : 4
##  Description : It is used to create three threads that count and display the
##                number of lowercase letters, uppercase letters, and digits
##                in a string.
##  Date        : 07/07/2026
##################################################################################

import threading

def Small(Name):
    print("TID of Small thread is : ",threading.get_ident())
    print("Name of thread is : ",threading.current_thread().name)
    Count = 0
    for ch in Name:
        if('a' <= ch <= 'z'):
            Count = Count + 1
    print("The number of lower case letters are : ",Count)

def Capital(Name):
    print("TID of Capital thread is : ",threading.get_ident())
    print("Name of thread is : ",threading.current_thread().name)
    Count = 0
    for ch in Name:
        if('A' <= ch <= 'Z'):
            Count = Count + 1
    print("The number of upper case letters are : ",Count)

def Digits(Name):
    print("TID of Numeric thread is : ",threading.get_ident())
    print("Name of thread is : ",threading.current_thread().name)
    Count = 0
    for ch in Name:
        if('0' <= ch <= '9'):
            Count = Count + 1
    print("The number of digits are : ",Count)

def main():
    String = input("Enter a string : ")

    t1 = threading.Thread(target=Small, args=(String,))
    t1.start()

    t2 = threading.Thread(target=Capital, args=(String,))
    t2.start()

    t3 = threading.Thread(target=Digits, args=(String,))
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()


##################################################################################
## Output:
## Enter a string : RuchaPawar1402
## TID of Small thread is :  6142472192
## Name of thread is :  Thread-1 (Small)
## The number of lower case letters are :  8
## TID of Capital thread is :  6159298560
## Name of thread is :  Thread-2 (Capital)
## The number of upper case letters are :  2
## TID of Numeric thread is :  6176124928
## Name of thread is :  Thread-3 (Digits)
## The number of digits are :  4
##################################################################################