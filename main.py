import sys
from time import sleep

import sdl2.ext
from app.modules.cell import Cell
from app.modules.maze_generator import RandomizedDepthFirstSearchMazeGenerator
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

maze_generator = RandomizedDepthFirstSearchMazeGenerator(
    ROWS, COLUMNS, cells
)


def draw():
    surface = window.get_surface()

    sdl2.ext.fill(surface, 0)

    if maze_generator.tick():
        maze_generator.generate()

    for row in cells:
        for cell in row:
            cell.draw(surface)


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
