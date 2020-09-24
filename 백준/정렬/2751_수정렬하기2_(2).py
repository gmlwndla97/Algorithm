import sys
##quick sort로 정렬 (백준 시간초과 해결 X)
def partition(arr,left, right):
    pivot=arr[left]
    i= left+1
    j= right

    while(i<=j):
        while(i<=right and  arr[i]<=pivot ):
            i=i+1

        while( j>=left+1 and  arr[j]>=pivot):
            j = j - 1


        if(i<=j):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    ##이제 j자리랑 pivot 바꾸기
    temp=arr[j]
    arr[j]=arr[left]
    arr[left]=temp
    return j

def quicksort(arr, left, right):
    if (left<=right):
        pivot=partition(arr,left, right)
        quicksort(arr,left,pivot-1)
        quicksort(arr,pivot+1,right)

    return arr

n=int(sys.stdin.readline().rstrip())
arr=[0]*(n+1)
for i in range(0, n):
    arr[i]=int(sys.stdin.readline().rstrip())

quicksort(arr, 0, n-1)
for i in range(0, n):
    print(arr[i])