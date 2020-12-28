import sdl2.ext

from app.helpers.colors import WHITE, RED


class Cell:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        self.top = True
        self.bottom = True
        self.left = True
        self.right = True

    def draw(self, surface, fill):
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

        if fill:
            sdl2.ext.fill(surface, RED, (self.x * self.size, self.y * self.size, self.size, self.size))
