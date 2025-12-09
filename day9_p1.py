class Solution:
    def parse_input(self, filename: str) -> list[list[int]]:
        with open(filename, "r") as file:
            return [[int(num) for num in line.strip().split(",")] for line in file.readlines()]

    def find_solution(self, filename: str) -> int:
        dots = self.parse_input(filename)
        max_area = 0
        for i in range(len(dots) - 1):
            for j in range(i, len(dots)):
                area = (abs(dots[i][0] - dots[j][0]) + 1)*(abs(dots[i][1] - dots[j][1]) + 1)
                if area > max_area:
                    max_area = area
        return max_area


if __name__ == "__main__":
    filename = "inputs/d9.txt"
    print(Solution().find_solution(filename))
