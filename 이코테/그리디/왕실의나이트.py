answer=input()
dx=[-1,-2,-2,-1,1,2,2,1]
dy=[-2,-1,1,2,2,1,-1,-2]
col=answer[0]
row=answer[1]
col=ord(answer[0])-97+1

count=0
for i in range(0, 8):
    nx=dx[i]+int(row)
    ny=dy[i]+int(col)
    if(nx>=1 and nx<=8 and ny>=1 and ny<=8):
        count+=1

print(count)
