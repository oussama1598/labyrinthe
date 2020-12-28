import sdl2.ext


class Window:
    def __init__(self, width, height):
        self.window = sdl2.ext.Window('Labyrinthe', size=(width, height))

        self.window.show()

    def refresh(self):
        self.window.refresh()

    def get_surface(self):
        return self.window.get_surface()
