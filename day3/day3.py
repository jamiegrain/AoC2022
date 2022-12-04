import string
letter_dict_1 = dict(zip(string.ascii_lowercase, list(range(1, 27))))
letter_dict_2 = dict(zip(string.ascii_uppercase, list(range(27, 53))))
letter_dict = { **letter_dict_1, **letter_dict_2 }

with open('input.txt', 'r') as file:
    bags = file.read().splitlines()

def part1() -> int:
    """
    Generate the sum of the duplicated letters for part1

    Returns:
        int: the sum of the duplicated letters
    """
    # Split the bags into compartments
    bag_contents = [(set(bag[:len(bag)//2]), set(bag[len(bag)//2:])) for bag in bags]

    # FInd the values that overlap between compartments
    priority_sum = 0
    for bag in bag_contents:
        overlapping_values = bag[0].intersection(bag[1])
        for letter in overlapping_values:
            priority_sum += letter_dict.get(letter)

    return priority_sum

def part2() -> int:
    """
    Get the sum of the shared values for each elf group

    Returns:
        int: The summed value
    """