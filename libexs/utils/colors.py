from libexs.types import HEX, RGB, RGBA


def hex_to_rgb(hex_color: str) -> RGB:
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16) / 255
    g = int(hex_color[2:4], 16) / 255
    b = int(hex_color[4:6], 16) / 255
    return r, g, b


def rgb_to_hex(rgb_color: RGB) -> HEX:
    r = int(rgb_color[0] * 255)
    g = int(rgb_color[1] * 255)
    b = int(rgb_color[2] * 255)
    return f"#{r:02x}{g:02x}{b:02x}"


def hex_to_rgba(hex_color: str) -> RGBA:
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16) / 255
    g = int(hex_color[2:4], 16) / 255
    b = int(hex_color[4:6], 16) / 255
    a = int(hex_color[6:8], 16) / 255 if len(hex_color) == 8 else 1.0
    return r, g, b, a


def rgba_to_hex(rgba_color: RGBA) -> HEX:
    r = int(rgba_color[0] * 255)
    g = int(rgba_color[1] * 255)
    b = int(rgba_color[2] * 255)
    a = int(rgba_color[3] * 255)
    if a == 255:
        return f"#{r:02x}{g:02x}{b:02x}"
    return f"#{r:02x}{g:02x}{b:02x}{a:02x}"
