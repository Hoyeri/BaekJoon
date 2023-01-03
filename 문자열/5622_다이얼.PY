def sec(c):
    if c >= 'W':
        return 10
    elif c >= 'T':
        return 9
    elif c >= 'P':
        return 8
    elif c >= 'M':
        return 7
    elif c >= 'J':
        return 6
    elif c >= 'G':
        return 5
    elif c >= 'D':
        return 4
    else:
        return 3


s = input()
time = 0
for i in range(len(s)):
    time += sec(s[i])

print(time)
