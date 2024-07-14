"""Script to give termux an initial configiration."""
from initializer.extra_keys import add_executable, toggle_extra_keys
from initializer.style import configure_colors, configure_font


def initialize():
    """Initialize termux configurations."""
    configure_colors()
    configure_font()
    toggle_extra_keys()
    add_executable()


if __name__ == "__main__":
    initialize()
