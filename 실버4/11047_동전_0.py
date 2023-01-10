n = input()
n = n.split()
money = int(n[1])
n = int(n[0])
li = []
for i in range(n):
     won = int(input())
     li.append(won)
li.sort(reverse=True)
c = 0

num = 0
while True:
     num += money//li[c]
     money = money%li[c]
     c += 1
     if money < min(li):
          break
print(num)
