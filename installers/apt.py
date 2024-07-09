"""Module to work with apt packages."""
from .installer import Installer


class APTInstaller(Installer):

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
        result = self._run(['apt', 'show', package])
        return result.returncode == 0

    def install(self, package: str) -> None:
        """Install a package."""
        self._run_with_check(['apt', 'install', '-y', package])
        print(f"Package {package} installed successfully.")

    def uninstall(self, package: str) -> None:
        """Uninstall a package."""
        self._run_with_check(['apt', 'remove', '-y', package])
        print(f"Package {package} uninstalled successfully.")

    def update(self) -> None:
        """Update the package list."""
        self._run_with_check(['apt', 'update'])
        print("Package list updated successfully.")

    def upgrade(self) -> None:
        """Upgrade all installed packages."""
        self._run_with_check(['apt', 'upgrade', '-y'])
        print("All packages upgraded successfully.")
