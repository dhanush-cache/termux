from init import initialize
from terminal import setup_terminal
from desktop_env.xfce4 import install_xfce4
from code_editors import install_code_oss, install_neovim

initialize()
setup_terminal()
install_neovim()
install_xfce4()
install_code_oss()
