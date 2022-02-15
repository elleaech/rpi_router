from router_cmd.os import RTAPIDebian, SUCCESS


class RTDhcpServer:
    def __init__(self, service_name: str) -> None:
        self._worker = RTAPIDebian()
        self._name: str = service_name

    def install(self) -> bool:
        self._worker.install(self._name)

    def enable(self) -> bool:
        return_code = self._worker.enable(self._name)
        return_code = self._worker.start(self._name)

        if SUCCESS == return_code:
            return True


class RTDhcpClient:
    def __init__(self, service_name: str) -> None:
        self._worker = RTAPIDebian()
        self._name: str = service_name

    def disable(self) -> bool:
        return_code = self._worker.disable(self._name)
        return_code = self._worker.stop(self._name)

        if SUCCESS == return_code:
            return True
