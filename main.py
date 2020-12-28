import sys
from time import sleep

import sdl2.ext
from app.modules.cell import Cell
from app.modules.maze_generator import RandomizedKruskalMazeGenerator
from app.modules.window import Window

sdl2.ext.init()

ROWS = 10
COLUMNS = 10
SIZE = 50

window = Window(
    COLUMNS * SIZE + 3,
    ROWS * SIZE + 3
)

cells = [
    [
        Cell(x, y, SIZE)
        for x in range(COLUMNS)
    ]
    for y in range(ROWS)
]

maze_generator = RandomizedKruskalMazeGenerator(
    ROWS, COLUMNS, cells
)

while maze_generator.sets.size() != 1:
    maze_generator.generate()


def draw():
    surface = window.get_surface()

    sdl2.ext.fill(surface, 0)

    root = None

    # if maze_generator.sets.size() != 1:
    #     maze_generator.generate()
    # else:
    root = maze_generator.get_start()

    for row in cells:
        for cell in row:
            fill = False

            if root and root[0] == cell.x and root[1] == cell.y:
                fill = True

            cell.draw(surface, fill=fill)


def run():
    running = True

    while running:
        events = sdl2.ext.get_events()

        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

        draw()

        window.refresh()

        sleep(0.1)

    return 0


if __name__ == "__main__":
    sys.exit(run())
