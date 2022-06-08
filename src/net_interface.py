from .data.addr import RTIpv4Address


class RTNetInterface:
    def __init__(self, addr: RTIpv4Address, link_type: str, has_wpa: bool = True) -> None:
        self._link_t = link_type
        self._link_config = f"allow-hotplug {self._link_t}"
        self._interface = f"iface {self._link_t} inet static"

        self._address = f"{addr.address}"
        self._netmask = f"{addr.netmask}"
        self._gateway = f"{addr.gateway}"
        self._broadcast = f"{addr.broadcast}"

        self._wpa_config = ""
        if has_wpa:
            self._wpa_config = f"wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf"

    def set_interface(self) -> None:
        interfaces_dir = "/etc/network/interfaces.d/"
        with open(f"{interfaces_dir}{self._link_t}", "w") as link_file:
            link_file.write(f"{self._link_config}\n")
            link_file.write(f"{self._interface}\n")
            link_file.write(f"\taddress {self._address}\n")
            link_file.write(f"\tnetmask {self._netmask}\n")
            link_file.write(f"\tgateway {self._gateway}\n")
            link_file.write(f"\tbroadcast {self._broadcast}\n")
            link_file.write(f"\t{self._wpa_config}\n")

    @property
    def link_t(self) -> str:
        return self._link_t
