from typing import Protocol, runtime_checkable

from libexs.widgets.window import Revealer, RevealerWindow, Window


@runtime_checkable
class SupportsVisibility(Protocol):
    @property
    def visible(self) -> bool: ...

    @visible.setter
    def visible(self, value: bool) -> None: ...

    def set_visible(self, value: bool) -> None: ...


class HasRevealer(Protocol):
    @property
    def revealer(self) -> Revealer: ...
    @revealer.setter
    def revealer(self, value: Revealer): ...


class HasWindow[_W](Protocol):
    @property
    def window(self) -> _W: ...


class IWindow(HasWindow[Window], SupportsVisibility, Protocol): ...


class IRevealerWindow(
    SupportsVisibility,
    HasRevealer,
    HasWindow[RevealerWindow],
    Protocol,
): ...


class FileGTKObjProtocol(Protocol):
    def get_path(self) -> str: ...
