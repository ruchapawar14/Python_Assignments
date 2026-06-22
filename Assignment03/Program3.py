########################################################
##  Author     : Rucha Hanumant Pawar
##  Assignment : 3
##  Question   : 3
##  Date       : 22/06/2026
########################################################

def fun():
    x = 10
    print(x)

fun()
print(x)

########################################################
## Output :
## NameError: name 'x' is not defined
## Explanation :
## The variable x is a local variable because it is
## declared inside the function fun(). It can be
## accessed only inside the function. Therefore,
## print(x) outside the function gives a NameError.
########################################################