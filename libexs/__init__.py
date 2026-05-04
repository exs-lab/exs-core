"""
Core Library for exs-shell and plugin
"""

__version__ = "0.0.1"
__author__ = "kipoha"  # only github usernames


try:
    import ignis  # noqa: F401
except ImportError:
    raise ImportError(
        "ignis is required but not installed.\n"
        "Install it with: pip install git+https://github.com/ignis-sh/ignis.git"
    )


from libexs import utils, register

__all__ = [
    "utils",
    "register",
]
