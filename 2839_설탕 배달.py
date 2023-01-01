n = int(input())
i = 0
li = []

while  True:
     k = (n - (5*i))%3
     if k == 0:
          na = i + (n - (5*i))//3
          li.append(na)
     i += 1
     if n-(5*i) == 0:
          li.append(i)
          break
     elif n-(5*i) < 0:
          break
          
if li == []:
     print("-1")
else:
     print(min(li))
