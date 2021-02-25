import sys
e, s, m=map(int, sys.stdin.readline().rstrip().split())
min=min(e, s, m)
num=1
while(True):
    if((num-e)%15 ==0 and (num-s)%28==0 and (num-m)%19==0):
        print(num)
        break
    else:
        num+=1
