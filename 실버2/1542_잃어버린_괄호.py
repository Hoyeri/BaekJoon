import sys
input = sys.stdin.readline


def pt(list):
    for i in range(len(list)):
        if list[i] == '-':
            k = i + 1
            while k < len(list):
                if list[k] == '+':
                    list[k] = '-'
                if list[k] == '-':
                    break
                k += 1

s = input()
ns = []
p = []
while s:
    k = len(s)
    if '+' not in s and '-' not in s:
        ns.append(s.strip('\n'))
        break
    for i in range(k):
        if s[i] == '+' or s[i] == '-':
            ns.append(s[:i])
            p.append(s[i])
            s = s[i+1:]
            break
pt(p)
for i in range(len(ns)):
   ns[i] = int(ns[i])
res = []
for i in range(len(p)):
    res.append(str(ns[i]))
    res.append(p[i])
res.append(str(ns[-1]))
print(eval(''.join(res)))
