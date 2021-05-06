import sys
number=sys.stdin.readline().rstrip()
mid=len(number)//2
min=987654321
setArr=[]
if(len(number)==1):
    print(1)
for i in range(1, mid+1):
    arr = []
    ans=''
    for j in range(0, len(number), i):
        temp=number[j:j+i]
        arr.append(temp)
    count=1
    for j in range(0, len(arr)-1):
        prev=arr[j]
        next=arr[j+1]
       # count=0
        if(prev!=next):
            if(count==1):
                ans+=prev
            else:
                ans+=str(count)
                ans+=prev
                count=1
        else:
         #   print("같다")
            count+=1
    if (count == 1):
        ans += arr[len(arr)-1]
    else:
        ans+=str(count)
        ans+=arr[len(arr)-1]
 #   print(ans)
    if(len(ans)<min):
        min=len(ans)

print(min)