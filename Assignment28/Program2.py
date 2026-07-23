##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 28
##  Question    : 2
##  Date        : 23/07/2026
##################################################################################

def CountWords(filename):
    fd =  open(filename, "r")

    data = fd.read()
    words = data.split()

    fd.close()

    return len(words)

def main():
    Name = input("Enter the file name : ")

    Result = CountWords(Name)

    print(f"The total number of words in {Name} are : {Result}")

if __name__ == "__main__":
    main()

##################################################################################
## Output:
## Enter the file name : Demo.txt
## The total number of words in Demo.txt are : 8
##################################################################################