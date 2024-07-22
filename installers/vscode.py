"""Module to work with vscode extensions."""
import json
from tempfile import NamedTemporaryFile

import requests
import bs4
from bs4 import BeautifulSoup

from .installer import Installer


class VSCodeExtension(Installer):
    def is_installed(self, package: str) -> bool:
        """Check if a package is installed."""
        result = self._run(['code', '--list-extensions'])
        return package.lower() in result.stdout.lower().split("\n")

    def __get_json(self, package: str) -> dict:
        publisher, ext_name = package.split(".")
        url = f"https://marketplace.visualstudio.com/items?itemName={publisher}.{ext_name}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        selectors = {'class': 'jiContent', 'type': 'application/json'}
        script_tag = soup.find('script', selectors)

        if not (isinstance(script_tag, bs4.element.Tag) and script_tag.string):
            return {}

        return json.loads(script_tag.string)

    def __get_download_url(self, package: str) -> str:
        data = self.__get_json(package)

        target_platform = "linux-arm64"
        version = data["Resources"]["Version"]
        publisher = data["Resources"]["PublisherName"]
        ext_name = data["Resources"]["ExtensionName"]
        platforms = data["WorksWith"][0].split(", ")

        platform_alias = data["TargetPlatforms"][target_platform]
        is_universal = "Universal" in platforms
        supports_linux = is_universal or (platform_alias in platforms)

        url = f"https://marketplace.visualstudio.com/_apis/public/gallery/publishers/{publisher}/vsextensions/{ext_name}/{version}/vspackage"
        text = f"Downloading {publisher}.{ext_name} for Universal"
        if not is_universal and supports_linux:
            query_string = f"?targetPlatform={target_platform}"
            url += query_string
            text = f"Downloading {publisher}.{ext_name} for {target_platform}"
        print(text)
        return url

    def manual_install(self, package: str) -> None:
        url = self.__get_download_url(package)
        file = NamedTemporaryFile(suffix=".vsix", delete=False)
        response = requests.get(url)
        file.write(response.content)
        self.install(file.name)

    def install(self, package: str, force=False) -> None:
        print("Installing:", package)
        """Install a package."""
        result = self._run(['code', '--install-extension', package])
        if result.returncode != 0 or force:
            self.manual_install(package)

    def uninstall(self, package: str) -> None:
        """Uninstall a package."""
        self._run_with_check(['code', '--uninstall-extension', package])


if __name__ == "__main__":
    ...
