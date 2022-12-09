class Tree:
    def __init__(self, height: int) -> None:
        self.is_left_visible = False
        self.is_right_visible = False
        self.is_up_visible = False
        self.is_down_visible = False
        self.height = int(height)
        self.left_score = 0
        self.right_score = 0
        self.up_score = 0
        self.down_score = 0
        

    def __repr__(self) -> str:
        return str(self.score)

    @property
    def is_visible(self) -> bool:
        return any([
            self.is_left_visible,
            self.is_right_visible,
            self.is_up_visible,
            self.is_down_visible
        ])

    @property
    def score(self) -> int:
        return self.down_score * \
            self.left_score * \
            self.right_score * \
            self.up_score

def setup():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
        trees = [list(map(Tree, l)) for l in lines]

    for tree in trees[0]:
        tree.is_up_visible = True

    for tree in trees[-1]:
        tree.is_down_visible = True

    for tree_row in trees:
        tree_row[0].is_left_visible = True

    for tree_row in trees:
        tree_row[-1].is_right_visible = True

    return trees

trees = setup()

def find_left_visibles():
    for row in trees:
        for i, tree in enumerate(row):
            heights = [row[t].height for t in range(i, -1, -1)]
            if heights[0] == max(heights) and heights[0] not in heights[1:]:
                row[i].is_left_visible = True

def find_right_visibles():
    for row in trees:
        for i, tree in enumerate(row):
            heights = [t.height for t in row[i:]]
            if heights[0] == max(heights) and heights[0] not in heights[1:]:
                row[i].is_right_visible = True

def find_up_visibles():
    for i, row in enumerate(trees):
        for j, tree in enumerate(row):
            heights = [trees[k][j].height for k in range(i, -1, -1)]
            if heights[0] == max(heights) and heights[0] not in heights[1:]:
                row[j].is_up_visible = True

def find_down_visibles():
    for i, row in enumerate(trees):
        for j, tree in enumerate(row):
            heights = [trees[k][j].height for k in range(i, len(trees))]
            if heights[0] == max(heights) and heights[0] not in heights[1:]:
                row[j].is_down_visible = True

def part1():
    find_left_visibles()
    find_right_visibles()
    find_up_visibles()
    find_down_visibles()

    n_visible = 0
    for row in trees:
        for tree in row:
            if tree.is_visible:
                n_visible += 1

    print(n_visible)

part1()

def find_left_score():
    for row in trees:
        for i, tree in enumerate(row):
            heights = [row[t].height for t in range(i, -1, -1)]
            initial_height = heights[0]
            for h in heights[1:]:
                if h >= initial_height:
                    tree.left_score += 1
                    break
                else:
                    tree.left_score += 1

def find_right_score():
    for row in trees:
        for i, tree in enumerate(row):
            heights = [t.height for t in row[i:]]
            initial_height = heights[0]
            for h in heights[1:]:
                if h >= initial_height:
                    tree.right_score += 1
                    break
                else:
                    tree.right_score += 1

def find_up_score():
    for i, row in enumerate(trees):
        for j, tree in enumerate(row):
            heights = [trees[k][j].height for k in range(i, -1, -1)]
            initial_height = heights[0]
            for h in heights[1:]:
                if h >= initial_height:
                    tree.up_score += 1
                    break
                else:
                    tree.up_score += 1

def find_down_score():
    for i, row in enumerate(trees):
        for j, tree in enumerate(row):
            heights = [trees[k][j].height for k in range(i, len(trees))]
            initial_height = heights[0]
            for h in heights[1:]:
                if h >= initial_height:
                    tree.down_score += 1
                    break
                else:
                    tree.down_score += 1
def part2():

    find_left_score()
    find_right_score()
    find_down_score()
    find_up_score()

    max_score = 0
    for row in trees:
        for tree in row:
            if tree.score > max_score:
                max_score = tree.score

    print(max_score)

part2()