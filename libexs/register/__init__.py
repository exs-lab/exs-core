from libexs._state import State
from libexs.types import AnyDict
from libexs.register.cmd import command, commands
from libexs.register.deco import add_post_init
from libexs.register.events import event
from libexs.register import events


def _register(cls: type, registry: AnyDict) -> type:
    def register(self):
        key = cls.__name__.lower()
        if key in registry:
            raise ValueError(f"{key} already registered")
        registry[key] = self

    add_post_init(cls, register)
    return cls


def widget(cls: type) -> type:
    return _register(cls, State.widgets)


def window(cls: type) -> type:
    return _register(cls, State.windows)


def service(cls: type) -> type:
    return _register(cls, State.services)


__all__ = [
    "widget",
    "service",
    "window",
    "event",
    "events",
    "command",
    "commands",
]
