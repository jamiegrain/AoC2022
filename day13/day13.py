from typing import List

with open('day13/input.txt', 'r') as file:
    lines = file.read().splitlines()
    lines = list(filter(lambda x: len(x) > 1, lines))
    line_pairs = [(eval(lines[i]), eval(lines[i+1])) for i in range(0, len(lines) - 1, 2)]

print(len(line_pairs))

def compare(l1: List[int], l2: List[int]) -> bool:
    """
    Compare if the two lists are in the right order
    That is, compare each element of each list one at a time
    (l1[i] with l2[i]) until we find one where the left is larger than the right
    or if we run out of numbers on the left before the right

    Args:
        l1 (List[int]): List of numbers
        l2 (List[int]): List of numbers

    Returns:
        bool: Whether the lists fit the rules
    """
    if not isinstance(l1, list):
        l1 = [l1]
    if not isinstance(l2, list):
        l2 = [l2]
    for i, j in zip(l1, l2):
        if isinstance(i, list) or isinstance(j, list):
            result = compare(i, j)
        else:
            result = j - i
        if result != 0:
            return result
    
    return len(l2) - len(l1)

index_sum = 0

for i, line in enumerate(line_pairs, 1):
    l1, l2 = line
    if compare(l1, l2) > 0:
        index_sum += i

print(index_sum)

# l1, l2 = line_pairs[3]
# print(l1)
# print(l2)
# print(compare(l1, l2))
