class Solution:
    def parse_input(self, filename: str) -> list[str]:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]

    def find_solution(self, filename: str) -> int:
        map = self.parse_input(filename)
        result = 0
        for x in range(len(map)):
            for y in range(len(map[0])):
                if map[x][y] == ".":
                    continue
                result += self.is_accessible(map, x, y)
        return result

    def is_accessible(self, map: list[str], x: int, y: int) -> bool:
        rolls = 0
        for i in range(max(0, x - 1), min(len(map), x + 2)):
            for j in range(max(0, y - 1), min(len(map[0]), y + 2)):
                if i == x and j == y:
                    continue
                if map[i][j] == "@":
                    rolls += 1
        return rolls < 4


if __name__ == "__main__":
    filename = "inputs/d4.txt"
    print(Solution().find_solution(filename))
