"""Several termux utility functions."""
from pathlib import Path
from typing import Union
import re
import subprocess


TERMUX_PATH = Path.home() / ".termux"


def get_config(key: str) -> Union[str, None]:
    """Read a configuration from the properties file."""
    configs_file = TERMUX_PATH / "termux.properties"
    configs = configs_file.read_text()

    pattern = fr"^### {key}$.*?^###"
    start = len(f"### {key}")
    end = len("###") * -1
    match = re.search(pattern, configs, flags=re.MULTILINE | re.DOTALL)
    return match.group()[start:end].strip() if match else None


def set_config(key: str, value: str):
    """Write a configuration to the properties file."""
    configs_file = TERMUX_PATH / "termux.properties"
    configs = configs_file.read_text()

    pattern = fr"^### {key}$.*?^###"
    repl = f"### {key}\n{value}\n\n###"

    result = re.sub(pattern, repl, configs, flags=re.MULTILINE | re.DOTALL)
    configs_file.write_text(result)


def reload_termux_style():
    """Reload the termux app style for applying style changes."""
    command = [
        "am", "broadcast",
        "--user", "0",
        "-a", "com.termux.app.reload_style",
        "com.termux"
    ]
    subprocess.run(command, capture_output=True)
