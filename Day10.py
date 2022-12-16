import aocd

instructions = aocd.get_data(year=2022, day=10).split('\n')

x = [1]
poi = [20, 60, 100, 140, 180, 220]

for instx in instructions:
    if 'addx' in instx:
        num = int(instx.split(' ')[1])
        x.append(x[-1])
        x.append(x[-1] + num)
    else:
        x.append(x[-1])

running_sum = 0
for i in poi:
    running_sum += i * x[i-1]

print(running_sum)