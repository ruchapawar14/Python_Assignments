##################################################################################
##  Author      : Rucha Hanumant Pawar
##  Assignment  : 12
##  Question    : 1
##  Description : It is used to check whether a character is a vowel or a consonant.
##  Date        : 26/06/2026
##################################################################################

def ChkVowel(ch):
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'or 
       ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        
        print(ch, "is a vowel")
    
    else:
        print(ch,"is a consonant")

def main():
    Value = input("Enter an alphabet : ")
    ChkVowel(Value)
    
if __name__ == "__main__":
    main()

##################################################################################
##  Output:
##  Enter a character : a
##  a is a Vowel
##
##  Enter a character : C
##  C is a Consonant
##
##################################################################################