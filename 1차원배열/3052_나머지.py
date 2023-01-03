namuzi = []

for i in range(10):
    x = int(input())
    namuzi.append(x % 42)

case = []
for i in namuzi:
    if i not in case:
        case.append(i)

print(len(case))
