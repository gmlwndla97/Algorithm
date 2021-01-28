import sys
from string import ascii_lowercase
from string import ascii_uppercase

upper=list(ascii_uppercase)
lower=list(ascii_lowercase)
str=sys.stdin.readline().rstrip()

answer=''
for i in str:
    if i!=' ':
        if i.isalpha():
            if i.isupper():
                index=ord(i)-65
                index+=13
                if index == 0: answer += upper[0]
                else:
                    index = index % 26
                    answer += (upper[index])

            elif i.islower():
                index = ord(i) - 97
                index += 13
                if index == 0:
                    answer += lower[0]
                else:
                    index = index % 26
                    answer += (lower[index])
        else: #숫자인경우
            answer+=(i)
    else:
        answer+=(' ')

print(answer)