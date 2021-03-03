import sys
n=int(sys.stdin.readline().rstrip())
num=1
cnt=0
flag=False
while(num<=n):
    str_num=str(num)
    prev_diff=0
    now_diff=0
    if len(str_num)<=2:
     #   print(num)
        cnt+=1

    else:
        prev_diff=int(str_num[0])-int(str_num[1])
        for i in range(1, len(str_num)-1):
            now_diff=int(str_num[i])-int(str_num[i+1])
            if(now_diff!=prev_diff):
                flag=True
                break
            flag=False
        if flag==False:
            cnt+=1
        prev_diff=0
        now_diff=0
        flag=False
    num+=1

print(cnt)

