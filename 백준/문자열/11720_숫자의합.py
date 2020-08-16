import sys
sum=0
n=int(sys.stdin.readline().rstrip())
list=sys.stdin.readline().rstrip()
for i in range(0, n):
    sum += int(list[i])
print(sum)