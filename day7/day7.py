with open('example.txt', 'r') as file:
    lines = file.readlines()

dirs = {}

def generate_initial_map():
    """
    Step one will be to generate a dict of what the dirs all contain
    This is regardless of whether the contents are files or dirs
    """
    current_dir = ''

    for line in lines:
        # If line is a non-ls command and not moving up dirs
        if line[0] == '$' and line[2:4] != 'ls' and line[6] != '.':
            dir_name = f'{current_dir}~{line[5:-1]}'
            if dir_name not in dirs.keys():
                dirs.update({dir_name: []})
            current_dir = dir_name
            if current_dir == 'ngmqbc':
                breakpoint()
        elif line[0] in map(lambda x: str(x), (0,1,2,3,4,5,6,7,8,9)):
            dirs[current_dir].append(int(line.split()[0]))
        elif line[:3] == 'dir':
            dirs[current_dir].append(f'{dir_name}~{line[4:-1]}')
        elif 'cd ..' in line:
            current_dir = '~'.join(current_dir.split('~')[:-1])

final_sizes = {}

def find_file_only_dirs():
    """
    Find dirs that contain only files, sum their sizes and add them
    to the final sizes dict. We then need to delete them from dirs
    """
    dirs_to_delete = []

    for dir_name, contents in dirs.items():
        if all([str(content).isnumeric() for content in contents]):
            final_sizes.update({dir_name: sum(contents)})
            dirs_to_delete.append(dir_name)
    for d in dirs_to_delete:
        del dirs[d]

def replace_dirs_where_possible():
    """
    Once we know the final size of as many dirs as possible we want
    to replace their values in other dirs in the dirs dict
    """
    for dir_name, contents in dirs.items():
        if set(contents).intersection(set(final_sizes.keys())):
            for i, c in enumerate(contents):
                if c in final_sizes.keys():
                    contents[i] = final_sizes.get(c)

def part1():
    """
    This puts it all together
    1. Generate the initial map
    2. Sum the file only dirs and remove them
    3. Replace the dirs we know the sizes of in the initial map
    4. Repeat two and three till nothing remains unknown
    5. Find the sum
    """
    generate_initial_map()
    while dirs:
        find_file_only_dirs()
        replace_dirs_where_possible()

    dir_sum = 0

    for v in final_sizes.values():
        if v <= 100000:
            dir_sum += v

    print(dir_sum)

part1()

def part2():
    """
    We need to find the additional space required for the update by
    subtracting the disk size (70000000) from the outer dir size and then finding 
    the difference to the required size (30000000)

    We then need to find the smallest dir greater than that amount
    """
    outer_dir_size = final_sizes['~/']
    remaining_space = 70000000 - outer_dir_size
    required_space = 30000000 - remaining_space

    leading_candidate = (30000000, '')

    for dir, size in final_sizes.items():
        if required_space <= size <= leading_candidate[0]:
            leading_candidate = (size, dir)

    print(leading_candidate)

part2()