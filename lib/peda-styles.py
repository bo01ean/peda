import os

def setup_colors():
    colorcodes = {
        # Addresses
        "data": "blue",
        "code": "red",
        "rodata": "green",
        # opcodes
        "cmp": "red",
        "test": "red",
        "call": "green",
        "j": "yellow", # jump
        "ret": "blue",
        # context
        "VULN_FUNCTIONS": "red",
        "TARGET": "green"
    }

    styles = {
        "VULN_FUNCTIONS": "bold, underline",
        "BEFORE_TARGET": "dark",
        "TARGET": "bold",
        "COMMENT": "dark"
    }

    for color in colorcodes:
        os.environ['PEDA_COLORS_' + color.upper()] = colorcodes[color]
    for style in styles:
        os.environ['PEDA_STYLES_' + style.upper()] = styles[style]


setup_colors()
