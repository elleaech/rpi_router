class RTIpAddress:
    def __init__(self, netmask_bytes: int, *addr_byte: str) -> None:
        self._netmask_bytes = 0
        self._network_bytes = list()
        self._addr_bytes = [0, 0, 0, 0]

        self._set_addr_bytes(*addr_byte)
        self._set_netmask_bytes(netmask_bytes)
        self._set_network_bytes(self._netmask_bytes)

    def _set_addr_bytes(self, *addr_byte: str):
        if len(addr_byte) != 4:
            print("INVALID PARAM!")
            raise
        for index, value in enumerate(addr_byte):
            self._addr_bytes[index] = value

    def _set_netmask_bytes(self, netmask_bytes: int):
        if netmask_bytes > 3 or netmask_bytes < 1:
            print("INVALID PARAM!")
            raise
        self._netmask_bytes = netmask_bytes

    def _set_network_bytes(self, netmask_bytes: int):
        self._network_bytes = self._addr_bytes.copy()

        for index in range(1, (4 - netmask_bytes) + 1):
            self._network_bytes[-index] = "0"

    @property
    def address(self) -> str:
        addr = ".".join(self._addr_bytes)
        return addr

    @property
    def network(self) -> str:
        addr = ".".join(self._network_bytes)
        return addr

    @property
    def netmask(self) -> str:
        bytes = self._network_bytes.copy()
        for index, value in enumerate(bytes):
            if value != "0":
                bytes[index] = "255"
        addr = ".".join(bytes)
        return addr

    @property
    def broadcast(self) -> str:
        bytes = self._network_bytes.copy()
        bytes[-1] = "255"
        addr = ".".join(bytes)
        return addr

    @property
    def gateway(self) -> str:
        bytes = self._network_bytes.copy()
        bytes[-1] = "1"
        addr = ".".join(bytes)
        return addr
