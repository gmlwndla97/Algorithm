import sys
n=int(input())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

target=1 #만들고자하는 금액
count=arr[0] #1원부터 시작
for i in arr:
    if(target<i):
        #만들 수 없음.
        break
    else:
        #만들 수 있는데.
        #다음 타겟은 이번 돈을 더한 값으로 갱신한다.
        #왜냐면 더한애 까지 만들수 있거든.
        target+=i
print(target)