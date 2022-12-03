with open('Day2_data.txt') as f:
    lines = [line.strip().split(' ') for line in f]

# What we know
# A = Rock
# B = Paper
# C = Scissor

# What we think we know
# X = Rock
# Y = Paper
# Z = Scissor

# Outcome
# Loss = 0
# Draw = 3
# Win = 6

selected = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

#1
'''
points = 0
for a, b in lines:
    # Tie
    if (a == 'A' and b == 'X') or (a == 'B' and b == 'Y') or (a == 'C' and b == 'Z'):
        semitotal = 3 + selected[b]
    # Lost
    elif (a == 'A' and b == 'Z') or (a == 'B' and b == 'X') or (a == 'C' and b == 'Y'):
        semitotal = selected[b]
    # Win
    else:
        semitotal = 6 + selected[b]
    points += semitotal
'''

#2
# Key
# X : Lose
# Y : Draw
# Z : Win

lose = {
    'A' : 'Z',
    'B' : 'X',
    'C' : 'Y'
}

tie = {
    'A' : 'X',
    'B' : 'Y',
    'C' : 'Z'
}

win = {
    'A' : 'Y',
    'B' : 'Z',
    'C' : 'X'
}

points = 0
for a, b in lines:
    #Lose
    if b == 'X':
        points += selected[lose[a]]
    elif b == 'Y':
        points += 3 + selected[tie[a]]
    else:
        points += 6 + selected[win[a]]

print(points)