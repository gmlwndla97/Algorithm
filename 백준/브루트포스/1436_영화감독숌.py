import sys
n=int(sys.stdin.readline().rstrip())
cnt=0
num=0
while(True):
    str_num=str(num)
    if '666' in str_num:
        cnt+=1
    if cnt==n:
        print(str_num)
        break
    else:
        num+=1