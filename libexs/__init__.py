"""
Core Library for exs-shell and plugin
"""

__version__ = "0.0.2"
__author__ = "kipoha"  # only github usernames


try:
    import ignis as _  # noqa: F401
except ImportError:
    raise ImportError(
        "ignis is required but not installed.\n"
        "Install it with: pip install git+https://github.com/ignis-sh/ignis.git"
    )


from libexs import utils, register, widgets, settings

__all__ = [
    "utils",
    "register",
    "widgets",
    "settings",
]
