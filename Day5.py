stacks = [
    ['N','Z'],
    ['D','C','M'],
    ['P']
]
 
'''
    [V] [G]             [H]        
[Z] [H] [Z]         [T] [S]        
[P] [D] [F]         [B] [V] [Q]    
[B] [M] [V] [N]     [F] [D] [N]    
[Q] [Q] [D] [F]     [Z] [Z] [P] [M]
[M] [Z] [R] [D] [Q] [V] [T] [F] [R]
[D] [L] [H] [G] [F] [Q] [M] [G] [W]
[N] [C] [Q] [H] [N] [D] [Q] [M] [B]
'''
 
stacks_r = [
    ['N','D','M','Q','B','P','Z'],
    ['C','L','Z','Q','M','D','H','V'],
    ['Q','H','R','D','V','F','Z','G'],
    ['H','G','D','F','N'],
    ['N','F','Q'],
    ['D','Q','V','Z','F','B','T'],
    ['Q','M','T','Z','D','V','S','H'],
    ['M','G','F','P','N','Q'],
    ['B','W','R','M']
]
 

stacks = [list(reversed(r)) for r in stacks_r]
 
with open('Day5_data.txt', 'r') as f:
    lines = [l for l in f.readlines()]
 
for l in lines:
    instx = l.split()
    n_ = int(instx[1])
    from_ = int(instx[3]) - 1
    to_ = int(instx[5]) - 1
 
    to_add = list(stacks[from_][:n_])
 
    print(n_, from_+1, to_+1, to_add, stacks)
 
    stacks[to_] = to_add + stacks[to_]
    stacks[from_] = stacks[from_][n_:]
 
output = ''.join([d[0] for d in stacks])
print(output)