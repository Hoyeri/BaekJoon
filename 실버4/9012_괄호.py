import sys
input = sys.stdin.readline


def isvps(li):
    cnt = 1
    k = 0
    while li:
        if li[k] == '(' and li[k+1] == ')':
            [li.pop(k) for _ in range(2)]
            cnt += 1
        else:
            k += 1
        if k+1 >= len(li):
            k = 0
            if not cnt or len(li) == 1:
              return "NO"
            cnt = 0
    return "YES"


T = int(input())
for i in range(T):
    chk = [False] * T
    s = list(input())
    s.pop()
    print(isvps(s))
