import sys
n, k=map(int, sys.stdin.readline().rstrip().split())
answer=[]
temp=[]
for i in range(0, n):
    answer.append(i+1)

num=0
for i in range(0, n):
    num += k-1
    if num>=len(answer):
        num= num%len(answer)
    temp.append(str(answer.pop(num)))
print("<",", ".join(temp)[:], ">", sep='')