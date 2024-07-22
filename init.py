"""Script to give termux an initial configiration."""
from utils.termux import extra_keys
from utils.termux.style import configure_colors, configure_font

from config import TERMUX


def initialize():
    """Initialize termux configurations."""
    TERMUX.mkdir(parents=True, exist_ok=True)
    configure_colors()
    configure_font()
    extra_keys.toggle(config=2)
    extra_keys.add_executable()


if __name__ == "__main__":
    initialize()
