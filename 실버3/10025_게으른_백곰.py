import sys

input = sys.stdin.readline
n, k = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
last = 0
for i in li:
    if last < i[1]:
        last = i[1]
next_ = 2 * k + 1
woori = [0] * 1000001
for i in li:
    woori[i[1]] = i[0]
window = sum(woori[:next_])
ans = window
for i in range(next_, last+1):
    window += woori[i] - woori[i-next_]
    ans = max(ans, window)
print(ans)
