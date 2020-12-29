import datetime
import random


class RandomizedDepthFirstSearchMazeGenerator:
    def __init__(self, rows, columns, cells):
        self.rows = rows
        self.columns = columns

        self.cells = cells
        self.stack = []

        random.seed(datetime.datetime.now())

        self.root = cells[0][0]
        self.root.visited = True

        self.stack.append(self.root)

    def _get_non_visited_neighbors(self, cell):
        x, y = cell.x, cell.y

        # TOP, RIGHT, BOTTOM, LEFT
        neighbors_local_coordinates = [(0, -1, 'U'), (1, 0, 'LA'), (0, 1, 'UA'), (-1, 0, 'L')]
        neighbors = []

        for neighbor_coordinates in neighbors_local_coordinates:
            neighbor_x = x + neighbor_coordinates[0]
            neighbor_y = y + neighbor_coordinates[1]
            neighbor_wall = neighbor_coordinates[2]

            if 0 <= neighbor_x <= self.columns - 1 and 0 <= neighbor_y <= self.rows - 1:
                cell = self.cells[neighbor_y][neighbor_x]

                if cell.visited:
                    continue

                neighbors.append(
                    (self.cells[neighbor_y][neighbor_x], neighbor_wall)
                )

        return neighbors

    def generate(self):
        current_cell = self.stack.pop()

        neighbors = self._get_non_visited_neighbors(
            current_cell
        )

        if len(neighbors) == 0:
            return

        self.stack.append(current_cell)

        neighbor, neighbor_wall = random.choice(neighbors)

        if neighbor_wall == 'U':
            current_cell.top = False

        if neighbor_wall == 'L':
            current_cell.left = False

        if neighbor_wall == 'LA':
            neighbor.left = False

        if neighbor_wall == 'UA':
            neighbor.top = False

        neighbor.visited = True

        self.stack.append(neighbor)

    def tick(self):
        return len(self.stack) != 0
