class Solution:
    def parse_input(self, filename: str) -> list[str]:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]

    def find_solution(self, filename: str) -> int:
        lines = self.parse_input(filename)
        result = 0
        for line in lines:
            result += self.get_joltage(line)
        return result

    def get_joltage(self, line: str) -> int:
        joltage = 0
        max_num = 0
        for ch in line:
            joltage = max(joltage, max_num + int(ch))
            max_num = max(max_num, int(ch) * 10)
        return joltage


if __name__ == "__main__":
    filename = "inputs/d3.txt"
    print(Solution().find_solution(filename))
