n = int(input())
li = []
for i in range(n):
    weight = int(input())
    li.append(weight)
li.sort()
real = []
for i in range(n):
    k = li[i]*(n-i)
    real.append(k)
print(max(real))
