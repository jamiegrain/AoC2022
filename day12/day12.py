# import string

# with open('day12/input.txt', 'r') as file:
#     lines = file.read().splitlines()
#     lines = [list(line) for line in lines]

# letter_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
# letter_dict.update({'S': 0})
# letter_dict.update({'E': 27})

# class Graph:

#     def __init__(self, letter_matrix):
#         self.matrix = letter_matrix
#         self.starting_position = self.find_starting_position()
#         self.create_distance_dict()
#         self.create_visited_dict()
#         self.points_to_visit = [self.starting_position]
#         self.finishing_position = self.find_finishing_position()

#     def find_starting_position(self):
#         for y, line in enumerate(self.matrix):
#             for x, letter in enumerate(line):
#                 if letter == 'S':
#                     return (x, y)

#     def find_finishing_position(self):
#         for y, line in enumerate(self.matrix):
#             for x, letter in enumerate(line):
#                 if letter == 'E':
#                     return (x, y)

#     def create_distance_dict(self):
#         points = []
#         for y, line in enumerate(self.matrix):
#             for x, letter in enumerate(line):
#                 points.append((x, y))
#         distances = dict(zip(points, [99999999999999] * len(points)))
#         distances[self.starting_position] = 0
#         self.distances = distances

#     def create_visited_dict(self):
#         points = []
#         for y, line in enumerate(self.matrix):
#             for x, letter in enumerate(line):
#                 points.append((x, y))
#         visited_dict = dict(zip(points, [False] * len(points)))
#         self.visited_dict = visited_dict

#     def find_neighbour_distances(self):
#         x, y = self.points_to_visit.pop(0)
#         self.visited_dict[(x, y)] = True
#         letter_val = letter_dict.get(self.matrix[y][x])
#         poss_neighbours = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
#         for neighbour in poss_neighbours:
#             # Check for corner cases
#             if not 0 <= neighbour[0] < len(self.matrix[0]):
#                 continue
#             elif not 0 <= neighbour[1] < len(self.matrix):
#                 continue
#             # Non-corner case
#             else:
#                 if self.visited_dict[neighbour]:
#                     continue
#                 neighbour_letter_val = letter_dict.get(self.matrix[neighbour[1]][neighbour[0]])
#                 # If the step is reachable
#                 if (neighbour_letter_val - letter_val) < 2:
#                     # If the neighbour hasn't been visited, add to the list to be visited
#                     self.distances[(neighbour[0], neighbour[1])] = min(self.distances[(neighbour[0], neighbour[1])], self.distances[(x, y)] + 1)
#                     if neighbour not in self.points_to_visit:
#                         self.points_to_visit.append(neighbour)
# def part1():
#     g = Graph(lines)

#     g.create_distance_dict()

#     while g.points_to_visit:
#         g.find_neighbour_distances()

#     print(g.distances[g.finishing_position])

# def part2():

#     g = Graph(lines)

#     a_points = []

#     for y, line in enumerate(g.matrix):
#             for x, letter in enumerate(line):
#                 if letter == 'a':
#                     a_points.append((x, y))

#     for a in a_points:

#         g.starting_position = a

#         g.create_distance_dict()

#         while g.points_to_visit:
#             g.find_neighbour_distances()

#         print(g.distances[g.finishing_position])

# part2()

import collections, string
    
class SquareGrid():
    def __init__(self, labels):
        self.labels = labels
        self.width = len(labels[0])
        self.height = len(labels)
    
    def label_from_node(self, node):
        if not node:
            return "#"
        else:
            col, row = node
            return self.labels[row][col]

    def node_from_label(self, label):
        for row_i in range(self.height):
            if label in self.labels[row_i]:
                return (self.labels[row_i].index(label), row_i)    
    
    def in_bounds(self, node):
        x, y = node
        return 0 <= x < self.width and 0 <= y < self.height
    
    def too_high(self, node1, node2):
        label1 = self.label_from_node(node1)
        label2 = self.label_from_node(node2)
        if self.label_from_node(node2) == "E":
            label2 = "z"
        height1 = string.ascii_letters.index(label1)
        height2 = string.ascii_letters.index(label2)
        return height2 - height1 > 1
    
    def neighbors(self, node):
        x, y = node
        new_nodes = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
        neighbors = []
        for new_node in new_nodes:
            if self.in_bounds(new_node):
                neighbors.append(new_node)
        return neighbors

class Queue():
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return not self.elements
    
    def add(self, element):
        self.elements.append(element)
        
    def get(self):
        return self.elements.popleft()
    
def breadth_first_search(grid, start, end):
    frontier = Queue()
    frontier.add(start)
    came_from = {}
    came_from[start] = None
    steps = 0
    while not frontier.empty():
        current_node = frontier.get()
        if current_node == end:
            break
        for next_node in grid.neighbors(current_node):
            if next_node not in came_from and not grid.too_high(current_node, next_node):
                steps += 1
                came_from[next_node] = current_node
                frontier.add(next_node)
    return came_from

def part1_solution(day12_input):
    solution = []
    grid = SquareGrid(day12_input)
    start = grid.node_from_label("S")
    end = grid.node_from_label("E") 
    path = breadth_first_search(grid, start, end)
    node = end   
    while node != start:
        solution.append(grid.label_from_node(path[node]))
        node = path[node]
    return solution

def part2_solution(day12_input):
    solution = []
    paths = []
    grid = SquareGrid(day12_input)
    start_nodes = []
    for row_i in range(len(grid.labels)):
        for col_i in range(len(grid.labels[row_i])):
            if grid.labels[row_i][col_i] == "a" or grid.labels[row_i][col_i] == "S":
                start_nodes.append((col_i, row_i))
    end = grid.node_from_label("E")
    for start_node in start_nodes:
        path = []
        searched = breadth_first_search(grid, start_node, end)
        if end in searched:
            node = end   
            while node != start_node:
                path.append(searched[node])
                node = searched[node]
            paths.append(path)
    solution = [len(p) for p in paths]
    solution.sort()
    return solution[0]


with open("day12/input.txt", "r", encoding="UTF-8") as f:
    day12_input = [list(line) for line in f.read().split("\n")]

print(f"Part1: {len(part1_solution(day12_input))}")
print(f"Part2: {part2_solution(day12_input)}")               
