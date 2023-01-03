n = int(input())
count = score = 0

for i in range(n):
    result = input()
    for j in range(len(result)):
        if result[j] == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)
    count = score = 0
