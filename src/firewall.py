from .os import RTAPIDebian, SUCCESS


class RTFireWall:
    def __init__(self) -> None:
        self._name = "firewalld"
        self._cmd = "firewall-cmd"
        self._worker = RTAPIDebian()

    def install(self) -> bool:
        if SUCCESS == self._worker.install(self._name):
            return True
        return False

    def allow_dhcp_traffic(self) -> bool:
        if SUCCESS == self._worker.do(f"{self._cmd} --add-service=dhcp --permanent"):
            return True
        return False

    def enable_package_forwarding(self) -> bool:
        if SUCCESS == self._worker.do(f"{self._cmd} --add-masquerade --permanent"):
            return True
        return False
