import sys
#############백준 시간초과 해결안됨
n = int(input())
list = []
min = 987654321
for i in range(0, n):
    x = int(input())
    list.append(x)

index = 0
for i in range(0, n - 1):
    for j in range(i, n):
        if list[j] < min:
            min = list[j]
            index = j
    temp = list[i]
    list[i] = min
    list[index] = temp
    min = 987654321

for i in list:
    print(i)