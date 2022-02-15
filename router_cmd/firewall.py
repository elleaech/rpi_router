from router_cmd.worker import RTAPIDebian

SUCCESS = 0


class RTFireWall:
    def __init__(self) -> None:
        self._name = "firewalld"
        self._cmd = "firewall-cmd"
        self._worker = RTAPIDebian()

    def install(self) -> bool:
        self._worker.install(self._name)

    def allow_dhcp_traffic(self) -> bool:
        return_code = self._worker.do(f"{self._cmd} --add-service=dhcp --permanent")

        if SUCCESS == return_code:
            return True

    def enable_package_forwarding(self) -> bool:
        return_code = self._worker.do(f"{self._cmd} --add-masquerade --permanent")

        if SUCCESS == return_code:
            return True
