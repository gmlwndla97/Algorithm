import sys
from collections import deque

q = deque()

begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot","log","cog"]

visit = {string : 0 for string in words}
if target not in words:
    print(0)

else:
    q.append((begin, 0))
    while (q):
        front = str(q[0][0])
        cnt = q[0][1]
        q.popleft()
        if front == target:
            print(cnt)
            break

        for w in words:
            diffcount = 0  # 글자 다른 개수 확인하기
            for i in range(0, len(w)):
                if (str(w[i]) != front[i]):
                    diffcount += 1
            if (diffcount > 1):
                continue
            elif (diffcount == 1):
                visit[w] = 1
                q.append((w, cnt + 1))

