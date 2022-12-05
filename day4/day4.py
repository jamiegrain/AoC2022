from typing import List, Set

def preprocess(filename: str) -> List[List[List[str]]]:
    """
    Preprocess the input data for use

    Args:
        filename (str): _description_

    Returns:
        List[List[List[str]]]: _description_
    """
    with open(filename, 'r') as file:
        sections = file.read().splitlines()
        sections = [section.split(',') for section in sections]
        sections = [[s.split('-') for s in section] for section in sections]

        section_sets = []

        for section in sections:
            l = []
            for s in section:
                s_set = set(range(int(s[0]), int(s[1]) + 1))
                l.append(s_set)
            section_sets.append(l)

    return section_sets

sections = preprocess('input.txt')

def is_full_overlap(s1: Set[int], s2: Set[int]) -> bool:
    """
    Given two sets of numbers check if there is a full overlap

    Args:
        s1 (Set[int]): a set of ints
        s2 (Set[int]): a set of ints

    Returns:
        bool: True if the sets have a full overlap
    """
    if s1.intersection(s2) == s1 or s1.intersection(s2) == s2:
        return True
    else:
        return False

def part1() -> int:
    """
    Find the number of fully overlapping sets

    Returns:
        int: the number of fully overlapping sets
    """
    n_overlapping_sets = 0
    for section in sections:
        if is_full_overlap(section[0], section[1]):
            n_overlapping_sets += 1

    return n_overlapping_sets

# print(part1())

def is_partial_overlap(s1: Set[int], s2: Set[int]) -> bool:
    """
    Find if two sets have any overlapping elements

    Args:
        s1 (Set[int]): A set of numbers
        s2 (Set[int]): A set of numbers

    Returns:
        bool: True if there is any overlap
    """
    if s1.intersection(s2):
        return True
    else:
        return False

def part2() -> int:
    """
    Find the number of partially overlapping sets

    Returns:
        int: the number of partially overlapping sets
    """
    n_overlapping_sets = 0
    for section in sections:
        if is_partial_overlap(section[0], section[1]):
            n_overlapping_sets += 1

    return n_overlapping_sets

print(part2())