import sys
a=int(sys.stdin.readline().rstrip())
b=int(sys.stdin.readline().rstrip())
c=int(sys.stdin.readline().rstrip())

result=str(a*b*c)
num=[0]*10
for i in range(0, len(result)):
    num[int(result[i])]+=1

for j in num:
    print(j)