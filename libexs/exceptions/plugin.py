from libexs.exceptions.base import LibException


class PluginError(LibException):
    pass


class PluginNotFoundError(PluginError):
    pass


class PluginLoadError(PluginError):
    pass


class PluginValidationError(PluginError):
    pass
