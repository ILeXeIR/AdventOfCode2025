class Solution:
    def parse_input(self, filename: str) -> list[str]:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]

    def find_solution(self, filename: str) -> int:
        map = self.parse_input(filename)
        queue = []
        new_map = [[] for _ in range(len(map))]
        for x in range(len(map)):
            for y in range(len(map[0])):
                rolls = self.rolls_around(map, x, y)
                new_map[x].append(rolls)
                if -1 < rolls < 4:
                    queue.append((x, y))
        result = len(queue)
        while queue:
            x, y = queue.pop()
            for i in range(max(0, x - 1), min(len(map), x + 2)):
                for j in range(max(0, y - 1), min(len(map[0]), y + 2)):
                    if i == x and j == y or new_map[i][j] == -1:
                        continue
                    new_map[i][j] -= 1
                    if new_map[i][j] == 3:
                        queue.append((i, j))
                        result += 1
        return result

    def rolls_around(self, map: list[str], x: int, y: int) -> int:
        if map[x][y] == ".":
            return -1
        rolls = 0
        for i in range(max(0, x - 1), min(len(map), x + 2)):
            for j in range(max(0, y - 1), min(len(map[0]), y + 2)):
                if i == x and j == y:
                    continue
                if map[i][j] == "@":
                    rolls += 1
        return rolls


if __name__ == "__main__":
    filename = "inputs/d4.txt"
    print(Solution().find_solution(filename))
