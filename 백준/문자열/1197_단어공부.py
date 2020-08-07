dic={}
string=input()
string=string.upper()
check=''.join(set(string))
max=0;
count=0;
for i in range(0, len(check)):
        count=string.count(check[i])
        dic[check[i]]=count
        if count>max:
            max=count
        count=0

sorted(dic.items(), key=lambda x:x[1], reverse=True)
rev={v:k for k, v in dic.items()}
#print(dic)
duplicatenum=0
for k in dic.values():
    if k==max:
        duplicatenum=duplicatenum+1

if duplicatenum>1:
    print('?')
else:
    print(rev.get(max))





