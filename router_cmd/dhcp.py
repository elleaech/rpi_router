from router_cmd.worker import Worker

SUCCESS = 0


class RTDhcp:
    def __init__(self) -> None:
        self._worker = Worker()
        self._name: str = ""


class RTDhcpServer(RTDhcp):
    pass


class RTDhcpClient(RTDhcp):
    def __init__(self) -> None:
        super().__init__(self)
        self._name = "dhcpcd"

    def disable(self) -> bool:
        return_code = self._worker.disable(self._name)
        return_code = self._worker.stop(self._name)

        if SUCCESS == return_code:
            return True
