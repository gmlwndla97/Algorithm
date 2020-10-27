import sys

input=int(sys.stdin.readline().rstrip())
answer=0
for i in range(1, input+1):
    if(i>=1 and i<=10):
        answer+=1
    else:
        stringNum = str(i)
        diff = int(stringNum[0]) - int(stringNum[1])
        flag = False
        for i in range(1, len(stringNum) - 1):
            if (int(stringNum[i]) - int(stringNum[i + 1])) != diff:
                flag = True
        if (flag == False):
            answer += 1

print(answer)
