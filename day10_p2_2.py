from ortools.linear_solver import pywraplp


class Machine:
    def __init__(self, pattern: list[int], buttons: list[list[int]]):
        self.pattern = pattern
        self.buttons = buttons

    def turn_on(self) -> int:
        n = len(self.pattern)
        k = len(self.buttons)
        solver = pywraplp.Solver.CreateSolver("CBC")
        upper_bound = sum(self.pattern)
        x = []
        for i in range(k):
            var = solver.IntVar(0, upper_bound, f"x_{i}")
            x.append(var)
        for j in range(n):
            vars_affecting_j = []
            for i in range(k):
                if j in self.buttons[i]:
                    vars_affecting_j.append(x[i])
            if not vars_affecting_j:
                continue
            solver.Add(sum(vars_affecting_j) == self.pattern[j])
        solver.Minimize(solver.Sum(x))
        status = solver.Solve()
        presses_per_button = [int(var.solution_value()) for var in x]
        return sum(presses_per_button)


class Solution:
    def parse_line(self, line: str) -> Machine:
        data = line.split(" ")
        pattern = [int(x) for x in data[-1][1:-1].split(",")]
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
                num = machine.turn_on()
                print(num)
                result += num
        return result


if __name__ == "__main__":
    filename = "inputs/d10.txt"
    print(Solution().find_solution(filename))
