import numpy as np

with open('Day8_data.txt') as f:
    lines = [list(line.strip()) for line in f]

# The keys will be the coordinates of the trees, the values will be the height.
highest_trees = {}
trees = np.array(lines).astype(int)

def evaluate_forest(trees, highest_trees = {}):
    extremes = [0, len(trees)-1]
    for i in range(len(trees)): # Up to down
        for j in range(len(trees[0])): # Left to right
            if i in extremes or j in extremes:
                highest_trees[(i,j)] = trees[i,j]
            # Looking left to right
            elif all(trees[i,:j] < trees[i,j]):
                    highest_trees[(i,j)] = trees[i,j]
            # Looking right to left
            elif all(trees[i,j+1:] < trees[i,j]):
                    highest_trees[(i,j)] = trees[i,j]
            # Looking up to down
            elif all(trees[:i,j] < trees[i,j]):
                    highest_trees[(i,j)] = trees[i,j]
            # Looking down to up
            elif all(trees[i+1:,j] < trees[i,j]):
                    highest_trees[(i,j)] = trees[i,j]

    return highest_trees

#highest_trees = evaluate_forest(trees)
#print(f'Part 1: {len(highest_trees)}')

def score_view(los : np.array, height : int):
    # This is going to assume we are standing to the left of the array
    if all(height > tree for tree in los):
        return len(los)
    for index, value in enumerate(los):
        if value >= height:
            return index + 1

def best_view(trees):
    ideal_location = ((0,0), 0)
    for i in range(1, len(trees)-1):
        for j in range(1, len(trees)-1):
            h = trees[i,j]
            trees_left = trees[i, :j][::-1]
            trees_right = trees[i, j+1:]
            trees_up = trees[:i,j][::-1]
            trees_down = trees[i+1:,j]
            score = score_view(trees_left, h) * \
                score_view(trees_right, h) * \
                score_view(trees_down, h) * \
                score_view(trees_up, h)
            if score > ideal_location[1]:
                ideal_location = ((i,j), score)
    return ideal_location

bv = best_view(trees)
print(bv)