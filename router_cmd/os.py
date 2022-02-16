from abc import ABC
import subprocess

SUCCESS = 0


class RTAPIOS(ABC):
    def __init__(self) -> None:
        self._process = subprocess

    def do(self, command: str) -> int:
        raise NotImplementedError

    def install(self, package: str) -> int:
        raise NotImplementedError

    def disable(self, service: str) -> int:
        raise NotImplementedError

    def enable(self, service: str) -> int:
        raise NotImplementedError

    def start(self, service: str) -> int:
        raise NotImplementedError

    def stop(self, service: str) -> int:
        raise NotImplementedError


class RTAPIDebian(RTAPIOS):
    def __init__(self) -> None:
        super().__init__()

    def do(self, command: str) -> int:
        self._process.run(command, shell=True)
        return SUCCESS

    def install(self, package: str) -> int:
        self.do(f"apt-get -y install {package}")
        return SUCCESS

    def disable(self, service: str) -> int:
        self.do(f"systemctl disable {service}")
        return SUCCESS

    def enable(self, service: str) -> int:
        self.do(f"systemctl enable {service}")
        return SUCCESS

    def start(self, service: str) -> int:
        self.do(f"systemctl start {service}")
        return SUCCESS

    def stop(self, service: str) -> int:
        self.do(f"systemctl stop {service}")
        return SUCCESS
