import sys
import subprocess
import tomllib
import importlib.util
from pathlib import Path
from typing import Literal, overload

from ignis import utils
from ignis.base_service import BaseService
from ignis.css_manager import CssInfoPath, CssManager

from libexs import State
from libexs.schemas import PluginEntity
from libexs.exceptions.plugin import PluginLoadError, PluginValidationError
from libexs.settings.base import BaseCategory


def is_installed_deps(package: str) -> bool:
    name = package.split("==")[0].split(">=")[0].split("@")[0].strip().replace("-", "_")
    return importlib.util.find_spec(name) is not None


def install_deps(plugin_path: Path) -> None:
    """
    Install dependencies from plugin pyproject
    """
    pyproject = plugin_path / "pyproject.toml"

    with open(pyproject, "rb") as f:
        meta = tomllib.load(f)

    deps = meta.get("project", {}).get("dependencies", [])
    missing = [d for d in deps if not is_installed_deps(d)]
    if missing:
        subprocess.run([sys.executable, "-m", "pip", "install", *missing])


@overload
def check(path: Path, strict: Literal[True]) -> PluginEntity: ...
@overload
def check(path: Path, strict: Literal[False] = ...) -> PluginEntity | None: ...
def check(path: Path, strict: bool = False) -> PluginEntity | None:
    """
    Check if path is a valid plugin
    """
    if not path.is_dir():
        if strict:
            raise PluginValidationError(path.name, "not a directory")
        return None
    if path.name.startswith((".", "_")):
        return None

    toml_file = path / "plugin.toml"
    pyproject = path / "pyproject.toml"

    if not toml_file.exists() or not pyproject.exists():
        if strict:
            raise PluginValidationError(
                path.name, "missing plugin.toml or pyproject.toml"
            )
        return None

    with open(toml_file, "rb") as f:
        meta = tomllib.load(f)

    if meta.get("plugin", {}).get("shell") != "exs-shell":
        if strict:
            raise PluginValidationError(path.name, "is not an exs-shell plugin")
        return None

    plugin_meta = meta.get("plugin", {})
    module_name = plugin_meta.get("module") or path.name
    src = path / module_name

    if not (src / "__init__.py").exists():
        if strict:
            raise PluginValidationError(path.name, f"missing {module_name}/__init__.py")
        return None

    return PluginEntity(
        path=path,
        name=plugin_meta.get("name") or path.name,
        version=plugin_meta.get("version") or "0.0.0",
        module_name=module_name,
        dependencies=plugin_meta.get("dependencies", []),
    )


def apply_css(path: Path) -> None:
    """
    Apply css in shell
    """
    if path.exists():
        CssManager.get_default().apply_css(
            CssInfoPath(
                name=path.name.upper(),
                compiler_function=lambda path: utils.sass_compile(
                    path, compiler="sass"
                ),
                path=str(path),
            )
        )


def apply_service(service: BaseService, service_name: str) -> None:
    """
    Apply service
    """
    if service_name not in State.services:
        State.services[service_name] = service


def apply_settings_category(settings_category: BaseCategory) -> None:
    """
    Apply settings category
    """
    if not isinstance(State.get("plugin_settings"), list):
        State["plugin_settings"] = []
    State.plugin_settings.append(settings_category)


def get_service(service_name: str) -> BaseService | None:
    """
    Get service by name
    :return BaseService"""
    return getattr(State.services, service_name, None)


def load(path: Path) -> None:
    """
    Load a plugin
    """
    try:
        pl = check(path, True)
        if not pl:
            return
        src = pl.path / pl.module_name
        install_deps(pl.path)
        sys.path.insert(0, str(pl.path))
        spec = importlib.util.spec_from_file_location(
            pl.path.name,
            src / "__init__.py",
            submodule_search_locations=[str(src)],
        )

        if spec:
            mod = importlib.util.module_from_spec(spec)
            sys.modules[pl.path.name] = mod
            if loader := spec.loader:
                loader.exec_module(mod)
                if hasattr(mod, "init"):
                    mod.init()
    except Exception as e:
        raise PluginLoadError(path.name, e)
