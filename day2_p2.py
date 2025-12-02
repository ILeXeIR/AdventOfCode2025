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
        buffer = set()
        for length in range(1, len(end) // 2 + 1):
            start_num, start_repeats = self.get_start_num(start, length)
            end_num, end_repeats = self.get_end_num(end, length)
            for repeats in range(start_repeats, end_repeats + 1):
                if repeats < end_repeats:
                    left, right = start_num, 10 ** length
                elif repeats > start_repeats:
                    left, right = 10 ** (length - 1), end_num + 1
                else:
                    left, right = start_num, end_num + 1
                buffer.update({int(str(num) * repeats) for num in range(left, right)})
        return sum(buffer)

    def get_start_num(self, start: str, length: int) -> tuple[int, int]:
        repeats = len(start) // length
        if len(start) % length > 0 or repeats < 2:
            return (10 ** (length - 1), max(repeats + 1, 2))
        start_num = int(start[:length])
        for i in range(length, len(start), length):
            num = int(start[i: i + length])
            if num != start_num:
                break
        return (start_num, repeats) if start_num >= num else (start_num + 1, repeats)

    def get_end_num(self, end: str, length: int) -> tuple[int, int]:
        repeats = len(end) // length
        if len(end) % length > 0:
            return 10 ** length - 1, repeats
        end_num = int(end[:length])
        for i in range(length, len(end), length):
            num = int(end[i: i + length])
            if num != end_num:
                break
        if end_num <= num:
            return end_num, repeats
        elif end_num == 10 ** (length - 1):
            return 10 ** length - 1, repeats - 1
        else:
            return end_num - 1, repeats


if __name__ == "__main__":
    filename = "inputs/d2.txt"
    print(Solution().find_solution(filename))
