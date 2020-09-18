import sys
n, k=map(int, sys.stdin.readline().rstrip().split())
answer=[]
for i in range(1, n+1):
    answer.append(i)

def resize(now, len):
    while now <= len:
        if now<0:
            now+=len
            break

    return now

now=k-1
result=[]
for i in range(0, n):
    print(now)
 #   print(answer[now])
    result.append(answer[now])
    answer.remove(answer[now])

    now=now+k-1
    if now>len(answer):
        now=resize(now, len(answer))


print(result)