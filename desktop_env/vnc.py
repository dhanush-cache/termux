from os import devnull
import re

from config import BIN, HOME


SHEBANG = "#!/data/data/com.termux/files/usr/bin/sh"
GEOMETRY = "2408x1080"
PORT = ":1"
VNC = HOME / ".vnc"


def define_xstartup():
    startup_file = VNC / "xstartup"
    text = f"{SHEBANG}\nxfce4-session &\n"
    startup_file.parent.mkdir(parents=True, exist_ok=True)
    startup_file.write_text(text)
    startup_file.chmod(0o755)


def define_config():
    config_file = VNC / "config"
    config = config_file.read_text() if config_file.exists() else ""
    pattern = r"^.*?geometry=.*?$"
    repl = f"geometry={GEOMETRY}"
    config = re.sub(pattern, repl, config, flags=re.MULTILINE)
    if repl not in config:
        config += repl
    config_file.write_text(config)


def define_passwd():
    passwd_file = VNC / "passwd"
    passwd = b'I@\x15\xf9\xa3^\x8b"'
    passwd_file.write_bytes(passwd)


def add_executable(text: str, filename: str):
    executable = BIN / filename
    executable.write_text(text)
    executable.chmod(0o755)


def define_executables():
    start = f"vncserver {PORT} >{devnull} 2>&1"
    kill = f"{SHEBANG}\nvncserver -kill {PORT} >{devnull} 2>&1"

    text = f"{kill}\n{start}\n"
    add_executable(text, "vncstart")

    text = f"{kill}\n"
    add_executable(text, "vncstop")


def setup_vnc():
    define_xstartup()
    define_config()
    define_passwd()
    define_executables()
