sum_ = int(input())
var = int(input())

for i in range(var):
    cost, n = map(int, input().split())
    sum_ -= (cost * n)

if sum_ == 0:
    print("Yes")
else:
    print("No")
