from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field

from typing import TYPE_CHECKING, Any

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
