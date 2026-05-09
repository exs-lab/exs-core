from collections.abc import Callable
from typing import TYPE_CHECKING, Any


if TYPE_CHECKING:
    core_property = property
else:
    from ignis.gobject import IgnisProperty

    core_property = IgnisProperty


class classproperty[_R]:
    def __init__(self, func: Callable[..., _R]) -> None:
        self.func: Callable[[type[Any]], _R] = func

    def __get__(self, _: Any, cls: type[Any]) -> _R:
        return self.func(cls)
