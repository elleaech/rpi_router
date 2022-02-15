from router_data.addr import RTIpAddress


class RTNetFile:
    def __init__(self, addr: RTIpAddress, file_name: str, has_wpa: bool) -> None:
        self._link_t = file_name
        self._link_config = f"allow-hotplug {self._link_t}"
        self._interface = f"iface {self._link_t} inet static"

        self._raw_address = addr
        self._address = f"{self._raw_address.address}"
        self._netmask = f"{self._raw_address.netmask}"
        self._gateway = f"{self._raw_address.gateway}"

        self._wpa_config = ""
        if has_wpa:
            self._wpa_config = f"wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf"

    def set_address(self) -> None:
        with open(f"{self._link_t}", "w") as link_file:
            link_file.write(f"{self._link_config}\n")
            link_file.write(f"{self._interface}\n")
            link_file.write(f"\t{self._address}\n")
            link_file.write(f"\t{self._netmask}\n")
            link_file.write(f"\t{self._gateway}\n")
            link_file.write(f"\t{self._wpa_config}\n")

    @property
    def name(self) -> str:
        return self._link_t
