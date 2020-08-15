import sys
#############백준 런타임에러 해결안됨

def mergesort(array):
    if len(array)<=1:
        return array
    mid=len(array)//2
    left=mergesort(array[:mid])
    right=mergesort(array[mid:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):  # 만약 왼쪽 배열이 남은 상태라면
        for k in range(i, len(left)):
            result.append(left[k])
    elif j < len(left):
        for k in range(i, len(right)):
            result.append(right[k])

    return result


list =[int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]
result=mergesort(list)
for i in result:
    print(i)