class Electr:
    def __init__(self, name_in_file):
        self.distance = 0.0
        self.heights = []
        with open(name_in_file, 'r') as electr_in_file:
            self.distance = int(electr_in_file.readline())
            self.heights = list(map(int, electr_in_file.readline().split(" ")))

    def form_solutions(self):
        solutions = [-1 for i in range(len(self.heights) + 1)]
        solutions[0] = 0
        solutions[1] = self.heights[0]
        for i in range(2, len(self.heights) + 1):
            solutions[i] = max(solutions[i - 1], solutions[i - 2] + self.heights[i - 1])
        return solutions

    def reconstruct_solution(self):
        solutions = self.form_solutions()
        indices_to_include = []
        i = len(solutions) - 1
        while i >= 1:
            if solutions[i] == solutions[i - 1]:
                i -= 1
            else:
                indices_to_include.insert(0, i - 1)
                i -= 2
            
        return indices_to_include

    def calculate_length_of_lines(self, indices):
        heights = self.heights
        length_of_lines = 0

        for i in range(len(heights)):
            if i not in indices:
                heights[i] = 1

        for i in range(len(heights) - 1):            
            length_of_line = (self.distance**2 + (heights[i] - heights[i+1])**2)**(1/2)
            length_of_lines += length_of_line

        return round(length_of_lines, 2)


