from typing import List, Tuple

with open('input.txt', 'r') as file:
    strategies = file.read().splitlines()
    unconverted_strategies = [strategy.split() for strategy in strategies]

score_mapping = {'rock': 1, 'paper': 2, 'scissors': 3}
result_mapping = {'lose': 0, 'draw': 3, 'win': 6}
win_mapping = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
p1_mapping = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
p2_mapping = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

def convert_strategies(unconverted_strategy_pairs: List[List[str]]) -> List[Tuple[str]]:
    """
    Convert the strategies as per part 1

    Args:
        unconverted_strategy_pairs (List[List[str]]): the list of lists of one letter strategies

    Returns:
        List[Tuple[str]]: the converted strategies
    """
    
    strategy_pairs = []

    for strategy in unconverted_strategy_pairs:
        p1_strategy = p1_mapping.get(strategy[0])
        p2_strategy = p2_mapping.get(strategy[1])

        strategy_pairs.append((p1_strategy, p2_strategy))

    return strategy_pairs

def decide_p2_result(p1: str, p2: str) -> str:
    """
    Decide on what result p1 gets

    Args:
        p1 (str): the p1 choice
        p2 (str): the p2 choice

    Returns:
        str: win, lose or draw
    """

    if p1 == p2:
        return 'draw'
    elif win_mapping.get(p1) == p2:
        return 'win'
    else:
        return 'lose'

def calculate_score(p2: str, result: str) -> int:
    """
    Calculate the score from the based on the result of one play

    Args:
        p2 (str): p2's choice (r, p, s)
        result (str): win, lose or draw

    Returns:
        int: the final score (based on the mapping dict)
    """
    return result_mapping.get(result) + score_mapping.get(p2)

def part1() -> int:
    """
    Get the answer to part 1

    Returns:
        int: the sum of the scores to the games
    """
    strategy_pairs = convert_strategies(unconverted_strategies)
    total_score = 0
    for strat in strategy_pairs:
        result = decide_p2_result(*strat)
        score = calculate_score(strat[1], result)
        total_score += score

    return total_score

# print(part1())

outcome_mapping = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
lose_mapping = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

def convert_strategies_part2(unconverted_strategy_pairs: List[List[str]]) -> List[Tuple[str]]:
    """
    Convert the strategies as per part 2

    Args:
        unconverted_strategy_pairs (List[List[str]]): the list of list of letter codes

    Returns:
        List[Tuple[str]]: the pairs of p1 strats and desired results
    """
    strategy_pairs = []

    for strategy in unconverted_strategy_pairs:
        p1_strategy = p1_mapping.get(strategy[0])
        desired_result = outcome_mapping.get(strategy[1])

        strategy_pairs.append((p1_strategy, desired_result))

    return strategy_pairs

def find_desired_action(p1: str, desired_result: str) -> str:
    """
    Find what p2 should do depending on what p1 does

    Args:
        p1 (str): rock paper or scissors
        desired_result (str): win lose or draw

    Returns:
        str: rock paper or scissors
    """

    if desired_result == 'draw':
        return p1
    elif desired_result == 'lose':
        return lose_mapping.get(p1)
    else:
        return win_mapping.get(p1)

def part2() -> int:
    """
    Calculate answer for part 2

    Returns:
        int: the final score
    """
    strategy_pairs = convert_strategies_part2(unconverted_strategies)
    total_score = 0
    for strat in strategy_pairs:
        p2_action = find_desired_action(*strat)
        score = result_mapping.get(strat[1]) + score_mapping.get(p2_action)
        total_score += score

    return total_score

print(part2())