import sys
n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(0, n):
    x, y=map(int,sys.stdin.readline().rstrip().split(' '))
    arr.append((y,x))

end=sorted(arr, key=lambda x:(x[0], x[1])) #첫번째 인자로 정렬하고, 중복되면 두번째 인자 기준
count=0
#먼저 끝나는 순서대로
now=0
for i in range(0, len(end)):
    if end[i][1]>=now:
        count+=1
        now=end[i][0]

print(count)