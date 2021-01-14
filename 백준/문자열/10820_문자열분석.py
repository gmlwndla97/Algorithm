import sys

while True:
    str=sys.stdin.readline().rstrip('\n')
    lower=0
    upper=0
    num=0
    blank=0
    if not str: #######EOF 처리방법
        break
    for i in str:
        if (i.islower()):
            lower += 1
        elif (i.isupper()):
            upper += 1
        elif (i.isdigit()):
            num += 1
        elif (i.isspace()):
            blank += 1
        # if(int(ord(i))>=97 and int(ord(i))<=122):
        #     lower+=1
        # elif (int(ord(i))>=65 and int(ord(i))<=90):
        #     upper+=1
        # elif(int(ord(i))>=48 and int(ord(i))<=57):
        #     num+=1
        # elif(int(ord(i))==32):
        #     blank+=1
    print(lower, upper, num, blank)

