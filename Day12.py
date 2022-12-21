import aocd
from collections import deque
from math import inf as INFINITY

# instructions = aocd.get_data(year=2022, day=12).split('\n')
# This is being shamelessly stolen from:
# https://github.com/mebeim/aoc/blob/master/2022/README.md#day-12---hill-climbing-algorithm
# What this does is automatically make a < b < c < d < ... < z, etc, because of the binary read. 
with open('Day12_data.txt', 'rb') as fin:
    lines = fin.read().splitlines()
    grid = list(map(list, lines))

# This is a breadth first search (bfs)
# The below function is vanilla, same for any other problem like this
# The difference arises from the get_neighbors function.
def bfs(grid, src, dst):
    '''
    grid -- list[list[]] of values of height
    src -- starting coordinate, S
    dst -- destination coordinate, E
    '''
    h, w    = len(grid), len(grid[0]) # pre-calculate height and width for simplicity
    queue   = deque([(0, src)])       # queue of tuples (distance_from_src, coords)
    visited = set()

    # While there are coordinates to visit
    while queue:
        print(queue)
        # Get the first one in the queue
        distance, rc = queue.popleft()
        # If we reached the desination, return the distance traveled so far
        if rc == dst:
            return distance

        # Skip already vsited coordinates
        if rc not in visited:
            visited.add(rc)

            # For each neighboring cell that wasn't already visited
            for n in get_neighbors(grid, rc[0], rc[1], h, w):
                if n in visited:
                    continue

                # Add it to the back of the queue with a distance equal to the
                # current one plus 1
                queue.append((distance + 1, n))

    return INFINITY

# The get neighbors function will use YIELD to return valid neighboard (current height + 1)
def get_neighbors(grid, r, c, h, w): # get h, w as parameters for simplicity
    # r - row, c - column, h - height of grid, w - width of grid
    max_el = int(grid[r][c]) + 1
    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
        if 0 <= nr < h and 0 <= nc < w: # ensure we are within the grid
            if grid[nr][nc] <= max_el:  # ensure this neighbor is reachable
                print(nr, nc, r, c)
                yield nr, nc

# These will all be ints since iterating bytes yields ints
# Since we are operating in byte space, we need to know the values of start, end, etc.
START, END, LOWEST, HIGHEST = b'SEaz'
src = dst = None

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == START:
            src = r, c
            grid[r][c] = LOWEST
        elif cell == END:
            dst = r, c
            grid[r][c] = HIGHEST

    if src and dst:
        break

# min_dist = bfs(grid, src, dst)
print('Part 1:', min_dist)

