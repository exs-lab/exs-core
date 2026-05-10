NAMESPACE_PREFIX = "libexs"


def gen_namespace(*args: str) -> str:
    return ".".join([NAMESPACE_PREFIX] + list(args))
