class CPU:

    def __init__(self):
        self.x = 1
        self.cycle_number = 0
        self.x_hist = []

    def noop(self):
        self.cycle_number += 1
        self.x_hist.append(self.x)

    def addx(self, x):
        self.noop()
        self.x += x
        self.noop()

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

execute_instructions()
find_signal_strength_sum()