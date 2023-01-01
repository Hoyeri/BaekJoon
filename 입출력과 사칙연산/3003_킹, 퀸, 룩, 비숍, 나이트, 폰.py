chess = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split()))
for i in range(5):
    print(chess[i] - white[i], end = ' ')
print(chess[-1] - white[-1])
