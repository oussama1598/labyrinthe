def calculate_distance(cell1, cell2):
    return abs(cell1.x - cell2.x) + abs(cell1.y - cell2.y)


class AStarMazeSolver:
    def __init__(self, rows, columns, cells, start, end):
        self.rows = rows
        self.columns = columns
        self.root = start
        self.end = end

        self.cells = cells
        self.unvisited = []
        self.path = []

        self.root.visited = True
        self.unvisited.append(self.root)

        self.current_distances = [[float('inf') for _ in range(columns)] for _ in range(rows)]
        self.current_distances[self.root.y][self.root.x] = 0

        self.previous_cells = [[None for _ in range(columns)] for _ in range(rows)]

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
                neighbor_cell = self.cells[neighbor_y][neighbor_x]

                if neighbor_wall == 'U' and cell.top:
                    continue

                if neighbor_wall == 'L' and cell.left:
                    continue

                if neighbor_wall == 'UA' and neighbor_cell.top:
                    continue

                if neighbor_wall == 'LA' and neighbor_cell.left:
                    continue

                neighbors.append(
                    self.cells[neighbor_y][neighbor_x]
                )

        return neighbors

    def _get_cell_with_min_current_distance(self):
        return sorted(
            self.unvisited,
            key=lambda item: self.current_distances[item.y][item.y]
        )[0]

    def solve(self):
        current_cell = self._get_cell_with_min_current_distance()

        current_cell.visited = True

        self.unvisited.remove(current_cell)

        neighbors = self._get_non_visited_neighbors(
            current_cell
        )

        if len(neighbors) == 0:
            return

        for neighbor in neighbors:
            x = current_cell.x
            y = current_cell.y

            neighbor_x = neighbor.x
            neighbor_y = neighbor.y

            neighbor.visited = True

            current_distance = self.current_distances[y][x] + calculate_distance(current_cell,
                                                                                 neighbor)

            if current_distance < self.current_distances[neighbor_y][neighbor_x]:
                self.current_distances[neighbor_y][neighbor_x] = current_distance

                self.previous_cells[neighbor_y][neighbor_x] = current_cell

                self.unvisited.append(neighbor)

            if neighbor == self.end:
                self.unvisited = []
                break

    def tick(self):
        return len(self.unvisited) != 0

    def construct_path(self):
        if len(self.path) != 0:
            return

        current_cell = self.end

        while current_cell:
            self.path.append(current_cell)

            current_cell = self.previous_cells[current_cell.y][current_cell.x]
