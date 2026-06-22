####################################################################
##  Author     : Rucha Hanumant Pawar
##  Assignment : 5
##  Question   : 4
##  Date       : 22/06/2026
####################################################################
ba = bytearray([65,66,67])
ba[0] = 97
print(ba)

####################################################################
## Output :
## bytearray(b'aBC')
## Explanation :
## The bytearray() function creates a mutable sequence of bytes.
## The value at index 0 is changed from 65 ('A') to 97 ('a').
## Therefore, the output becomes bytearray(b'aBC').
####################################################################