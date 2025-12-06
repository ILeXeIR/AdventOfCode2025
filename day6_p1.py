class Solution:
    def parse_input(self, filename: str) -> list[list[str]]:
        with open(filename, "r") as file:
            return [line.strip().split() for line in file.readlines()]

    def find_solution(self, filename: str) -> int:
        sheet = self.parse_input(filename)
        total = 0
        for i in range(len(sheet[0])):
            ch = sheet[-1][i]
            result = int(sheet[0][i])
            for j in range(1, len(sheet) - 1):
                if ch == "+":
                    result += int(sheet[j][i])
                else:
                    result *= int(sheet[j][i])
            total += result
        return total


if __name__ == "__main__":
    filename = "inputs/d6.txt"
    print(Solution().find_solution(filename))