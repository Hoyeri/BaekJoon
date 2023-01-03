max = int(input())
count = 1

for i in range(8):
    x = int(input())
    if x > max:
        max = x
        count = i + 2

print(max)
print(count)
