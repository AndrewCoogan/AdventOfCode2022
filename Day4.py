with open('Day4_data.txt') as f:
    lines = [line.strip() for line in f]

grid = []
print(len(lines))

for l in lines:
    e = [r.split('-') for r in l.split(',')]
    grid.append([
        (int(e[0][0]), int(e[0][1])), (int(e[1][0]), int(e[1][1]))
    ])

# Part 1
def func(inp):
    # Left is contained in the right
    if inp[0][0] >= inp[1][0] and inp[0][1] <= inp[1][1]:
        return True
    # Right is contained in the left
    elif inp[1][0] >= inp[0][0] and inp[1][1] <= inp[0][1]:
        return True
    else:
        return False

# Part 2
def func2(inp):
    r1 = set(range(inp[0][0], inp[0][1]+1))
    r2 = set(range(inp[1][0], inp[1][1]+1))

    if r1.intersection(r2):
        return True
    else:
        return False

grid_f = list(filter(func2, grid))
print(len(grid_f))
