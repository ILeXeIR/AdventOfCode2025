class Solution:
    def parse_input(self, filename: str) -> list[int]:
        with open(filename, "r") as file:
            return [self.get_number(line.strip()) for line in file.readlines()]

    def get_number(self, line: str) -> int:
        num  = int(line[1:]) % 100
        return num if line[0] == "R" else -num
    
    def find_solution(self, filename: str) -> int:
        moves = self.parse_input(filename)
        point = 50
        nulls = 0
        for move in moves:
            point += move
            if point < 0:
                point += 100
            elif point > 99:
                point -= 100
            if point % 100 == 0:
                nulls += 1
        return nulls

if __name__ == "__main__":
    filename = "inputs/d1p1.txt"
    print(Solution().find_solution(filename))
