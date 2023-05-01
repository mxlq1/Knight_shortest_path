class Point:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def addToQueueMoves(self, queue):
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
            queue.append(i)

    def equals(self, point):
        if point.x == self.x and point.y == self.y:
            return True
        return False


def solution():
    N = int(input())
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    position = Point(x1, y1, 0)
    destination = Point(x2, y2, 0)

    print(bfs(position, destination, N))


def bfs(pos, destination, limit):
    visited = []
    queue = [pos]

    while queue:
        v = queue.pop(0)
        flag = False

        for i in visited:
            if v.equals(i):
                flag = True
        if flag:
            continue

        visited.append(v)
        if not(1 <= v.x <= limit) or not(1 <= v.y <= limit):
            continue
        if v.equals(destination):
            return v.d
        v.addToQueueMoves(queue)


solution()
