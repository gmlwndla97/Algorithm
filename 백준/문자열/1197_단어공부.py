dic={}
string=input()
string=string.upper()
check=''.join(set(string)) #문자열 중복제거
max=0;
count=0;
for i in range(0, len(check)):
        count=string.count(check[i])
        dic[check[i]]=count
        if count>max:
            max=count
        count=0

sorted(dic.items(), key=lambda x:x[1], reverse=True) #value값 기준으로 내림차순 정렬
rev={v:k for k, v in dic.items()}  #key, value 순서 반대로 한 dictionary
#print(dic)
duplicatenum=0
for k in dic.values():
    if k==max:
        duplicatenum=duplicatenum+1

if duplicatenum>1:
    print('?')
else:
    print(rev.get(max))





