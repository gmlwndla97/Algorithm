import sys
n=int(sys.stdin.readline().rstrip())
arr=list( sys.stdin.readline().rstrip().split() for _ in range(n))
for i in range(0, n):
    arr[i][1]=int(arr[i][1])
    arr[i][2] = int(arr[i][2])
    arr[i][3] = int(arr[i][3])

sortedArr=sorted(arr, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(0, n):
    print(sortedArr[i][0])