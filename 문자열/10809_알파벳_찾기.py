s = input()

for i in range(97, 123):
    where = -1
    for j in range(len(s)):
        if chr(i) == s[j]:
            where = j
            break
    print(where, end = ' ')
