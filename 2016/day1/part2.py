
ins = input().split(", ")

pos = [0, 0]
dir = 0 # N, E, S, W

visited = set()
visited.add((pos[0], pos[1]))
first_repeat_found = False

for x in ins:
    turn_dir = x[0]
    change = int(x[1:])

    if turn_dir == 'L': dir = (dir + 3) % 4
    else: dir = (dir + 1) % 4

    for _ in range(change):
        if dir == 0: pos[1] += 1
        elif dir == 2: pos[1] -= 1
        elif dir == 1: pos[0] += 1
        elif dir == 3: pos[0] -= 1

        if not first_repeat_found:
            if (pos[0], pos[1]) in visited:
                print("P2:", abs(pos[0]) + abs(pos[1]))
                first_repeat_found = True
            visited.add((pos[0], pos[1]))

print(abs(pos[0]) + abs(pos[1]))

