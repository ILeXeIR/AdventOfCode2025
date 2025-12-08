import heapq


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z


class Solution:
    def parse_input(self, filename: str) -> list[Point]:
        with open(filename, "r") as file:
            return [Point(*(int(num) for num in line.strip().split(","))) for line in file.readlines()]

    def find_solution(self, filename: str) -> int:
        points = self.parse_input(filename)
        heap_distances = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                distance = self.get_distance_square(points[i], points[j])
                heapq.heappush(heap_distances, (distance, (i, j)))
        circuits = []
        for _ in range(1000):
            distance, nums = heapq.heappop(heap_distances)
            self.add_in_circuits(circuits, nums[0], nums[1])
        lengths = sorted([len(x) for x in circuits], reverse=True)
        return lengths[0] * lengths[1] * lengths[2]

    def get_distance_square(self, p1: Point, p2: Point) -> int:
        return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2

    def add_in_circuits(self, circuits: list[set[int]], p1: int, p2: int):
        i = self.get_circuit_num(circuits, p1)
        j = self.get_circuit_num(circuits, p2)
        if i == -1 and j == -1:
            circuits.append(set((p1, p2)))
        elif i == j:
            return
        elif i == -1:
            circuits[j].add(p1)
        elif j == -1 :
            circuits[i].add(p2)
        else:
            circuits[i].update(circuits[j])
            circuits.pop(j)

    def get_circuit_num(self, circuits: list[set[int]], num: int) -> int:
        for i, circuit in enumerate(circuits):
            if num in circuit:
                return i
        return -1


if __name__ == "__main__":
    filename = "inputs/d8.txt"
    print(Solution().find_solution(filename))
