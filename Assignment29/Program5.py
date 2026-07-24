##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 29
##  Question    : 5
##  Date        : 23/07/2026
##################################################################################
import sys

def ChkFrequency(FileName, Word):
    fobj = open(FileName, "r")

    Data = fobj.read()

    fobj.close()

    Count = Data.count(Word)

    print(f"{Word} appears {Count} times in {FileName}")

def main():
    ChkFrequency(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()
##################################################################################
## Input :
## python3 program5.py  Demo.txt Marvellous
## Output:
## Marvellous appears 0 times in Demo.txt
##################################################################################
