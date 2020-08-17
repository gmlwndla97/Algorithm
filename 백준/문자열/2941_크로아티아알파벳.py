import sys

alpha=['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string=sys.stdin.readline().rstrip()
sum=0
for j in range(0, len(alpha)):
    if string.find((alpha[j]))!=-1: #있을 떄
        string=string.replace(alpha[j],'a') #그냥 a로 바꿔줌

print(len(string))