import sys
n=int(sys.stdin.readline().rstrip())
num=1
count=0
while(True):
    if('666' in str(num)):
       count+=1
       if(count==n):
           print(num)
           break

    num+=1
