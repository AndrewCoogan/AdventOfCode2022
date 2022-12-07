with open('Day6_data.txt', 'r') as f:
    lines = [l for l in f.readlines()]
 
line = lines[0]
 
shift = 14 # 4
i = 0
 
while i + shift < len(line):
    sub_line = line[i:i+shift]
    if len(set(list(sub_line))) == shift:
        print(i+shift)
        break
    i += 1