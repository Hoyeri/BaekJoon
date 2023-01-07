import sys
input = sys.stdin.readline


def isprime(x):
    if x == 1:
        return False
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

pli = []
for i in range(2, 2*123456+1):
    if isprime(i):
        pli.append(i)
        
while True:
    cnt = 0
    n = int(input())
    if n == 0:
        break
    for i in pli:
        if n < i <= 2*n:
            cnt += 1
    print(cnt)
