with open('input.txt', 'r') as file:
    stream = file.read()

def part1() -> int:
    """
    Find the first unique sequence of 4 letters
    and return the index of the last character

    Returns:
        int: the index of the last character of the substring
    """
    for i in range(len(stream)-3):
        marker = stream[i:i+4]
        if len(set(marker)) == 4:
            return i+4

# print(part1())

def part2() -> int:
    """
    Find the first unique sequence of 14 letters
    and return the index of the last character

    Returns:
        int: the index of the last character of the substring
    """
    for i in range(len(stream)-13):
        marker = stream[i:i+14]
        if len(set(marker)) == 14:
            return i+14

print(part2())