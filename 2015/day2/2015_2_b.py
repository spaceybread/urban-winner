from collections import Counter



f = open("input.txt")
s = f.read().strip().split("\n")

total = 0
for l in s:
    vals = [int(v) for v in l.split("x")]
    
    sides = [vals[0] + vals[1], vals[1] + vals[2], vals[2] + vals[0]]
    vol = vals[0] * vals[1] * vals[2]

    total += 2 * min(sides) + vol

print(total)



