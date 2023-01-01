spots = list(map(int, input().split()))
count = 0
counts = []

for i in range(3):
    for j in spots:
        if spots[i] == j:
            count += 1 # min 1, max 3
    counts.append(count)
    count = 0

if max(counts) == 3:
    reward = 10000 + spots[0]*1000
elif max(counts) == 2:
    reward = 1000 + spots[counts.index(2)]*100
else:
    reward = max(spots) * 100

print(reward)
