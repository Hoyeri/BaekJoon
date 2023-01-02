def ishansu(n):
    if n >= 100:
        nlist = list(map(int, str(n)))
        if (nlist[0]-nlist[1]) == (nlist[1]-nlist[2]):
            return True
        else:
            return False
    else:
        return True

n = int(input())
c = 0
for i in range(1, n+1):
    if ishansu(i) == True:
        c += 1

print(c)
