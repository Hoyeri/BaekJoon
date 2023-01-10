import sys
input = sys.stdin.readline


def bfs(p):
    for i in connli[p]:
        if not virus[i]:
            virus[i] = True
            bfs(i)


comp = int(input())
conn = int(input())
connli = [[] for _ in range(comp+1)]
for i in range(conn):
    a, b = map(int, input().split())
    connli[a].append(b)
    connli[b].append(a)
virus = [False] * (comp+1)
virus[1] = True
chk = [False] * (comp+1)
for i in range(comp+1):
    if virus[i] and not chk[i]:
        chk[i] = True
        bfs(i)
print(virus.count(True)-1)
