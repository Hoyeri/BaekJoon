n = int(input())

nlist = list(map(int, input().split()))
a = int(input())
count = 0

for i in nlist:
    if i == a:
        count += 1

print(count)
