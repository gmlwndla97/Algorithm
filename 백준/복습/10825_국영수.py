import sys
n=int(input())
answer=[]
for _ in range(n):
    name, a, b, c=sys.stdin.readline().rstrip().split()
    answer.append((int(a), int(b), int(c), name))

answer.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))

for i in range(n):
    print(answer[i][3])