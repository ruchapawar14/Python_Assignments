###############################################################
##  Author     : Rucha Hanumant Pawar
##  Assignment : 4
##  Question   : 3
##  Date       : 22/06/2026
###############################################################
lst = [10,20,30]
tpl = (10,20,30)

lst[0] = 100
tpl[0] = 100

###############################################################
## Output :
## TypeError: 'tuple' object does not support item assignment
## Explanation :
## The statement lst[0] = 100 executes successfully
## because lists are mutable and their elements can be changed.
## The statement tpl[0] = 100 raises a TypeError because
## tuples are immutable and their elements cannot be modified.
###############################################################