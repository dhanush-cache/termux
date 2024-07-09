"""Module to work with termux packages."""
from .installer import Installer


class PKGInstaller(Installer):

    def __init__(self, *packages, force: bool = False) -> None:
        if not self.check(*packages):
            self.update()
            self.upgrade()
        super().__init__(*packages, force=force)

    def is_installed(self, package: str) -> bool:
        """Check if a package is installed."""
        result = self._run(['dpkg', '-s', package])
        return result.returncode == 0

    def exists(self, package: str) -> bool:
        """Check if a package is installed."""
        result = self._run(['pkg', 'show', package])
        return result.returncode == 0

    def install(self, package: str) -> None:
        """Install a package."""
        self._run_with_check(['pkg', 'install', '-y', package])
        print(f"Package {package} installed successfully.")

    def uninstall(self, package: str) -> None:
        """Uninstall a package."""
        self._run_with_check(['pkg', 'uninstall', '-y', package])
        print(f"Package {package} uninstalled successfully.")

    def update(self) -> None:
        """Update the package list."""
        self._run_with_check(['pkg', 'update', '-y'])
        print("Package list updated successfully.")

    def upgrade(self) -> None:
        """Upgrade all installed packages."""
        self._run_with_check(['pkg', 'upgrade', '-y'])
        print("All packages upgraded successfully.")
