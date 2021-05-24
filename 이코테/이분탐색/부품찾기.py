import sys
n=int(sys.stdin.readline().rstrip())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline().rstrip())
find=list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

#이진 탐색 시작

# for target in find:
#     start = 0
#     end = n - 1
#     while(True):
#         if start>=end:
#             print("No")
#             break
#         mid=(start+end)//2
#         if(arr[mid]==target):
#             print("Yes")
#             break
#         elif(arr[mid]>target):
#             end=mid-1
#             continue
#         else:
#             start=mid+1
#             continue
flag=False
for target in find:
    start=0
    end=n-1
    flag=False
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==target):
            print("yes")
            flag=True
            break
        elif(arr[mid]>target):
            end=mid-1
        else:
            start=mid+1
    if(flag==False):
        print("no")
