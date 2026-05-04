from __future__ import annotations
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from libexs._schemas import Command


type Anchor = Literal["left", "right", "top", "bottom"]
type TopBottom = Literal["top", "bottom"]
type EntryPosition = Literal["top", "center", "bottom"]
type Arrow = Literal[
    "top",
    "top_left",
    "top_right",
    "bottom_left",
    "bottom_right",
    "bottom",
    "left",
    "right",
]
type Align = Literal["top", "bottom", "left", "right"]
type OSD = Literal["arc", "scale"]
type AnyDict = dict[str, Any]
type AnyList = list[Any]
type Commands = dict[str, dict[str, Command]]
type RGB = tuple[float, float, float]
type RGBA = tuple[float, float, float, float]
type HEX = str
type CavaOutput = Literal["text", "values"]
type IconSize = Literal["xs", "s", "m", "l", "xl", "xxl", "xxxl"]
type IconType = Literal["Outlined", "Rounded", "Sharp"]
type SystemSizeUnit = Literal["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
type ProcessSortBy = Literal["cpu", "memory", "pid", "name"]
