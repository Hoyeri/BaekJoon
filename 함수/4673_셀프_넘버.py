def d(n):
    nlist = list(map(int, str(n)))
    n += sum(nlist)
    return n

n = 0
notself = [0 for i in range(10000)]
while True:
    n += 1
    if d(n) <= 10000:
        notself[d(n)-1] = 1
    if n > 10000:
        break
    
for i in range(10000):
    if notself[i] == 0:
        print(i + 1)
