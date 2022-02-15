from router_cmd.worker import RTAPIDebian

SUCCESS = 0


class RTDhcp:
    def __init__(self, service_name: str) -> None:
        self._worker = RTAPIDebian()
        self._name: str = service_name


class RTDhcpServer(RTDhcp):
    pass


class RTDhcpClient(RTDhcp):
    def __init__(self, service_name: str) -> None:
        super().__init__(service_name)

    def disable(self) -> bool:
        return_code = self._worker.disable(self._name)
        return_code = self._worker.stop(self._name)

        if SUCCESS == return_code:
            return True
