class Solution:
    def __init__(self):
        self.shapes = []
        self.tasks = []
        self.pixels = []
        self.answers = {"yes": 0, "no": 0, "unknown": 0}

    def parse_input(self, filename: str):
        with open(filename, "r") as file:
            line = file.readline().strip()
            while line and line[-1] == ":":
                line = file.readline().strip()
                shape = []
                pixels = 0
                while line:
                    shape.append([ch for ch in line])
                    pixels += sum([ch == "#" for ch in shape[-1]])
                    line = file.readline().strip()
                self.shapes.append(shape)
                self.pixels.append(pixels)
                line = file.readline().strip()
            while line:
                data = line.split(": ")
                size = [int(x) for x in data[0].split("x")]
                quantities = [int(x) for x in data[1].split(" ")]
                self.tasks.append({
                    "size": size,
                    "quantities": quantities
                })
                line = file.readline().strip()


    def find_solution(self, filename: str) -> int:
        self.parse_input(filename)
        for task in self.tasks:
            self.able_to_fit_all(task)
        return self.answers["yes"]

    def able_to_fit_all(self, task: dict):
        n, m = task["size"]
        quantities = task["quantities"]
        field_area = n * m
        min_shapes_area = sum([quantities[i] * self.pixels[i] for i in range(len(quantities))])
        max_shapes_area = sum([quantities[i] * 9 for i in range(len(quantities))])
        if field_area < min_shapes_area:
            self.answers["no"] += 1
        elif field_area >= max_shapes_area:
            self.answers["yes"] += 1
        else:
            self.answers["unknown"] += 1


if __name__ == "__main__":
    filename = "inputs/d12.txt"
    print(Solution().find_solution(filename))
