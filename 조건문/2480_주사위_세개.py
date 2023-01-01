score = []
count = 0
eyes = list(map(int, input().split()))

for i in range(3):
    for j in eyes:
        if eyes[i] == j:
            count += 1
    score.append(count)
    count = 0
count = max(score)
i = score.index(count)

if count == 3:
    reward = 10000 + eyes[i]*1000
elif count == 2:
    reward = 1000 + eyes[i]*100
else:
    reward = max(eyes) * 100

print(reward)
