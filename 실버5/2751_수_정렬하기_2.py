import sys
input = sys.stdin.readline

n = int(input())
nli = [int(input()) for _ in range(n)]
nli.sort()
for i in nli:
    print(i)
