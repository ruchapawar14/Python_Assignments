####################################################################
##  Author     : Rucha Hanumant Pawar
##  Assignment : 4
##  Question   : 7
##  Date       : 22/06/2026
####################################################################
d = {1: "One", 1: "ONE", 2: "Two"}
print(d)

####################################################################
## Output :
## {1: 'ONE', 2: 'Two'}
## Explanation :
## Dictionary keys must be unique. When duplicate keys are used,
## the latest value replaces the previous value. Therefore, the
## value "ONE" overwrites "One" for the key 1.
####################################################################