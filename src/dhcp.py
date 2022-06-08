from .os import RTAPIDebian, SUCCESS
from .data.addr import RTIpv4Address


class RTDhcpServer:
    def __init__(self, gateway_addr: RTIpv4Address, gateway_link_t: str) -> None:
        self._worker = RTAPIDebian()
        self._name: str = "isc-dhcp-server"

        self._gateway_addr: RTIpv4Address = gateway_addr
        self._gateway_link_t: str = gateway_link_t

    def install(self) -> bool:
        if SUCCESS == self._worker.install(self._name):
            return True
        return False

    def enable(self) -> bool:
        if SUCCESS == self._worker.enable(self._name):
            if SUCCESS == self._worker.start(self._name):
                return True
        return False

    def configure(self) -> None:
        return_code = self._configure_dhcp_routing()
        return_code = self._configure_dhcp_interface()

        if SUCCESS == return_code:
            return True

    def _configure_dhcp_routing(self) -> int:
        file_name = f"/etc/dhcp/dhcpd.conf"

        with open(file_name, "w") as dhcp_conf:
            dhcp_conf.write("ddns-update-style none;\n")
            dhcp_conf.write("default-lease-time 600;\nmax-lease-time 7200;\n")

            domain_options = 'option domain-name "rpi.local";\noption domain-name-servers 8.8.8.8, 8.8.4.4;'
            dhcp_conf.write(f"{domain_options}\n")

            dhcp_conf.write(
                f"subnet {self._gateway_addr.network} netmask {self._gateway_addr.netmask} "
            )
            dhcp_conf.write("{\n")

            start_range = self._gateway_addr.replace_end_byte(2)
            end_range = self._gateway_addr.replace_end_byte(254)
            dhcp_conf.write(f"\trange {start_range} {end_range};\n")

            dhcp_conf.write(f"\toption routers {self._gateway_addr.gateway};\n")
            dhcp_conf.write(f"\toption subnet-mask {self._gateway_addr.netmask};\n")
            dhcp_conf.write("}\n")

        return SUCCESS

    def _configure_dhcp_interface(self) -> int:
        file_name = f"/etc/default/{self._name}"
        dhcp_interface = open(file_name, "r")

        new_lines = dhcp_interface.readlines()

        for line in new_lines:
            if line.startswith("INTERFACESv4"):
                index = new_lines.index(line)
                new_lines[index] = f'INTERFACESv4="{self._gateway_link_t}"\n'

        dhcp_interface.close()

        with open(file_name, "w") as dhcp_interface:
            dhcp_interface.write("".join(new_lines))

        return SUCCESS


class RTDhcpClient:
    def __init__(self) -> None:
        self._worker = RTAPIDebian()
        self._name: str = "dhcpcd"

    def disable(self) -> bool:
        if SUCCESS == self._worker.disable(self._name):
            if SUCCESS == self._worker.stop(self._name):
                return True
        return False
