n = int(input())
count = 0

for i in range(n):
    used = []
    word = input()
    c = 0
    used.append(word[0])
    for j in range(1, len(word)):
        if word[j] != word[j - 1]:
            if word[j] in used:
                c += 1
        if word[j] not in used:
            used.append(word[j])
    if c == 0:
        count += 1

print(count)
