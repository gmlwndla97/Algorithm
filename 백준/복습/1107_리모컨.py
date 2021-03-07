import sys
n=int(input())
m=int(input())
if m!=0:
    mal=list(map(int, sys.stdin.readline().rstrip().split()))
else:
    mal=[]

minval=abs(100-n)
high=n
low=n
num=0
if m==10:
    print(minval)
    sys.exit(0)
while(True):
    high=n+num
    low=n-num
    if(low<0):
        low=0
    #print(high,low)
    highflag=False
    lowflag=False
    sthigh=str(high)
    stlow=str(low)
    for j in range(0, len(sthigh)):
        if int(sthigh[j]) in mal:
            highflag=True
            break
    for j in range(0, len(stlow)):
        if int(stlow[j]) in mal:
            lowflag=True
            break
    #print(high, low)
    if highflag==False and lowflag==True:
        #high만 버튼 다 누를 수 있는 경우
        minval=min(minval, abs(high-n)+len(sthigh))
        break
    elif highflag==True and lowflag==False:
        minval = min(minval, abs(low - n) + len(stlow))
        break
    elif highflag==False and lowflag==False:
      #  print(high, low )
        temphigh = min(minval, abs(high - n) + len(sthigh))
        templow=min(minval, abs(low - n) + len(stlow))
        minval=min(temphigh, templow)
        break
    num+=1
print(minval)
