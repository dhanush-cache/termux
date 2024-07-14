"""Module to configure termux styling."""
import json
import re

import requests

from initializer.utils import reload_termux_style, TERMUX_PATH


def configure_colors():
    """Apply the Argonaut color theme."""
    url = "https://raw.githubusercontent.com/Gogh-Co/Gogh/master/json/argonaut.json"
    response = requests.get(url)
    colors_file = TERMUX_PATH / "colors.properties"
    initial_data = colors_file.read_text()

    color_codes = json.loads(response.text)

    final_data = ""
    for key, value in color_codes.items():
        if key in ["name", "hash"]:
            continue
        if "color" in key:
            match = re.search(r"\d+", key)
            index = int(match.group()) - 1 if match else None
            key = f"color{index}"
        final_data += f"{key}={value.lower()}\n"
    if initial_data != final_data:
        colors_file.write_text(final_data)
        reload_termux_style()


def configure_font():
    """Install Meslo Nerd font"""
    url = "https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/Meslo/S/Regular/MesloLGSNerdFontMono-Regular.ttf"
    response = requests.get(url)
    font_file = TERMUX_PATH / "font.ttf"
    initial_data = font_file.read_bytes()
    final_data = response.content

    if initial_data != final_data:
        font_file.write_bytes(final_data)
        reload_termux_style()


if __name__ == "__main__":
    configure_colors()
    configure_font()
