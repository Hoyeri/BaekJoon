a = int(input()) # a is int, 1
b = list(input()) # b is str, 2
b.reverse()
result = 0
for i in range(3):
    print(a * int(b[i]))
    result += a * int(b[i]) * (10**i)
print(result)
