import io
from pathlib import Path
from zipfile import ZipFile
import subprocess

import requests

from installers.pkg import PKGInstaller
from config import HOME


FONTS = HOME / ".fonts"


def download_fonts(url: str, file_path: str = ""):
    response = requests.get(url)
    FONTS.mkdir(parents=True, exist_ok=True)

    if file_path:
        font_file = FONTS / Path(file_path).name
        with ZipFile(io.BytesIO(response.content)) as zip_file:
            with zip_file.open(file_path) as font:
                font_file.write_bytes(font.read())
    else:
        font_file = FONTS / Path(url).name
        font_file.write_bytes(response.content)


def build_font_cache():
    command = ["fc-cache", "-f"]
    subprocess.run(command)


def install_fonts():
    PKGInstaller("fontconfig-utils")

    url = "https://download.jetbrains.com/fonts/JetBrainsMono-2.304.zip"
    file_path = "fonts/ttf/JetBrainsMono-Regular.ttf"
    download_fonts(url, file_path)

    url = "https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/Meslo/S/Regular/MesloLGSNerdFontMono-Regular.ttf"
    download_fonts(url)

    build_font_cache()
