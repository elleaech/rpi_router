import argparse
from pathlib import Path
from router_data import *
from router_cmd import *


def get_cl_parameters() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("client_link_t", help="external link type")
    parser.add_argument("client_addr", help="external ip address")
    parser.add_argument("client_addr_network_bytes", help="netmask bytes number")
    parser.add_argument("gateway_link_t", help="internal link type")
    parser.add_argument("gateway_addr", help="internal gateway ip address")
    parser.add_argument("gateway_addr_network_bytes", help="netmask bytes number")

    args = parser.parse_args()

    return args


def set_network(
    client_link_t,
    gateway_link_t,
    client_addr,
    gateway_addr,
    client_addr_network_bytes: int,
    gateway_addr_network_bytes: int,
) -> bool:
    conf_directory = RTPath(Path("/", "etc", "network", "interfaces.d"))

    parsed_client_addr = client_addr.split(".")
    parsed_gateway_addr = gateway_addr.split(".")

    if len(parsed_gateway_addr) >= 4 and len(parsed_client_addr) >= 4:
        client_addr = RTIpAddress(
            client_addr_network_bytes,
            parsed_client_addr[0],
            parsed_client_addr[1],
            parsed_client_addr[2],
            parsed_client_addr[3],
        )

        gateway_addr = RTIpAddress(
            gateway_addr_network_bytes,
            parsed_gateway_addr[0],
            parsed_gateway_addr[1],
            parsed_gateway_addr[2],
            parsed_gateway_addr[3],
        )

        conf_directory.append(RTFile(client_addr, client_link_t, True))
        conf_directory.append(RTFile(gateway_addr, gateway_link_t, False))

        conf_directory.go()

        conf_directory.get_file(client_link_t).set_address()
        conf_directory.get_file(gateway_link_t).set_address()

        conf_directory.goback()

        return True
    else:
        return False


def set_dhcp_server() -> bool:
    dhcp_server = RTDhcpServer("isc-dhcp-server")
    dhcp_server.install()
    dhcp_server.enable()
    dhcp_server.configure()

    return True


def set_firewall() -> bool:
    firewall = RTFireWall()
    firewall.install()
    firewall.allow_dhcp_traffic()
    firewall.enable_package_forwarding()


def main() -> int:
    cl_parameters = get_cl_parameters()

    try:
        client_addr_network_bytes = int(cl_parameters.client_addr_network_bytes)
        gateway_addr_network_bytes = int(cl_parameters.gateway_addr_network_bytes)
    except ValueError:
        raise ValueError

    success: bool = set_network(
        cl_parameters.client_link_t,
        cl_parameters.gateway_link_t,
        cl_parameters.client_addr,
        cl_parameters.gateway_addr,
        client_addr_network_bytes,
        gateway_addr_network_bytes,
    )

    if success:
        dhcp_client = RTDhcpClient("dhcpcd")

        if dhcp_client.disable():
            success: bool = set_dhcp_server()

            if success:
                set_firewall()


if __name__ == "__main__":
    main()
