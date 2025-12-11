class Solution:
    def __init__(self):
        self.map = {}
        self.way_counter = {}

    def parse_input(self, filename: str) -> dict[set[str]]:
        with open(filename, "r") as file:
            map = {}
            for line in file.readlines():
                key, line = line.strip().split(": ")
                map[key] = set(line.split(" "))
        return map

    def find_solution(self, filename: str) -> int:
        self.map = self.parse_input(filename)
        a = self.count_ways("svr", "dac", set())
        self.way_counter = {}
        b = self.count_ways("dac", "fft", set())
        self.way_counter = {}
        c = self.count_ways("fft", "out", set())
        self.way_counter = {}
        f = self.count_ways("dac", "out", set())
        self.way_counter = {}
        d = self.count_ways("svr", "fft", set())
        self.way_counter = {}
        e = self.count_ways("fft", "dac", set())
        return (a * b * c + d * e * f)

    def count_ways(self, start: str, end: str, way: set[str]) -> int:
        if start not in self.map:
            return 0
        result = 0
        way.add(start)
        for step in self.map[start]:
            if step == end:
                result += 1
            elif step not in way:
                if step not in self.way_counter:
                    self.way_counter[step] = self.count_ways(step, end, way.copy())
                result += self.way_counter[step]
        return result


if __name__ == "__main__":
    filename = "inputs/d11.txt"
    print(Solution().find_solution(filename))
