a, b = input().split()
a_ = []
b_ = []

for i in reversed(range(3)):
    a_.append(a[i])
    b_.append(b[i])

a_ = int(''.join(a_))
b_ = int(''.join(b_))

print(max(a_, b_))
