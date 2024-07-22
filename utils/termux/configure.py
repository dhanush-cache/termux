"""Several termux utility functions."""
from typing import Union
import re
import subprocess

from config import TERMUX


configs_file = TERMUX / "termux.properties"


def get_config(key: str) -> Union[str, None]:
    """Read a configuration from the properties file."""
    alt = f"### {key}\n\n###"
    configs = configs_file.read_text() if configs_file.exists() else alt
    pattern = fr"^### {key}$.*?^###"
    start = len(f"### {key}")
    end = len("###") * -1

    match = re.search(pattern, configs, flags=re.MULTILINE | re.DOTALL)
    return match.group()[start:end].strip() if match else None


def set_config(key: str, value: str):
    """Write a configuration to the properties file."""
    alt = f"### {key}\n\n###"
    configs = configs_file.read_text() if configs_file.exists() else alt
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
