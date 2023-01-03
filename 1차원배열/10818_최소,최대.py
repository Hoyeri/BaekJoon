n = int(input())
a = list(map(int, input().split()))
min = max = a[0]

for i in a:
    if i < min:
        min = i
    if i > max:
        max = i

print(min, max)
