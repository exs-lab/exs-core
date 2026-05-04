from collections.abc import Callable
from typing import Any


class classproperty[R]:
    def __init__(self, func: Callable[..., R]) -> None:
        self.func: Callable[[type[Any]], R] = func

    def __get__(self, _: Any, cls: type[Any]) -> R:
        return self.func(cls)
