"""Module to configure extra keys that come along with the keyboard."""
from pathlib import Path
import subprocess

from initializer.utils import get_config, set_config, reload_termux_style
from installers.pkg import PKGInstaller


def toggle_extra_keys():
    """Toggles the presence of extra keys."""
    comment = "Default extra-key configuration"
    virtual_value = "extra-keys = [['ESC','/','-','HOME','UP','END','~'], ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','$']]"
    physical_value = "extra-keys = []"

    if get_config(comment) == virtual_value:
        set_config(comment, physical_value)
    else:
        set_config(comment, virtual_value)

    reload_termux_style()


def add_executable():
    """Adds a executable file to path to toggle the presence of extra keys."""
    PKGInstaller("ldd", "ccache")
    target = Path("/data/data/com.termux/files/usr/bin/ekeys")
    command = ["pyinstaller", "--onefile", "--distpath",
               str(target.parent), "--name", "ekeys", "initializer/extra_keys.py"]
    if not target.exists():
        subprocess.run(command)


def add_keybinding():
    """Adds a zsh keybinding to toggle the presence of extra keys."""
    script = """extra-keys() {
    ekeys
    zle accept-line
}
zle -N extra-keys
bindkey '^E' extra-keys
"""
    env_file = Path.home() / ".zshrc"

    if script not in env_file.read_text():
        with env_file.open("a") as file:
            file.write(script)


if __name__ == "__main__":
    toggle_extra_keys()
