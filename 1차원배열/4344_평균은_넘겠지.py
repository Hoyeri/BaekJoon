c = int(input())

for i in range(c):
    score = list(map(int, input().split()))
    ave = (sum(score) - score[0]) / score[0]
    count = 0
    for j in range(1, score[0] + 1):
        if score[j] > ave:
            count += 1
    print("%.3f%%" %(count/score[0]*100))
