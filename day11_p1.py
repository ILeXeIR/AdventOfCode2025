class Solution:
    def __init__(self):
        self.map = {}

    def parse_input(self, filename: str) -> dict[set[str]]:
        with open(filename, "r") as file:
            map = {}
            for line in file.readlines():
                key, line = line.strip().split(": ")
                map[key] = set(line.split(" "))
        return map

    def find_solution(self, filename: str) -> int:
        self.map = self.parse_input(filename)
        return self.count_ways("you", [])

    def count_ways(self, node: str, way: list[str]) -> int:
        if node not in self.map:
            return 0
        result = 0
        visited = [way[index + 1] for index, step in enumerate(way) if step == node]
        way.append(node)
        for step in self.map[node]:
            if step == "out":
                result += 1
            elif step in visited:
                continue
            else:
                result += self.count_ways(step, way.copy())
        return result


if __name__ == "__main__":
    filename = "inputs/d11.txt"
    print(Solution().find_solution(filename))
