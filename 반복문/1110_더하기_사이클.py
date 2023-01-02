n = int(input())
a = n
count = 0

while True:
    if n < 10:
        n = n*10 + n
        count += 1
    else:
        nlist = list(map(int, str(n)))
        sumlist = list(map(int, str(sum(nlist))))
        n = nlist[-1]*10 + sumlist[-1]
        count += 1
    if n == a:
        break

print(count)
