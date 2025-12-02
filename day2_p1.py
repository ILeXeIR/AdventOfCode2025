class Solution:
    def parse_input(self, filename: str) -> list[tuple[int, int]]:
        with open(filename, "r") as file:
            ranges = file.readline().strip().split(",")
            return [(range.split("-")) for range in ranges]

    def find_solution(self, filename: str) -> int:
        ranges = self.parse_input(filename)
        result = 0
        for range in ranges:
            result += self.get_sum_invalid_ids(range[0], range[1])
        return result

    def get_sum_invalid_ids(self, start: str, end: str) -> int:
        start_num = self.get_start_num(start)
        end_num = self.get_end_num(end)
        return sum((int(f"{num}{num}") for num in range(start_num, end_num + 1)))

    def get_start_num(self, start: str) -> int:
        if len(start) < 2:
            return 0
        half_len = len(start) // 2
        if len(start) % 2 == 1:
            return 10 ** half_len
        start_num = int(start[:half_len])
        return start_num if start_num >= int(start[half_len:]) else start_num + 1

    def get_end_num(self, end: str) -> int:
        if len(end) < 2:
            return 0
        half_len = len(end) // 2
        if len(end) % 2 == 1:
            return 10 ** half_len - 1
        end_num = int(end[:half_len])
        return end_num if end_num <= int(end[half_len:]) else end_num - 1


if __name__ == "__main__":
    filename = "inputs/d2.txt"
    print(Solution().find_solution(filename))
