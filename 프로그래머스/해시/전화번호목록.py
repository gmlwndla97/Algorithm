import sys
phone_book=["119", "97674223", "1195524421"]
answer='YES'

dic = {}
for phone in phone_book:
    if phone[0] not in dic.keys():
        dic[phone[0]] = [phone]
    else:
        dic[phone[0]].append(phone)

for l in dic.keys():
    if len(dic[l]) > 1:
        for j in range(0, len(dic[l])):
            for k in range(0, len(dic[l])):
                if len(dic[l][j]) < len(dic[l][k]) and dic[l][k][:len(dic[l][j])] == dic[l][j]:
                    answer = 'NO'
                    break


print(answer)