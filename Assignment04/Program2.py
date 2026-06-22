####################################################################
##  Author     : Rucha Hanumant Pawar
##  Assignment : 4
##  Question   : 5
##  Date       : 22/06/2026
####################################################################
s = "Python"
print(id(s))

s = s + "3"
print(id(s))

####################################################################
## Output :
## 1570078785376
## 1570079330000
## Explanation :
## The id of s changes because strings are immutable in Python.
## The statement s = s + "3" creates a new string object "Python3"
## and stores it in s. Therefore, the memory address changes.
####################################################################