a, b = input().split()
a_ = []
b_ = []

for i in reversed(range(3)):
    a_.append(a[i])
    b_.append(b[i])

print(''.join(max(a_, b_)))
