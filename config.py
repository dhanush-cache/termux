from pathlib import Path
import os


ROOT = Path("/")
HOME = Path.home()
prefix = os.getenv("PREFIX")
PREFIX = Path(prefix) if prefix else ROOT
BIN = PREFIX / "bin"
ETC = PREFIX / "etc"
TERMUX = HOME / ".termux"

for key, value in os.environ.items():
    if "/.termux" in value.lower():
        print(key, value)
