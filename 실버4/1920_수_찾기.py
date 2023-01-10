import sys
input = sys.stdin.readline

N = int(input())
Ali = set(map(int, input().split()))
M = int(input())
Xli = list(map(int, input().split()))
for i in Xli:
    print(int(i in Ali))
