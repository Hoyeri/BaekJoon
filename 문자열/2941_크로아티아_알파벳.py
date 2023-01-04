calist = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

s =input()
for i in calist:
    if i in s:
        s= s.replace(i, "0")

print(len(s))
