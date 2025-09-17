from collections import Counter

f = open("input.txt")
s = f.read().strip()

visited = set()
pos = [0, 0]

for c in s: 
    visited.add( (pos[0], pos[1]) )
    
    if c == "^": pos[1] += 1
    if c == "v": pos[1] -= 1
    if c == ">": pos[0] += 1
    if c == "<": pos[0] -= 1

print(len(visited))

