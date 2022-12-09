with open('input.txt', 'r') as file:
    all_meals = file.read().splitlines()

def part1():
    """
    Solution for AoC Day 1 Part 1
    """
    largest = 0
    current_sum = 0

    for meal in all_meals:
        # If the entry is empty, that's the end of that elf's provisions
        if meal == '':
            # If the sum of that elf's provisions is greater than the current largest
            if current_sum > largest:
                largest = current_sum
            current_sum = 0
        else:
            current_sum += int(meal)

    if current_sum > largest:
        largest = current_sum

    return largest

def part2():
    """
    Solution for AoC Day 1 Part 2
    """
    largest1, largest2, largest3 = 0, 0, 0
    current_sum = 0

    for meal in all_meals:
        # If the entry is empty, that's the end of that elf's provisions
        if meal == '':
            # If the sum of that elf's provisions is greater than the current largest
            if current_sum > largest1:
                largest3, largest2, largest1 = largest2, largest1, current_sum
            elif current_sum > largest2:
                largest3, largest2 = largest2, current_sum
            elif current_sum > largest3:
                largest3 = current_sum
            current_sum = 0
        else:
            current_sum += int(meal)

    if current_sum > largest1:
        largest3, largest2, largest1 = largest2, largest1, current_sum
    elif current_sum > largest2:
        largest3, largest2 = largest2, current_sum
    elif current_sum > largest3:
        largest3 = current_sum

    return sum((largest1, largest2, largest3))

print(part2())
