class CountSquares:

    def __init__(self):
        self.points = {}
        self.rows = {}

    def add(self, point):
        x, y = point

        self.points[(x, y)] = self.points.get((x, y), 0) + 1

        if y not in self.rows:
            self.rows[y] = {}
        self.rows[y][x] = self.rows[y].get(x, 0) + 1

    def count(self, point):
        x, y = point

        if y not in self.rows:
            return 0

        res = 0

        for nx in self.rows[y]:
            if nx == x:
                continue

            d = nx - x

            res += (
                self.rows[y][nx] *
                self.points.get((x, y + d), 0) *
                self.points.get((nx, y + d), 0)
            )

            res += (
                self.rows[y][nx] *
                self.points.get((x, y - d), 0) *
                self.points.get((nx, y - d), 0)
            )

        return res