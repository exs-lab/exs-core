from collections.abc import Sequence
from ignis.base_service import BaseService

from libexs._core import core_property
from libexs.compositor.abc_core import (
    CompositorInterface,
    CompositorMonitor,
    CompositorWindow,
    CompositorWorkspace,
)


class CompositorService(BaseService):
    def __init__(self, compositor: CompositorInterface) -> None:
        super().__init__()
        self._compositor = compositor
        self._compositor.on_workspace_changed(self._on_workspace_changed)
        self._compositor.on_window_focused(self._on_window_focused)
        self._compositor.on_layout_changed(self._on_layout_changed)

    @core_property
    def compositor_name(self) -> str:
        return self._compositor.compositor_name

    @core_property
    def workspaces(self) -> Sequence[CompositorWorkspace]:
        return self._compositor.workspaces()

    @core_property
    def windows(self) -> Sequence[CompositorWindow]:
        return self._compositor.windows()

    @core_property
    def monitors(self) -> Sequence[CompositorMonitor]:
        return self._compositor.monitors()

    @core_property
    def active_monitor(self) -> CompositorMonitor:
        return self._compositor.active_monitor()

    @core_property
    def active_keyboard_layout(self) -> str:
        return self._compositor.active_keyboard_layout

    def switch_to_workspace(self, _id: int) -> None:
        self._compositor.switch_to_workspace(_id)

    def focus_window(self, window_id: int) -> None:
        self._compositor.focus_window(window_id)

    def close_window(self, window_id: int) -> None:
        self._compositor.close_window(window_id)

    def _on_workspace_changed(self) -> None:
        self.notify("workspaces")

    def _on_window_focused(self) -> None:
        self.notify("windows")

    def _on_layout_changed(self) -> None:
        self.notify("active_keyboard_layout")
