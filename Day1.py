total = []
point_total = 0

with open('Day1_data.txt') as f:
    lines = [line.strip() for line in f]

for l in lines:
    if l == '':
        total.append(point_total)
        point_total = 0
    else:
        point_total += int(l)

total.append(point_total)

total_sorted = sorted(total, reverse=True)

print(total_sorted[:3])
print(sum(total_sorted[:3]))