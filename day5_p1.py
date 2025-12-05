class Solution:
    def __init__(self):
        self.ranges = []
        self.ingridients = []

    def parse_input(self, filename: str) -> list[str]:
        with open(filename, "r") as file:
            line = file.readline().strip()
            while line:
                x, y = (int(num) for num in line.split("-"))
                self.insert_range(x, y)
                line = file.readline().strip()
            self.ingridients = [int(line.strip()) for line in file.readlines()]

    def binary_search(self, num: int) -> int:
        start, end = 0, len(self.ranges)
        while start < end:
            mid = (start + end) // 2
            if num > self.ranges[mid][1]:
                start = mid + 1
            elif num < self.ranges[mid][0]:
                end = mid
            else:
                return mid
        return start

    def insert_range(self, x: int, y: int):
        i = j = self.binary_search(x)
        if i == len(self.ranges):
            self.ranges.append((x, y))
        while j < len(self.ranges) and y >= self.ranges[j][0]:
            j += 1
        range = (min(x, self.ranges[i][0]), max(y, self.ranges[j - 1][1]) if j >= 0 else y)
        self.ranges = self.ranges[:i] + [range] + self.ranges[j:]

    def find_solution(self, filename: str) -> int:
        self.parse_input(filename)
        result = 0
        for num in self.ingridients:
            i = self.binary_search(num)
            if i < len(self.ranges) and num >= self.ranges[i][0]:
                result += 1
        return result


if __name__ == "__main__":
    filename = "inputs/d5.txt"
    print(Solution().find_solution(filename))
