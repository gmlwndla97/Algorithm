import sys

from collections import deque
n=int(sys.stdin.readline().rstrip())
answer=deque()
for i in range(1, n+1):
    answer.append(i)

while True:
    if len(answer)==1:
        print(answer[0])
        break
    else:
        ##1.맨앞 버리기
        answer.popleft()
        ##2.맨앞 맨뒤로
        temp=answer[0]
        answer.popleft()
        answer.append(temp)


