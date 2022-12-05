def process_input():
    with open('input.txt', 'r') as file:
        first_line = file.readline()
        n_cols = len(first_line)//4
        stack_dict = dict(zip(list(range(1, n_cols + 1)), [[]] * n_cols))
        line = first_line
        col_container_pairs = []
        while line[1] != '1':
            for i in range(0, n_cols * 4, 4):
                if '[' in line[i:i+3]:
                    col_container_pairs.append((int(i/4 + 1), line[i:i+3]))
            line = file.readline()
        for pair in col_container_pairs:
            stack_dict.update({pair[0]: stack_dict.get(pair[0]) + [pair[1]]})

        return stack_dict

def get_steps():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        lines = list(filter(lambda x: x and x[:4] == 'move', lines))
        lines = [line.split()[1::2] for line in lines]
        lines = [[int(num) for num in l] for l in lines]
        return lines

def move_container(from_col, to_col):
    container = stack_dict[from_col][0]
    stack_dict.update({from_col: stack_dict[from_col][1:]})
    stack_dict.update({to_col: [container] + stack_dict[to_col]})

stack_dict = process_input()
steps = get_steps()

def part1():
    for step in steps:
        for i in range(step[0]):
            move_container(step[1], step[2])

    keyword = []

    for i in range(1, len(stack_dict.keys()) + 1):
        keyword.append(stack_dict[i][0][1])

    print(''.join(keyword))

# part1()

def move_containers(from_col, to_col, n_containers):
    containers = stack_dict[from_col][:n_containers]
    stack_dict.update({from_col: stack_dict[from_col][n_containers:]})
    stack_dict.update({to_col: containers + stack_dict[to_col]})

def part2():
    for step in steps:
        move_containers(step[1], step[2], step[0])

    keyword = []

    for i in range(1, len(stack_dict.keys()) + 1):
        keyword.append(stack_dict[i][0][1])

    print(''.join(keyword))

part2()