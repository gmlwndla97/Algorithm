participant=["leo","kiki","eden"]
completion=["eden","kiki"]

dic = {}
for i in participant:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]+=1

for j in completion:
    if j in dic.keys():
        dic[j]-=1


for i in dic:
    if dic.get(i)>0:
        print(i)