from collections import Counter

f = open("input.txt")
s = f.read().strip()

c = 0
for i in range(len(s)):
    x = s[i]

    if x == '(': c += 1
    elif x == ')': c -= 1
    
    if c < 0: 
        print(i)
        break
