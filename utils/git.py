import subprocess
from pathlib import Path


def clone(url: str, path: Path = Path.home(), shallow: bool = False):
    if path.exists():
        return

    command = ["git", "clone", url]
    if shallow:
        command.insert(2, "--depth=1")
    if path != Path.home():
        command.append(str(path))

    subprocess.run(command, check=True)


def config(key: str, value: str, level="global"):
    command = ["git", "config", f"--{level}", key, value]
    subprocess.run(command)
