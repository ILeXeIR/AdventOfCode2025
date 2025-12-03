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
        joltage = [ch for ch in line[:12]]
        for ch in line[12:]:
            for i in range(11):
                if joltage[i] < joltage[i + 1]:
                    joltage.pop(i)
                    joltage.append(ch)
                    ch = ""
                    break
            if ch and joltage[-1] < ch:
                joltage[-1] = ch
        return int("".join(joltage))


if __name__ == "__main__":
    filename = "inputs/d3.txt"
    print(Solution().find_solution(filename))
