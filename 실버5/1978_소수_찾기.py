import sys
input = sys.stdin.readline

def prime(n):
    for j in range(2, int(i**0.5)+1):
        if n % j == 0:
            return False
    return True

pli = [2]
for i in range(3, 1001):
    if prime(i) == True:
        pli.append(i)

n = int(input())
nli = list(map(int, input().split()))
cnt = 0
for i in nli:
        if i in pli:
            cnt += 1
print(cnt)
