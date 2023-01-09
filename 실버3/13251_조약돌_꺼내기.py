from math import comb
import sys
input = sys.stdin.readline

m = int(input())
incolor = list(map(int, input().split()))
k = int(input())

up = 0
for i in incolor:
    up += comb(i, k)
print(up / comb(sum(incolor), k))
