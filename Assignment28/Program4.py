##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 28
##  Question    : 4
##  Date        : 23/07/2026
##################################################################################

def CopyFiles(File1, File2):
    fobj1 = open(File1,"r")
    fobj2 = open(File2,"w")

    data = fobj1.read()

    fobj2.write(data)

    fobj1.close()
    fobj2.close()

    print(f"The contents of {File1} are copied into {File2}")

def main():
    File1 = input("Enter the name of existing file : ")
    File2 = input("Enter the name of new file to copy contents : ")

    CopyFiles(File1,File2)

if __name__ == "__main__":
    main()

