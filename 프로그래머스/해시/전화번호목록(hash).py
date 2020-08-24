# phone_book=["119", "97674223", "1195524421"]
phone_book=["12","123","1235","567","88"]
map={}
for i in phone_book:
    map[i]=1

for phone in map.keys():
    temp=""
    for idx in range(0, len(phone)):
        temp+=phone[idx]
        if temp in map and temp!=phone:
            print('False')

print('True')
