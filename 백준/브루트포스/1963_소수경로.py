import sys
import math
from collections import deque
q=deque()
array=[True]*10001
dist=[0]*10001
visit=[0]*10001
flag=False

for i in range(2, int(math.sqrt(10000)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= 10000:
            array[i * j] = False
            j += 1

prime=[]
for i in range(1000, 10000):
    if array[i]:
        prime.append(i)

t=int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    x, y=map(int, sys.stdin.readline().rstrip().split())
    q.append((x, 0))
    visit[x]=1
    while(q):
        now=q[0][0]
        nowcnt=q[0][1]
        q.popleft()
        if now==y:
            print(nowcnt)
            flag=True
            break
        strnum=str(now)
        for i in range(0, 4):
            for j in range(0, 10):
                if i==0 and j==0: continue
                temp=strnum[0:i] + str(j) + strnum[i+1:4]
                num=int(temp)
                #print(num)
                if num in prime and visit[num]==0:
                    dist[num]+=1
                    #print(num)
                    q.append((num, nowcnt+1))
                    visit[num]=1

    dist = [0] * 10001
    visit = [0] * 10001
    q.clear()
    if(flag==False):
        print("Impossible")
    flag=False
