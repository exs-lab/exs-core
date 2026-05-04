from typing import Protocol, runtime_checkable


@runtime_checkable
class SupportsVisibility(Protocol):
    @property
    def visible(self) -> bool: ...

    @visible.setter
    def visible(self, value: bool) -> None: ...

    def set_visible(self, value: bool) -> None: ...


class HasRevealer(Protocol):
    @property
    def revealer(self) -> ...: ...
    @revealer.setter
    def revealer(self, value: ...): ...


class HasWindow(Protocol):
    @property
    def window(self) -> ...: ...


class IWindow(HasWindow, SupportsVisibility, Protocol): ...


class IRevealerWindow(
    SupportsVisibility,
    HasRevealer,
    HasWindow,
    Protocol,
): ...
