import aocd
import numpy as np
from collections import Counter

instructions = aocd.get_data(year=2022, day=9).split('\n')

def distance(t1 : tuple, t2 : tuple) -> int:
    return np.abs(t1[0] - t2[0]) + np.abs(t1[1] - t2[1])

def in_perimiter(t1 : tuple, t2 : tuple) -> bool:
    x_range = [t1[0] - 1, t1[0], t1[0] + 1]
    y_range = [t1[1] - 1, t1[1], t1[1] + 1]
    if t2[0] in x_range and t2[1] in y_range:
        return True
    return False

def part1():
    head_coordinate = [0,0] # X, Y
    tail_coordinate = [0,0] # X, Y
    positions = Counter()

    for instruction in instructions:
        direc, dist = instruction.split()
        dist = int(dist)  

        for _ in range(dist):
            last_coordinate = head_coordinate.copy()

            if direc == 'L':
                head_coordinate[0] -= 1
            elif direc == 'D':
                head_coordinate[1] -= 1
            elif direc == 'R':
                head_coordinate[0] += 1
            else: # Up
                head_coordinate[1] += 1
            
            if not in_perimiter(head_coordinate, tail_coordinate):
                # This is where we need to update the tail.
                # X axis is the same, moving Y closer
                if head_coordinate[0] == tail_coordinate[0]:
                    if head_coordinate[1] > tail_coordinate[1]:
                        tail_coordinate[1] += 1
                    else:
                        tail_coordinate[1] -= 1
                elif head_coordinate[1] == tail_coordinate[1]:
                    if head_coordinate[0] > tail_coordinate[0]:
                        tail_coordinate[0] += 1
                    else:
                        tail_coordinate[0] -= 1
                else:
                    tail_coordinate = last_coordinate.copy()

            positions[(tail_coordinate[0], tail_coordinate[1])] += 1

    print(f'Part 1: {len(positions)}')

# For part 2, I can just run the first 10 times, updating the inital point.
# No that wont work, do we need to translate this to be a new set of instructions?
# Diagonal instructions dont exist, which makes that not possible.
# 0 will be the head, 9 the tail
knot_locations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
prior_locations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
positions = []

for instruction in instructions:
    direc, dist = instruction.split()
    dist = int(dist)  

    for _ in range(dist):
        #print(knot_locations)
        # We need to do another loop here.
        # As a reminder, the head moved one step a turn, the tail will lag
        prior_locations[0] = knot_locations[0].copy()

        if direc == 'L':
            knot_locations[0][0] -= 1
        elif direc == 'D':
            knot_locations[0][1] -= 1
        elif direc == 'R':
            knot_locations[0][0] += 1
        else: # Up
            knot_locations[0][1] += 1

        for i in range(1,len(knot_locations)):
            prior_locations[i] = knot_locations[i].copy()
            
            if not in_perimiter(knot_locations[i-1], knot_locations[i]):
                # This is where we need to update the tail.
                # X axis is the same, moving Y closer
                if knot_locations[i-1][0] == knot_locations[i][0]:
                    if knot_locations[i-1][1] > knot_locations[i][1]:
                        knot_locations[i][1] += 1
                    else:
                        knot_locations[i][1] -= 1
                elif knot_locations[i-1][1] == knot_locations[i][1]:
                    if knot_locations[i-1][0] > knot_locations[i][0]:
                        knot_locations[i][0] += 1
                    else:
                        knot_locations[i][0] -= 1
                else:
                    knot_locations[i] = prior_locations[i-1]
            
        tail_coordinate_f = (knot_locations[9][0], knot_locations[9][1])
        if tail_coordinate_f not in positions:
            positions.append(tail_coordinate_f)
    break

print(len(positions))
# 2443