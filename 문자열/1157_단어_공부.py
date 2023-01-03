diff = ord('a') - ord('A') # 대문자에 diff를 더하면 소문자
s = input()
countlist = [0 for i in range(150)]

for i in range(len(s)):
    if ord(s[i]) < ord('a'): # 대문자
        countlist[ord(s[i])] += 1
    else: #소문자
        countlist[ord(s[i]) - diff] += 1

count = 0
for i in countlist:
    if i == max(countlist):
        count += 1
        
if count > 1:
    print('?')
else:
    print(chr(countlist.index(max(countlist))))
