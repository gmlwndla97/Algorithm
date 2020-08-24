import sys
t=int(sys.stdin.readline().rstrip())
answer='YES'
for i in range(0, t):
    answer='YES'
    phone_book = []
    n = int(sys.stdin.readline().rstrip())
    for k in range(0, n):
        phone = sys.stdin.readline().rstrip()
        phone_book.append(phone)

    map={}
    for i in phone_book:
        map[i]=1

    for phone in map.keys():
        temp=""
        for idx in range(0, len(phone)):
            temp+=phone[idx]
            if temp in map and temp!=phone:
                answer='NO'

    print(answer)
