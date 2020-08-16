import sys
import math

alpha=[2, 3,4,5,6,7,8,9,10]
str=sys.stdin.readline().rstrip()
sum=0
for i in range(0, len(str)):
    if str[i]=='A' or str[i]=='B' or str[i]=='C':
        sum +=3
    elif str[i]=='D' or str[i]=='E' or str[i]=='F':
        sum +=4
    elif str[i]=='G' or str[i]=='H' or str[i]=='I':
        sum +=5
    elif str[i]=='J' or str[i]=='K' or str[i]=='L':
        sum +=6
    elif str[i]=='M' or str[i]=='N' or str[i]=='O':
        sum +=7
    elif str[i]=='P' or str[i]=='Q' or str[i]=='R' or str[i]=='S':
        sum +=8
    elif str[i]=='T' or str[i]=='U' or str[i]=='V':
        sum +=9
    elif str[i]=='W' or str[i]=='X' or str[i]=='Y' or str[i]=='Z':
        sum +=10

print(sum)