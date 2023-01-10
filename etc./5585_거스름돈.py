paid = int(input())
money = 1000 - paid
coin = [500,100,50,10,5,1]
num = 0
i = 0
while True:
     num += money//coin[i]
     money = money%coin[i]
     i += 1
     if money < 1:
          break
print(num)
