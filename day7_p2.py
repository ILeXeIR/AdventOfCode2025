class Solution:
    def parse_input(self, filename: str) -> list[str]:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]

    def find_solution(self, filename: str) -> int:
        lines = self.parse_input(filename)
        cur = [0 if ch == "." else 1 for ch in lines[0]]
        for line in lines[1:]:
            prev = cur.copy()
            for i, ch in enumerate(line):
                if ch == "^" and prev[i] > 0:
                    cur[i] = 0
                    if i - 1 >= 0:
                        cur[i - 1] += prev[i]
                    if i + 1 < len(cur):
                        cur[i + 1] += prev[i]
        return sum(cur)


if __name__ == "__main__":
    filename = "inputs/d7.txt"
    print(Solution().find_solution(filename))
