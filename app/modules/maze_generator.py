import datetime
import random

from app.modules.disjoint_set import DisjointSets


class RandomizedKruskalMazeGenerator:
    def __init__(self, rows, columns, cells):
        random.seed(datetime.datetime.now())

        self.cells = cells

        self.vertices = []
        self.edges = []

        for i in range(columns):
            for j in range(rows):
                self.vertices.append((i, j))

                self.edges.append((i, j, 'U'))
                self.edges.append((i, j, 'L'))

        self.sets = DisjointSets(self.vertices)

    def generate(self):
        if len(self.edges) == 0:
            return

        edge = random.choice(self.edges)

        self.edges.remove(edge)

        i = edge[0]
        j = edge[1]
        position = edge[2]

        if i > 0 and position == 'L' and self.sets.root((i, j)) != self.sets.root((i - 1, j)):
            self.sets.union((i, j), (i - 1, j))

            self.cells[i][j].left = False

        if j > 0 and position == 'U' and self.sets.root((i, j)) != self.sets.root((i, j - 1)):
            self.sets.union((i, j), (i, j - 1))

            self.cells[i][j].top = False

    def get_start(self):
        for item in self.sets.sets_list:
            if item.parent != item:
                return item.root().data
