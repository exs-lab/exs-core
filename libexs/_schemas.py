from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field, fields

from typing import TYPE_CHECKING, Any

from libexs._types import Anchor
from libexs.enums.gtk.windows import Exclusivity, KeyboardMode, Layer

if TYPE_CHECKING:
    from libexs._types import AnyDict, AnyList


@dataclass
class Command:
    call: Callable[..., Any]
    args: AnyList = field(default_factory=list)
    kwargs: AnyDict = field(default_factory=dict)
    description: str = ""
    group: str = "base"


@dataclass
class ClipboardItem:
    id: str
    raw: str
    is_binary: bool


@dataclass
class WindowEntity:
    namespace: str
    monitor: int | None = None
    anchor: list[Anchor] | None = None
    exclusivity: Exclusivity = Exclusivity.NORMAL
    layer: Layer = Layer.TOP
    kb_mode: KeyboardMode = KeyboardMode.NONE
    popup: bool = False
    margin_bottom: int = 0
    margin_left: int = 0
    margin_right: int = 0
    margin_top: int = 0
    dynamic_input_region: bool = False
    extra: AnyDict = field(default_factory=dict)

    def __post_init__(self):
        standard_fields = {f.name for f in fields(self)}
        for k in list(vars(self).keys()):
            if k not in standard_fields:
                self.extra[k] = getattr(self, k)
                delattr(self, k)

    @classmethod
    def create(cls, **kwargs: Any) -> "WindowEntity":
        standard_fields = {f.name for f in fields(cls)}
        init_kwargs = {k: v for k, v in kwargs.items() if k in standard_fields}
        extra_kwargs = {k: v for k, v in kwargs.items() if k not in standard_fields}
        obj = cls(**init_kwargs)
        obj.extra.update(extra_kwargs)
        return obj

    def asdict(self) -> AnyDict:
        return {
            f.name: getattr(self, f.name) for f in fields(self) if f.name != "extra"
        } | self.extra
