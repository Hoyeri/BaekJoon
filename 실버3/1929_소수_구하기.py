import sys
input = sys.stdin.readline

def isprime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

M, N = map(int, input().split())

prime = []
for i in range(M, N+1):
    if isprime(i):
        prime.append(i)

for i in prime:
    print(i)
