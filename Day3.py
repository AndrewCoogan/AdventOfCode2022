with open('Day3_data.txt') as f:
    lines = [line.strip() for line in f]

'''
items = []
for l in lines:
    length = int(len(l)/2)
    
    front = set(l[:length])
    back = set(l[length:])
    items.append(list(front.intersection(back))[0])

key = 'abcdefghijklmnopqrstuvwxyz'
key = key + key.upper()

points = 0
for i in items:
    points += key.index(i) + 1
    
print(points)
'''

items = []
for i in range(0, len(lines), 3):
    bag1 = set(lines[i])
    bag2 = set(lines[i+1])
    bag3 = set(lines[i+2])

    overlap = bag1.intersection(bag2).intersection(bag3)
    items.append(list(overlap)[0])

key = 'abcdefghijklmnopqrstuvwxyz'
key = key + key.upper()

points = 0
for i in items:
    points += key.index(i) + 1
    
print(points)