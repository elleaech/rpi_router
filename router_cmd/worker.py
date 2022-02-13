import subprocess


class Worker:
    def __init__(self) -> None:
        self._process = subprocess

    def do(self, command: str) -> int:
        self._process.run(command)

    def install(self, package: str) -> int:
        if self._has_sudo():
            self._process.run(f"sudo apt-get -y install {package}")

    def _has_sudo(self) -> bool:
        return True
