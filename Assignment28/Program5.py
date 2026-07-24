##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 28
##  Question    : 5
##  Date        : 23/07/2026
##################################################################################

def SearchWord(FileName, Word):
    fobj = open(FileName, "r")

    Data = fobj.read()

    fobj.close()

    if Word in Data:
        return True
    else:
        return False

def main():
    Name = input("Enter the file name : ")
    Word = input("Enter the word to search : ")

    Result = SearchWord(Name, Word)

    if Result == True:
        print(f"{Word} is present in {Name}")
    else:
        print(f"{Word} is not present in {Name}")

if __name__ == "__main__":
    main()

##################################################################################
## Output:
##  the file name : Demo.txt
## Enter the word to search : Marvellous
## Marvellous is not present in Demo.txt
##
## Enter the file name : Demo.txt
## Enter the word to search : Pune
## Pune is present in Demo.txt
##################################################################################
