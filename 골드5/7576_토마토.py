import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
sch = deque()  # deque의 선언 위치


def bfs():
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    while sch:
        y, x = sch.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if box[ny][nx] == 0:
                    box[ny][nx] = box[y][x] + 1
                    sch.append((ny, nx))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            sch.append((i, j))
bfs()
maxa = 0
for i in box:
    a = max(i)
    if a > maxa:
        maxa = a
for i in box:
    if 0 in i:
        print(-1)
        sys.exit()
print(maxa - 1)
