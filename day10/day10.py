class CPU:

    def __init__(self):
        self.x = 1
        self.cycle_number = 0
        self.x_hist = []
        self.crt = ['#']

    def noop(self):
        self.cycle_number += 1
        self.x_hist.append(self.x)
        self.add_pixel()

    def addx(self, x):
        self.noop()
        self.x += x
        self.noop()

    def add_pixel(self):
        if self.x in ((self.cycle_number - 1) % 40, self.cycle_number % 40, (self.cycle_number + 1) % 40):
            self.crt.append('#')
        else:
            self.crt.append('.')

def setup():
    with open('day10/input.txt', 'r') as file:
        lines = file.read().splitlines()
        instructions = [line.split() for line in lines]
    return instructions

instrunctions = setup()
cpu = CPU()

def execute_instructions():
    for instr in instrunctions:
        if instr[0] == 'noop':
            cpu.noop()
        else:
            cpu.addx(int(instr[1]))

def find_signal_strength_sum():
    cycles = list(range(20, 221, 40))
    signal_sum = 0
    for cycle in cycles:
        signal = cpu.x_hist[cycle - 2] * cycle
        signal_sum += signal

    print(signal_sum)

def part1():
    execute_instructions()
    find_signal_strength_sum()
    
# part1()

def draw_letters():
    cycles = [0] + list(range(0, 241, 40))
    for i in range(len(cycles) - 1):
        print(''.join(cpu.crt[cycles[i]:cycles[i+1]]))

def part2():
    execute_instructions()
    draw_letters()

part2()

