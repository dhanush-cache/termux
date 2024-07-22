from installers.pkg import PKGInstaller
from utils.termux.env import add_env_variable
from .vnc import setup_vnc
from .style import install_fonts


def install_xfce4():
    """Installs the xfce4 desktop enviornment for termux."""
    PKGInstaller("x11-repo")
    PKGInstaller("tigervnc", "xfce4", "xfce4-terminal")

    setup_vnc()
    add_env_variable("DISPLAY", ":1")
    install_fonts()
