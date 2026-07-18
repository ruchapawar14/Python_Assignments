##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 27
##  Question    : 1
##  Date        : 15/07/2026
##################################################################################

class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author 
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {BookStore.NoOfBooks}")

Bobj1 = BookStore("Linux System Programmimg", "Robert Love")
Bobj1.Display()

Bobj2 = BookStore("C Programming", "Dennis Ritchie")
Bobj2.Display()

Bobj3 = BookStore("Python Programmimg", "Guido van Rossum")
Bobj3.Display()

##################################################################################
## Output:
## Linux System Programmimg by Robert Love. No of books : 1
## C Programming by Dennis Ritchie. No of books : 2
## Python Programmimg by Guido van Rossum. No of books : 3
##################################################################################