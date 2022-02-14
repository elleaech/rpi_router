class RTIpAddress:
    def __init__(self, f_byte: str, s_byte: str, t_byte: str, l_byte: str) -> None:
        self.f_byte = f_byte
        self.s_byte = s_byte
        self.t_byte = t_byte
        self.l_byte = l_byte

    @property
    def address(self) -> str:
        return f"{self._f_byte}.{self._s_byte}.{self._t_byte}.{self._l_byte}"

    @property
    def network(self) -> str:
        return f"{self._f_byte}.{self._s_byte}.{self._t_byte}.0"

    @property
    def netmask(self) -> str:
        return "255.255.255.0"

    @property
    def broadcast(self) -> str:
        return f"{self._f_byte}.{self._s_byte}.{self._t_byte}.255"

    @property
    def gateway(self) -> str:
        return f"{self._f_byte}.{self._s_byte}.{self._t_byte}.1"
