import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(n)]
count = 0
chk = [[False] * m for _ in range(n)]
maxa = 0

def bfs(y, x):
    search = deque()
    search.append((y, x))
    chk[y][x] = True
    area = 1
    dy = [0, 1 , 0, -1]
    dx = [1, 0, -1, 0]
    while True:
        if len(search) == 0:
            return area
        y, x = search.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
               if map_[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    area += 1
                    search.append((ny, nx))

for j in range(n):
    for i in range(m):
        if map_[j][i] == 1 and chk[j][i] == False:
            a = bfs(j, i)
            count += 1
            if maxa < a:
                maxa = a

print(count)
print(maxa)
