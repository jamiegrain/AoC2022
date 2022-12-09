with open('day9/input.txt', 'r') as file:
    directions = [line.split() for line in file.read().splitlines()]

class Head:

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def __repr__(self) -> str:
        return str((self.x, self.y))


class Tail:

    def __init__(self, head: Head) -> None:
        self.x = 0
        self.y = 0
        self.positions_visited = set()
        self.head = head
        self.add_new_position()

    def move_right(self):
        if self.head.x > self.x + 1:
            self.x += 1
            if self.head.y > self.y:
                self.y += 1
            if self.head.y < self.y:
                self.y -= 1
        self.add_new_position()
        self.catch_up()

    def move_left(self):
        if self.head.x < self.x - 1:
            self.x -= 1
            if self.head.y > self.y:
                self.y += 1
            if self.head.y < self.y:
                self.y -= 1
        self.add_new_position()
        self.catch_up()

    def move_up(self):
        if self.head.y > self.y + 1:
            self.y += 1
            if self.head.x > self.x:
                self.x += 1
            if self.head.x < self.x:
                self.x -= 1
        self.add_new_position()
        self.catch_up()

    def move_down(self):
        if self.head.y < self.y - 1:
            self.y -= 1
            if self.head.x > self.x:
                self.x += 1
            if self.head.x < self.x:
                self.x -= 1
        self.add_new_position()
        self.catch_up()

    def add_new_position(self):
        self.positions_visited.add((self.x, self.y))

    def catch_up(self):
        if self.head.x - self.x > 1:
            self.x += 1
            if self.head.y - self.y > 0:
                self.y += 1
            if self.head.y - self.y < 0:
                self.y -= 1
        if self.head.y - self.y > 1:
            self.y += 1
            if self.head.x - self.x > 0:
                self.x += 1
            if self.head.x - self.x < 0:
                self.x -= 1
        if self.head.x - self.x < -1:
            self.x -= 1
            if self.head.x - self.x > 0:
                self.x += 1
            if self.head.x - self.x < 0:
                self.x -= 1
        if self.head.x - self.x < -1:
            self.y -= 1
            if self.head.x - self.x > 0:
                self.x += 1
            if self.head.x - self.x < 0:
                self.x -= 1

    def __repr__(self) -> str:
        return str((self.x, self.y))


def part1():
    head = Head()
    tail = Tail(head)

    for d in directions:
        direction, times = d[0], int(d[1])

        for i in range(times):
            if direction == 'U':
                head.move_up()
                tail.move_up()
            if direction == 'D':
                head.move_down()
                tail.move_down()
            if direction == 'R':
                head.move_right()
                tail.move_right()
            if direction == 'L':
                head.move_left()
                tail.move_left()

    print(len(tail.positions_visited))

def part2():
    head = Head()
    tail1 = Tail(head)
    tail2 = Tail(tail1)
    tail3 = Tail(tail2)
    tail4 = Tail(tail3)
    tail5 = Tail(tail4)
    tail6 = Tail(tail5)
    tail7 = Tail(tail6)
    tail8 = Tail(tail7)
    tail9 = Tail(tail8)

    rope = [
        tail9,
        tail8,
        tail7,
        tail6,
        tail5,
        tail4,
        tail3,
        tail2,
        tail1,
        head
    ]

    rope.reverse()

    for d in directions:
        direction, times = d[0], int(d[1])

        for _ in range(times):
            if direction == 'U':
                head.move_up()
                tail1.move_up()
                tail2.move_up()
                tail3.move_up()
                tail4.move_up()
                tail5.move_up()
                tail6.move_up()
                tail7.move_up()
                tail8.move_up()
                tail9.move_up()
            if direction == 'D':
                head.move_down()
                tail1.move_down()
                tail2.move_down()
                tail3.move_down()
                tail4.move_down()
                tail5.move_down()
                tail6.move_down()
                tail7.move_down()
                tail8.move_down()
                tail9.move_down()
            if direction == 'R':
                head.move_right()
                tail1.move_right()
                tail2.move_right()
                tail3.move_right()
                tail4.move_right()
                tail5.move_right()
                tail6.move_right()
                tail7.move_right()
                tail8.move_right()
                tail9.move_right()
            if direction == 'L':
                head.move_left()
                tail1.move_left()
                tail2.move_left()
                tail3.move_left()
                tail4.move_left()
                tail5.move_left()
                tail6.move_left()
                tail7.move_left()
                tail8.move_left()
                tail9.move_left()
            print(rope)

    # print(tail9.positions_visited)
    print(len(tail9.positions_visited))

part1()

# So why am I not getting the correct answer? Well, it's to do with how the rope moves
# My initial understanding was that the rope would move a la snake. This is not the case
# and the rope can move sideways. This can be left as an exercise to be done some other time