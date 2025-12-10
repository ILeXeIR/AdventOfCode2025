class Machine:
    def __init__(self, pattern: list[bool], buttons: list[list[int]]):
        self.pattern = pattern
        self.buttons = buttons

    def turn_on(self) -> int:
        min_switches = len(self.buttons)
        pattern = {i for i in range(len(self.pattern)) if self.pattern[i]}
        for i in range(2 ** len(self.buttons)):
            push_buttons = self._convert_into_binary(i, len(self.buttons))
            state = set()
            for x in range(len(push_buttons)):
                if push_buttons[x] == "1":
                    for num in self.buttons[x]:
                        if num in state:
                            state.remove(num)
                        else:
                            state.add(num)
            if state == pattern:
                switches = sum([ch == "1" for ch in push_buttons])
                if switches < min_switches:
                    min_switches = switches
                    if min_switches < 2:
                        break
        return min_switches

    def _convert_into_binary(self, num: int, length: int) -> str:
        result = ""
        for _ in range(length):
            result += str(num % 2)
            num //= 2
        return result

class Solution:
    def parse_line(self, line: str) -> Machine:
        data = line.split(" ")
        pattern = [ch == "#" for ch in data[0][1:-1]]
        buttons = []
        for s in data[1:-1]:
            button = [int(x) for x in s[1:-1].split(",")]
            buttons.append(button)
        return Machine(pattern=pattern, buttons=buttons)

    def find_solution(self, filename: str) -> int:
        result = 0
        with open(filename, "r") as file:
            for line in file.readlines():
                machine = self.parse_line(line.strip())
                result += machine.turn_on()
        return result


if __name__ == "__main__":
    filename = "inputs/d10.txt"
    print(Solution().find_solution(filename))
