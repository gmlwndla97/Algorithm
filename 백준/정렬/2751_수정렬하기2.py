import sys

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:

            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]

        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


def mergesort(array):
    if len(array)<=1:
        return array
    mid=len(array)//2
    left=mergesort(array[:mid])
    right=mergesort(array[mid:])
    return merge(left, right)


n = int(input())
list = []
for i in range(0, n):
    x = int(input())
    list.append(x)
result=mergesort(list)
for i in result:
    print(i)