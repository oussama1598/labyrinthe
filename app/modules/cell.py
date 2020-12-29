import sdl2.ext

from sdl2.examples.gui import RED
from app.helpers.colors import WHITE, BLUE


class Cell:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        self.top = True
        self.left = True

        self.fill = None
        self.visited = False

    def fill(self, color=RED):
        self.fill = color

    def draw(self, surface):
        if self.visited:
            sdl2.ext.fill(surface, BLUE, (self.x * self.size, self.y * self.size, self.size, self.size))

        if self.fill:
            sdl2.ext.fill(surface, self.fill, (self.x * self.size, self.y * self.size, self.size, self.size))

        if self.top:
            x1 = self.size * self.x
            y1 = self.size * self.y

            x2 = self.size * (self.x + 1)

            sdl2.ext.line(surface, WHITE, (x1, y1, x2, y1))

        if self.left:
            x1 = self.size * self.x
            y1 = self.size * self.y

            y2 = self.size * (self.y + 1)

            sdl2.ext.line(surface, WHITE, (x1, y1, x1, y2))