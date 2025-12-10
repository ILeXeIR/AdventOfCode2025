from sympy import Matrix, reduce_inequalities, And
from sympy.solvers.solveset import linsolve
from sympy.core.relational import Relational


class Machine:
    def __init__(self, pattern: list[int], buttons: list[list[int]]):
        self.pattern = Matrix(pattern)
        self.buttons = buttons
        self.matrix = self._get_matrix()

    def _get_matrix(self) -> Matrix:
        matrix = [[0] * len(self.buttons) for _ in range(len(self.pattern))]
        for i, button in enumerate(self.buttons):
            for j in button:
                matrix[j][i] = 1
        return Matrix(matrix)

    def turn_on(self) -> int:
        solutions = linsolve((self.matrix, self.pattern))
        # print(solutions)
        solution_tuple = list(solutions)[0]
        params = list(set().union(*[expr.free_symbols for expr in solutions]))
        # print("Params:", params)
        if not params:
            return sum([expr for expr in solution_tuple])
        param_ranges = self.extract_params_ranges(params, solution_tuple)
        # print("Ranges:", param_ranges)
        min_sum = float("inf")
        subs_dict = {key: bound[0] for key, bound in param_ranges.items()}
        prev = []
        while True:
            evaluated = [expr.subs(subs_dict) for expr in solution_tuple]
            if all([num >= 0 and num.is_integer for num in evaluated]):
                min_sum = min(min_sum, sum(evaluated))
                if prev and sum(evaluated) > sum(prev):
                    subs_dict[params[0]] = param_ranges[params[0]][1]
            if subs_dict[params[0]] != param_ranges[params[0]][0]:
                for i in range(len(evaluated)):
                    if evaluated[i] < 0 and evaluated[i] < prev[i]:
                        subs_dict[params[0]] = param_ranges[params[0]][1]
            for i, item in enumerate(subs_dict.items()):
                key, value = item
                if value < param_ranges[key][1]:
                    subs_dict[key] += 1
                    break
                if i == len(subs_dict) - 1:
                    return min_sum
                subs_dict[key] = param_ranges[key][0]
            prev = evaluated.copy()

    def extract_params_ranges(self, params, solution_tuple) -> dict:
        bounds = {p: [-100, 100] for p in params}
        inequalities = [expr >= 0 for expr in solution_tuple]
        ineq = None
        for param in params:
            try:
                ineq = reduce_inequalities(inequalities, [param])
                break
            except NotImplementedError:
                pass
        if not ineq:
            return bounds
        clauses = []
        if isinstance(ineq, And):
            clauses = list(ineq.args)
        else:
            clauses = [ineq]
        for clause in clauses:
            if not isinstance(clause, Relational):
                continue
            lhs, rhs = clause.lhs, clause.rhs
            for p in params:
                def is_numeric(expr):
                    return expr.free_symbols.isdisjoint(params)
                if lhs == p and is_numeric(rhs):
                    low, up = bounds[p]
                    if clause.rel_op in ('>=', '>'):
                        low = max(low, rhs)
                    elif clause.rel_op in ('<=', '<'):
                        up = min(up, rhs)
                    bounds[p] = (low, up)
                elif rhs == p and is_numeric(lhs):
                    low, up = bounds[p]
                    if clause.rel_op in ('<=', '<'):
                        low = max(low, lhs)
                    elif clause.rel_op in ('>=', '>'):
                        up = min(up, lhs)
                    bounds[p] = (low, up)
        return bounds


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
