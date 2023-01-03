n = int(input())
scorelist = list(map(int, input().split()))
newlist = []

for i in scorelist:
    new = i / max(scorelist)*100
    newlist.append(new)

ave = sum(newlist) / n
print(ave)
