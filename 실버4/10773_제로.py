import sys
input = sys.stdin.readline

K = int(input())
nli = []
for i in range(K):
    n = int(input())
    if n == 0:
        nli.pop()
    else:
        nli.append(n)
print(sum(nli))
