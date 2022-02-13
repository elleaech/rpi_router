from router_data import *
from router_cmd import *

CLIENT = RTFile("wlan0")
GATEWAY = RTFile("eth0")

CONF_DIRECTORY = RTPath("etc/network/interfaces.d")

DHCP_CLIENT = RTDhcpClient()
DHCP_SERVER = RTDhcpServer()

FIREWALL = RTFireWall()


def set_network() -> bool:
    CONF_DIRECTORY.append(CLIENT)
    CONF_DIRECTORY.append(GATEWAY)

    CONF_DIRECTORY.go()

    CLIENT.set_addr()
    GATEWAY.set_addr()

    CONF_DIRECTORY.goback()


def set_dhcp_server() -> bool:
    DHCP_SERVER.install()
    DHCP_SERVER.enable()
    DHCP_SERVER.configure()


def set_firewall() -> bool:
    FIREWALL.install()
    FIREWALL.allow_dhcp_traffic()
    FIREWALL.enable_package_forwarding()


def main() -> int:
    DHCP_CLIENT.disable()

    success: bool = set_network()

    if success:
        success: bool = set_dhcp_server()

        if success:
            set_firewall()


if __name__ == "__main__":
    main()
