"""Module to configure extra keys that come along with the keyboard."""
from pathlib import Path
import subprocess

from utils.termux.configure import get_config, set_config, reload_termux_style
from installers.pkg import PKGInstaller
from installers.pip import PIPInstaller
from config import BIN, HOME


ZSHRC = HOME / ".zshrc"


def toggle(config: int = 0):
    """Toggles the presence of extra keys."""
    comment = "Default extra-key configuration"
    configs = [
        "extra-keys = [['ESC','/','-','HOME','UP','END','~'], ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','$']]",
        "extra-keys = []"
    ]

    alternate = 1 if get_config(comment) == configs[0] else 0
    index = config - 1 if config else alternate

    if get_config(comment) == configs[index]:
        return

    set_config(comment, configs[index])
    reload_termux_style()


def add_executable():
    """Adds a executable file to path to toggle the presence of extra keys."""
    PKGInstaller("ldd", "binutils")
    PIPInstaller("pyinstaller")
    target = BIN / "ekeys"

    script_file = __name__.replace(".", "/") + ".py"
    command = ["pyinstaller", "--onefile", "--noconfirm", "--distpath",
               str(target.parent), "--name", "ekeys", script_file]

    if not target.exists():
        subprocess.run(command)


if __name__ == "__main__":
    toggle()
