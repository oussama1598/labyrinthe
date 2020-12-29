import sys
from time import sleep

import sdl2.ext

from app.helpers.colors import WHITE, RED, GREEN
from app.modules.cell import Cell
from app.modules.maze_generator import RandomizedDepthFirstSearchMazeGenerator
from app.modules.maze_solver_a_star import AStarMazeSolver
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

START = cells[0][0]
END = cells[-1][-1]

maze_generator = RandomizedDepthFirstSearchMazeGenerator(
    ROWS, COLUMNS, cells
)

maze_solver = AStarMazeSolver(
    ROWS, COLUMNS, cells,
    START, END
)

while maze_generator.tick():
    maze_generator.generate()


def clean_cells():
    for row in cells:
        for cell in row:
            cell.visited = False


clean_cells()

finished = False


def draw():
    global finished

    surface = window.get_surface()

    sdl2.ext.fill(surface, 0)

    if maze_generator.tick():
        maze_generator.generate()
    elif maze_solver.tick():
        if not finished:
            finished = True

            clean_cells()

        maze_solver.solve()
    else:
        maze_solver.construct_path()

    # if maze_solver.tick():
    #     maze_solver.solve()
    # else:
    #     maze_solver.construct_path()

    for row in cells:
        for cell in row:
            if cell in maze_solver.path:
                cell.fill(color=GREEN)

            if cell == START or cell == END:
                cell.fill(color=RED)

            cell.draw(surface)

    # Add boundaries

    # Right wall
    sdl2.ext.line(surface, WHITE, (COLUMNS * SIZE, 0, COLUMNS * SIZE, ROWS * SIZE))

    # Bottom wall
    sdl2.ext.line(surface, WHITE, (0, COLUMNS * SIZE, COLUMNS * SIZE, ROWS * SIZE))


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
