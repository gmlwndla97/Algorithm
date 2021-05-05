import sys
ans=sys.stdin.readline().rstrip()
alpha=[]
num=[]
for i in ans:
    if(i.isalpha()==True):
        alpha.append(i)
    elif(i.isdigit()==True):
        num.append(int(i))

result=[]
alpha.sort()
for i in alpha:
    result.append(i)
result.append(sum(num))

for i in result:
    print(i, end='')