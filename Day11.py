import aocd
import re

data = aocd.get_data(year=2022, day=11).split('\n')

class monk():
    def __init__(self, lines):
        self.name = int(re.findall(r'\d+', lines[0])[0])
        self.items = [int(s.strip()) for s in lines[1].split(':')[1].split(',')]
        self.operation = lambda old: eval(lines[2].split('=')[1].strip())
        self.test = lambda val: val % int(re.findall(r'\d+', lines[3])[0]) == 0
        self.test_true = int(re.findall(r'\d+', lines[4])[0])
        self.test_false = int(re.findall(r'\d+', lines[5])[0])
        self.inspect_count = 0
    
    def inspect(self, modulo):
        self.inspect_count += 1
        item = self.items[0]
        new_worry = self.operation(int(item))
        post_bored = new_worry % modulo
        # This is called the modulo trick, had to find this online.
        # https://github.com/mebeim/aoc/blob/master/2022/README.md#day-11---monkey-in-the-middle
        test_val = self.test(post_bored)
        self.items = self.items[1:]
        return post_bored, self.test_true if test_val else self.test_false   

monkies = []
modulo = 1

for i in range(0,len(data), 7):
    monkies.append(monk(data[i:i+6]))
    modulo *= int(re.findall(r'\d+', data[i+3])[0])


for _ in range(10000):
    print(_)
    for i in range(len(monkies)):
        while len(monkies[i].items):
            worry_pass, monk_pass = monkies[i].inspect(modulo)
            monkies[monk_pass].items.append(worry_pass)

monk_business = []

for monkey in monkies:
    monk_business.append(monkey.inspect_count)

monk_business = sorted(monk_business, reverse=True)

print(monk_business[0] * monk_business[1])