from libexs.protocols import IWindow
from libexs._state import State


def get_window(name: str) -> IWindow:
    return State.windows[name]
