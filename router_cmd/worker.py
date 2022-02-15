import subprocess


class RTAPIDebian:
    def __init__(self) -> None:
        self._process = subprocess

    def do(self, command: str) -> int:
        self._process.run(command)

    def install(self, package: str) -> int:
        if self._has_sudo():
            self.do(f"apt-get -y install {package}")

    def disable(self, service: str) -> int:
        if self._has_sudo():
            self.do(f"systemctl disable {service}")

    def enable(self, service: str) -> int:
        if self._has_sudo():
            self.do(f"systemctl enable {service}")

    def start(self, service: str) -> int:
        if self._has_sudo():
            self.do(f"systemctl start {service}")

    def stop(self, service: str) -> int:
        if self._has_sudo():
            self.do(f"systemctl stop {service}")

    def _has_sudo(self) -> bool:
        return True
