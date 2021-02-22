import sys
n=int(sys.stdin.readline().rstrip())
tree=[0]*(n+1)
def previous(start):
    if(start==-19):
        return
    print(chr(start+65), end='')
    previous(tree[start][0])
    previous(tree[start][1])
    return


def mid(start):
    if(start==-19):
        return
    mid(tree[start][0])
    print(chr(start + 65), end='')
    mid(tree[start][1])
    return


def post(start):
    if(start==-19):
        return

    post(tree[start][0])
    post(tree[start][1])
    print(chr(start + 65), end='')
    return

for _ in range(0, n):
    root, left, right=sys.stdin.readline().rstrip().split()
    root=int(ord(root)-65)
    left=int(ord(left)-65)
    right=int(ord(right)-65)
    tree[root]=((left, right))
#
# for i in range(0, n):
#     print(tree[i][0], tree[i][1])

previous(0)
print()
mid(0)
print()
post(0)