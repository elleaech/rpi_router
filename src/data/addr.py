class RTAddress:
    def __init__(self, netmask_bytes: int, *addr_byte: str) -> None:
        self._netmask_bytes = netmask_bytes
        self._network_bytes = list()
        self._addr_bytes = list()

    def _set_addr_bytes(self, *addr_byte: str):
        raise NotImplementedError

    def _set_network_bytes(self, netmask_bytes: int):
        raise NotImplementedError

    @property
    def address(self) -> str:
        raise NotImplementedError

    @property
    def network(self) -> str:
        raise NotImplementedError

    @property
    def netmask(self) -> str:
        raise NotImplementedError

    @property
    def broadcast(self) -> str:
        raise NotImplementedError

    @property
    def gateway(self) -> str:
        raise NotImplementedError


class RTIpv4Address(RTAddress):
    def __init__(self, netmask_bytes: int, *addr_byte: str) -> None:
        super().__init__(netmask_bytes, addr_byte)

        self._set_addr_bytes(*addr_byte)
        self._set_network_bytes(netmask_bytes)

    def _set_addr_bytes(self, *addr_byte: str):
        if len(addr_byte) != 4:
            print("INVALID PARAM!")
            raise
        for value in addr_byte:
            self._addr_bytes.append(value)

    def _set_network_bytes(self, netmask_bytes: int):
        if netmask_bytes > 3 or netmask_bytes < 1:
            print("INVALID PARAM!")
            raise

        self._network_bytes = self._addr_bytes.copy()
        for index in range(1, (4 - netmask_bytes) + 1):
            self._network_bytes[-index] = "0"

    def replace_end_byte(self, new_end_byte: int) -> str:
        bytes = self._network_bytes.copy()
        if new_end_byte >= 0 and new_end_byte < 255:
            bytes[-1] = str(new_end_byte)
        return ".".join(bytes)

    @property
    def address(self) -> str:
        return ".".join(self._addr_bytes)

    @property
    def network(self) -> str:
        return ".".join(self._network_bytes)

    @property
    def netmask(self) -> str:
        bytes = self._network_bytes.copy()
        for index, value in enumerate(bytes):
            if value != "0":
                bytes[index] = "255"
        return ".".join(bytes)

    @property
    def broadcast(self) -> str:
        bytes = self._network_bytes.copy()
        bytes[-1] = "255"
        return ".".join(bytes)

    @property
    def gateway(self) -> str:
        bytes = self._network_bytes.copy()
        bytes[-1] = "1"
        return ".".join(bytes)
