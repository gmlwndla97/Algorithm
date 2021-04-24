import sys
from collections import deque
n, k=map(int, sys.stdin.readline().rstrip().split())
naegu=list(map(int, sys.stdin.readline().rstrip().split()))
convey=[False]*(2*n)
stage=0
def rotate():
    edge=naegu.pop()
    naegu.insert(0, edge)

    edge=convey.pop()
    convey.insert(0, edge)
    convey[n-1]=False


def move():
    for i in range(n-2, -1, -1):
        if(i!=n-1 and convey[i+1]==False and naegu[i+1]>0
        and convey[i]==True): #지금 있어야만 이동시키는 것
            convey[i]=False
            convey[i+1]=True
            naegu[i+1]-=1
    convey[n-1]=False

def put_robot():
    if(naegu[0]>0):
        convey[0]=True
        naegu[0]-=1

while(True):
    stage+=1
    rotate()
    move()
    put_robot()
    cnt=0
    for i in naegu:
        if i==0:
            cnt+=1
    if(cnt>=k):
        print(stage)
        break
