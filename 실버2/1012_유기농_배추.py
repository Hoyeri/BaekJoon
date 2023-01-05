import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def bfs(y, x):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    sch = deque()
    sch.append((y, x))
    while sch:
        y, x = sch.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if bat[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    sch.append((ny, nx))

for i in range(t):
    m, n, k = map(int, input().split())
    bat = [[0] * m for _ in range(n)]
    chk = [[False] * m for _ in range(n)]
    cnt = 0
    for j in range(k):
        x, y = map(int, input().split())
        bat[y][x] = 1
    for k in range(n):
        for l in range(m):
            if bat[k][l] == 1 and chk[k][l] == False:
                chk[k][l] = True
                bfs(k, l)
                cnt += 1

    print(cnt)
