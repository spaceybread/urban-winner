from collections import Counter

f = open("input.txt")
s = f.read().strip()

visited = set()
pos1 = [0, 0]
pos2 = [0, 0]

i = 0
for c in s:
    if i % 2 == 0: pos = pos1
    else: pos = pos2

    visited.add( (pos[0], pos[1]) )
    
    if c == "^": pos[1] += 1
    if c == "v": pos[1] -= 1
    if c == ">": pos[0] += 1
    if c == "<": pos[0] -= 1
    i += 1

print(len(visited))

