class Solution:
    def __init__(self):
        self.dots = []
        self.verticals = []
        self.horizontals = []

    def parse_input(self, filename: str) -> list[list[int]]:
        with open(filename, "r") as file:
            return [[int(num) for num in line.strip().split(",")] for line in file.readlines()]

    def find_solution(self, filename: str) -> int:
        self.dots = self.parse_input(filename)
        self.dots.append(self.dots[0])
        for i in range(len(self.dots) - 1):
            if self.dots[i][0] == self.dots[i + 1][0]:
                y1, y2 = min(self.dots[i][1], self.dots[i + 1][1]), max(self.dots[i][1], self.dots[i + 1][1])
                self.verticals.append((self.dots[i][0], y1, y2))
            else:
                x1, x2 = min(self.dots[i][0], self.dots[i + 1][0]), max(self.dots[i][0], self.dots[i + 1][0])
                self.horizontals.append((self.dots[i][1], x1, x2))
        max_area = 0
        for i in range(len(self.dots) - 2):
            for j in range(i, len(self.dots) - 1):
                area = (abs(self.dots[i][0] - self.dots[j][0]) + 1)*(abs(self.dots[i][1] - self.dots[j][1]) + 1)
                if area > max_area and self.rect_is_inside(i, j):
                    max_area= area
        return max_area

    def rect_is_inside(self, i: int, j: int) -> bool:
        dots = [[self.dots[i][0], self.dots[j][1]], [self.dots[j][0], self.dots[i][1]]]
        for dot in dots:
            if not self.dot_is_inside(dot[0], dot[1]):
                return False
        edges = [[self.dots[i], dots[0]], [self.dots[i], dots[1]],
                 [self.dots[j], dots[0]], [self.dots[j], dots[1]]]
        for edge in edges:
            if not self.edge_is_inside(edge):
                return False
        return True

    def dot_is_inside(self, x: int, y: int) -> bool:
        intersections = 0
        for edge in self.verticals:
            if edge[1] <= y <= edge[2]:
                if x == edge[0]:
                    return True
                elif x > edge[0] and y < edge[2]:
                    intersections += 1
        return intersections % 2

    def edge_is_inside(self, edge: list[list[int]]) -> bool:
        x1, y1, x2, y2 = edge[0][0], edge[0][1], edge[1][0], edge[1][1]
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for line in self.horizontals:
                if line[1] < x1 < line[2] and y1 < line[0] < y2:
                    return False
        else:
            x1, x2 = min(x1, x2), max(x1, x2)
            for line in self.verticals:
                if line[1] < y1 < line[2] and x1 < line[0] < x2:
                    return False
        return True


if __name__ == "__main__":
    filename = "inputs/d9.txt"
    print(Solution().find_solution(filename))
