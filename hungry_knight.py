class Point:

    # d stands for distance
    # distance is used to track how many steps
    # it took the knight to get to some Point

    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def addToQueueMoves(self, queue, limit):
        move = [
            Point(self.x - 1, self.y + 2, self.d + 1),
            Point(self.x - 1, self.y - 2, self.d + 1),
            Point(self.x - 2, self.y + 1, self.d + 1),
            Point(self.x - 2, self.y - 1, self.d + 1),
            Point(self.x + 1, self.y + 2, self.d + 1),
            Point(self.x + 1, self.y - 2, self.d + 1),
            Point(self.x + 2, self.y + 1, self.d + 1),
            Point(self.x + 2, self.y - 1, self.d + 1)
        ]
        for i in move:
            if 1 <= i.x <= limit and 1 <= i.y <= limit:
                queue.append(i)

    def equals(self, point):
        return point.x == self.x and point.y == self.y


def solution():
    N = int(input())
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    # here position and destination do not
    # need distance parameter, so it is 0

    position = Point(x1, y1, 0)
    destination = Point(x2, y2, 0)

    if not(1 <= position.x <= N) and not(1 <= position.y <= N):
        print("Position out of reach")

    if not(1 <= destination.x <= N) and not(1 <= destination.y <= N):
        print("Destination out of reach")

    print(bfs(position, destination, N))


# regular bfs algorithm


def bfs(pos, destination, limit):
    visited = []
    queue = [pos]

    while queue:
        v = queue.pop(0)
        flag = False

        for i in visited:
            if v.equals(i):
                flag = True
                break
        if flag:
            continue

        visited.append(v)
        if v.equals(destination):
            return v.d
        v.addToQueueMoves(queue, limit)

    return None

    # return None if there is no way for
    # the knight to reach destination Point,
    # which will not happen


solution()
