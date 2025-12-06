class Solution:
    def parse_input(self, filename: str) -> list[list[str]]:
        with open(filename, "r") as file:
            return [line for line in file.readlines()]

    def find_solution(self, filename: str) -> int:
        sheet = self.parse_input(filename)
        total = 0
        start = 0
        while start < len(sheet[-1]):
            ch = sheet[-1][start]
            end = start + 1
            while end < len((sheet[-1])) and sheet[-1][end] == " ":
                end += 1
            if end == len((sheet[-1])):
                end += 1
            result = 0 if ch == "+" else 1
            for i in range(start, end - 1):
                num = 0
                for j in range(len(sheet) - 1):
                    if sheet[j][i] == " ":
                        continue
                    num = num * 10 + int(sheet[j][i])
                if ch == "+":
                    result += num
                else:
                    result *= num
            total += result
            start = end
        return total


if __name__ == "__main__":
    filename = "inputs/d6.txt"
    print(Solution().find_solution(filename))