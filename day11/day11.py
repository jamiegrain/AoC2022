class Monkey:

    def __init__(
        self, 
        monkey_id, 
        items, 
        operation, 
        test, 
        if_true_monkey_id, 
        if_false_monkey_id
        ) -> None:
        # Items represented by their raw worry level
        self.id = monkey_id
        self.items = items
        self.operation = operation
        self.test_divisible_by = int(test)
        self.if_true_monkey = int(if_true_monkey_id)
        self.if_false_monkey = int(if_false_monkey_id)
        self.items_inspected = 0

    def __repr__(self) -> str:
        return f'Monkey {self.id} has items: {self.items} and has inspected {self.items_inspected} items'

    def take_turn(self):
        while self.items:
            old = self.items.pop(0)
            self.items_inspected += 1
            # new is defined in the exec
            # new = eval(self.operation) // 3
            # Changed for part 2
            new = eval(self.operation) % multiplier
            is_divisible = new % self.test_divisible_by == 0
            if is_divisible:
                receiving_monkey = monkeys.get(self.if_true_monkey)
                receiving_monkey.items.append(new)
                monkeys.update({self.if_true_monkey: receiving_monkey})
            else:
                receiving_monkey = monkeys.get(self.if_false_monkey)
                receiving_monkey.items.append(new)
                monkeys.update({self.if_false_monkey: receiving_monkey})
            

with open('day11/input.txt', 'r') as file:
    file_contents = file.read()
    unprocessed_monkeys = file_contents.split('\n\n')
    monkeys = {}
    for monkey in unprocessed_monkeys:
        lines = monkey.splitlines()
        monkey_id = int(lines[0].split()[-1][:-1])
        items = [int(item) for item in lines[1].split(':')[1].split(',')]
        operation = lines[2].split('=')[1].strip()
        test = lines[3].split()[-1]
        if_true_monkey = lines[4].split()[-1]
        if_false_monkey = lines[5].split()[-1]
        monkeys.update({monkey_id: Monkey(
            monkey_id,
            items,
            operation,
            test,
            if_true_monkey,
            if_false_monkey
        )})

def part1():
    for _ in range(20):
        for i in range(len(monkeys)):
            monkeys[i].take_turn()

    items_counted_per_monkey = [monkey.items_inspected for monkey in monkeys.values()]

    items_counted_per_monkey.sort(reverse=True)

    max_two = items_counted_per_monkey[:2]

    monkey_business = max_two[0] * max_two[1]

    return monkey_business

def find_mutliplier():
    
    divisors = [monkey.test_divisible_by for monkey in monkeys.values()]
    x = 1
    for d in divisors:
        x *= d
    return x

def part2():

    for _ in range(10000):
        for i in range(len(monkeys)):
            monkeys[i].take_turn()
        print(_)

    items_counted_per_monkey = [monkey.items_inspected for monkey in monkeys.values()]

    items_counted_per_monkey.sort(reverse=True)

    max_two = items_counted_per_monkey[:2]

    monkey_business = max_two[0] * max_two[1]

    return monkey_business

multiplier = find_mutliplier()

print(part2())