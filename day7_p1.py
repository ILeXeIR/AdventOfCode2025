class Solution:
    def parse_input(self, filename: str) -> list[str]:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]

    def find_solution(self, filename: str) -> int:
        lines = self.parse_input(filename)
        result = 0
        row = [ch if ch == "." else "1" for ch in lines[0]]
        for line in lines:
            for i, ch in enumerate(line):
                if ch == "^" and row[i] == "1":
                    result += 1
                    row[i] = "."
                    if i - 1 >= 0:
                        row[i - 1] = "1"
                    if i + 1 < len(row):
                        row[i + 1] = "1"
        return result


if __name__ == "__main__":
    filename = "inputs/d7.txt"
    print(Solution().find_solution(filename))
