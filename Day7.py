from pathlib import Path

with open('Day7_data.txt') as f:
    lines = [line.strip() for line in f]

def get_dir_tree(commands) -> dict:
    level = Path("")
    dir_tree = {}
    for entry in commands:
        if "$ cd" in entry:
            if ".." in entry:
                level = level.parent
            else:
                direc_name = entry[5:]
                level = level / direc_name
                if level not in dir_tree:
                    dir_tree[level] = []
        elif "dir" in entry:
            _, direc_name = entry.split(" ")
            dir_tree[level].append(level / direc_name)
        elif entry[0].isnumeric():
            file_size, file_name = entry.split(" ")
            dir_tree[level].append((file_name, int(file_size)))
    return dir_tree

def total_dir_size(dir_path, dir_tree) -> int:
    total_size = 0
    for k in dir_tree[dir_path]:
        if isinstance(k, tuple):
            total_size += int(k[1])
        else:
            total_size += total_dir_size(k, dir_tree)
    return total_size

def get_dir_size(dir_tree) -> dict:
    return {dir: total_dir_size(dir, dir_tree) for dir in dir_tree}

file_system = get_dir_tree(lines)
dir_size = get_dir_size(file_system)

max_size = 100_000
print(f'Part 1: {sum(k for k in dir_size.values() if k <= max_size)}')

total_disk_space = 70_000_000
free_space_required = 30_000_000
used_space = dir_size[Path("/")]
initial_free_space = total_disk_space - used_space
space_to_clear = free_space_required - initial_free_space

# This is just to initialize the tuple.
min_removeable_dir = (total_disk_space, Path('Dummy/Path'))

for dir in dir_size:
    if dir_size[dir] > space_to_clear:
        if dir_size[dir] < min_removeable_dir[0]:
            min_removeable_dir = (dir_size[dir], dir)

print(f'Part 2: {min_removeable_dir[0]}')