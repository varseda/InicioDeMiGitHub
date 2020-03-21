from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("INICIO", font='big'),
            screen.height // 2 - 10),
        Cycle(
            screen,
            FigletText("GIT!", font='big'),
            screen.height // 2 - 3),
        Cycle(
            screen,
            FigletText("JOSE VARELA", font='big'),
            screen.height // 2 + 4),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)