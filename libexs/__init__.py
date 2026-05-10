"""
Core Library for exs-shell and plugin
"""

__version__ = "0.1.5"
__author__ = "kipoha"  # only github usernames


try:
    import ignis as _  # noqa: F401
except ImportError:
    raise ImportError(
        "ignis is required but not installed.\n"
        "Install it with: pip install git+https://github.com/ignis-sh/ignis.git"
    )


from libexs._core import classproperty, coreproperty
from libexs._state import State
from libexs import utils, register, widgets, settings, types as core_types

__all__ = [
    "utils",
    "register",
    "widgets",
    "settings",
    "State",
    "classproperty",
    "core_types",
    "coreproperty",
]
