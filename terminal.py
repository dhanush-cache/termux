from installers.pkg import PKGInstaller
from zsh import ohmyzsh
from zsh import p10k
from utils import git


from config import HOME


def setup_terminal():
    PKGInstaller("zsh", "curl", "git")

    ohmyzsh.install_ohmyzsh()
    ohmyzsh.change_shell("zsh")
    ohmyzsh.ekeys_keybinding()
    ohmyzsh.fix_prompt_reset()

    url = "https://github.com/romkatv/powerlevel10k.git"
    path = HOME / ".oh-my-zsh" / "custom" / "themes" / "powerlevel10k"
    git.clone(url, path, shallow=True)
    ohmyzsh.set_theme("powerlevel10k/powerlevel10k")
    p10k.configure_p10k()

    url = "https://github.com/zsh-users/zsh-autosuggestions"
    path = HOME / ".oh-my-zsh" / "custom" / "plugins" / "zsh-autosuggestions"
    git.clone(url, path, shallow=True)
    ohmyzsh.add_plugin("zsh-autosuggestions")

    url = "https://github.com/zsh-users/zsh-syntax-highlighting.git"
    path = HOME / ".oh-my-zsh" / "custom" / "plugins" / "zsh-syntax-highlighting"
    git.clone(url, path, shallow=True)
    ohmyzsh.add_plugin("zsh-syntax-highlighting")


if __name__ == "__main__":
    setup_terminal()
