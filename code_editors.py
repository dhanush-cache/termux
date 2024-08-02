import subprocess

from installers.pkg import PKGInstaller
from installers.vscode import VSCodeExtension
from config import BIN, HOME
from utils import git


def install_code_oss():
    PKGInstaller("tur-repo")
    PKGInstaller("code-oss")

    code_oss_binary = BIN / "code-oss"
    code_binary = BIN / "code"
    if code_oss_binary.exists() and not code_binary.exists():
        code_oss_binary.rename(code_binary)

    extensions = [
        "dracula-theme.theme-dracula",
        "PKief.material-icon-theme",
        "GitHub.github-vscode-theme",
        "esbenp.prettier-vscode",
        "EditorConfig.EditorConfig",
        "eamodio.gitlens",
        "mhutchie.git-graph",
        "ms-python.python",
        "ms-pyright.pyright",
        "ms-python.autopep8",
        "formulahendry.code-runner",
        "mkhl.shfmt",
        "timonwong.shellcheck",
        "foxundermoon.shell-format",
        "ms-vscode.cpptools",
    ]
    VSCodeExtension(*extensions)


def install_neovim():
    PKGInstaller("neovim", "build-essential", "nodejs-lts", "python-pip", "clang")
    url = "https://github.com/NvChad/starter"
    path = HOME/".config"/"nvim" 
    git.clone(url, path, shallow=True)
    command = ["nvim", "--headless", "-c", "q"]
    subprocess.run(command)