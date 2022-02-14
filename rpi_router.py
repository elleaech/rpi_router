from pathlib import Path
from router_data import *
from router_cmd import *


def set_network() -> bool:
    conf_directory = RTPath(Path("/", "etc", "network", "interfaces.d"))

    client_link = "wlan0"
    server_link = "eth0"

    conf_directory.append(RTFile(None, client_link, True))
    conf_directory.append(RTFile(None, server_link, False))

    conf_directory.go()

    conf_directory.get_file(client_link).set_address()
    conf_directory.get_file(server_link).set_address()

    conf_directory.goback()


def set_dhcp_server() -> bool:
    dhcp_server = RTDhcpServer()
    dhcp_server.install()
    dhcp_server.enable()
    dhcp_server.configure()


def set_firewall() -> bool:
    firewall = RTFireWall()
    firewall.install()
    firewall.allow_dhcp_traffic()
    firewall.enable_package_forwarding()


def main() -> int:
    dhcp_client = RTDhcpClient("dhcpcd")
    dhcp_client.disable()

    success: bool = set_network()

    if success:
        success: bool = set_dhcp_server()

        if success:
            set_firewall()


if __name__ == "__main__":
    main()
