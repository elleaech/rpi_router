from router_data.addr import RTAddress


class RTFile:
    def __init__(self, addr: RTAddress, link_name: str, has_wpa: bool) -> None:
        self._name = link_name
        self._link_config = f"allow-hotplug {self._name}"
        self._interface = f"iface {self._name} inet static"

        self._address = f"{addr.address}"
        self._netmask = f"{addr.netmask}"
        self._gateway = f"{addr.gateway}"

        self._wpa_config = ""
        if has_wpa:
            self._wpa_config = f"wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf"

    def set_address(self) -> None:
        with open(f"{self._name}", "w") as link_file:
            link_file.write(self._link_config)
            link_file.write(self._interface)
            link_file.write(f"\t{self._address}")
            link_file.write(f"\t{self._netmask}")
            link_file.write(f"\t{self._gateway}")
            link_file.write(f"\t{self._wpa_config}")

    @property
    def name(self) -> str:
        return self._name
