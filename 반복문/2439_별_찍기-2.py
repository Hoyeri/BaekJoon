n = int(input())

for i in reversed(range(n)):
    for j in range(i):
        print(' ', end = '')
    for k in range(n-i-1):
        print('*', end = '')
    print('*')
