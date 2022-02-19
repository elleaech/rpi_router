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


def print_cl_parameters(cl_parameters: argparse.Namespace):
    log("-" * 50)
    log(f"CLIENT LINK TYPE: {cl_parameters.client_link_t}")
    log(f"CLIENT ADDRESS: {cl_parameters.client_addr}")
    log(f"CLIENT NETMASK BYTES: {cl_parameters.client_addr_network_bytes}")
    log(f"GATEWAY LINK TYPE: {cl_parameters.gateway_link_t}")
    log(f"GATEWAY ADDRESS: {cl_parameters.gateway_addr}")
    log(f"GATEWAY NETMASK BYTES: {cl_parameters.gateway_addr_network_bytes}")
    log("-" * 50)


def log(message):
    print(message)


def init_address(addr_network_bytes: int, address_as_str: str):
    log("\nSETTING ADDRESS:")

    parsed_address = address_as_str.split(".")

    if len(parsed_address) >= 4:
        address = RTIpv4Address(
            addr_network_bytes,
            parsed_address[0],
            parsed_address[1],
            parsed_address[2],
            parsed_address[3],
        )

        log(address.address)
        return address
    else:
        return None


def set_network(
    client_link_t: str,
    gateway_link_t: str,
    client_addr: RTIpv4Address,
    gateway_addr: RTIpv4Address,
) -> bool:
    log("\nSETTING NETWORK INTERFACES:")

    if client_addr != None and gateway_addr != None:
        conf_directory = RTPath(Path("/", "etc", "network", "interfaces.d"))

        conf_directory.append(RTNetFile(client_addr, client_link_t, True))
        conf_directory.append(RTNetFile(gateway_addr, gateway_link_t, False))

        conf_directory.go()

        conf_directory.get_file(client_link_t).set_address()
        log(conf_directory.get_current_dir())
        conf_directory.get_file(gateway_link_t).set_address()
        log(conf_directory.get_current_dir())

        conf_directory.goback()

        return True
    else:
        return False


def set_dhcp_server(
    gateway_addr: RTIpv4Address,
    gateway_link_t: str,
) -> bool:
    log("\nSETTING DHCP SERVER:")

    if gateway_addr != None:
        dhcp_server = RTDhcpServer(gateway_addr, gateway_link_t)
        return (
            dhcp_server.install() and dhcp_server.configure() and dhcp_server.enable()
        )

    else:
        return False


def set_firewall() -> bool:
    log("\nSETTING FIREWALL:")
    firewall = RTFireWall()

    return (
        firewall.install()
        and firewall.allow_dhcp_traffic()
        and firewall.enable_package_forwarding()
    )


def main() -> int:
    cl_parameters = get_cl_parameters()
    print_cl_parameters(cl_parameters)

    if cl_parameters.client_link_t == cl_parameters.gateway_link_t:
        print("link_t cannot be equal!")
        return -1

    try:
        client_addr_network_bytes = int(cl_parameters.client_addr_network_bytes)
        gateway_addr_network_bytes = int(cl_parameters.gateway_addr_network_bytes)
    except ValueError:
        raise ValueError

    client_addr = init_address(client_addr_network_bytes, cl_parameters.client_addr)
    gateway_addr = init_address(gateway_addr_network_bytes, cl_parameters.gateway_addr)

    success: bool = set_network(
        cl_parameters.client_link_t,
        cl_parameters.gateway_link_t,
        client_addr,
        gateway_addr,
    )

    if success:
        dhcp_client = RTDhcpClient()

        log("DISABLING DHCP CLIENT:")
        if dhcp_client.disable():
            success: bool = set_dhcp_server(gateway_addr, cl_parameters.gateway_link_t)

            if success:
                set_firewall()


if __name__ == "__main__":
    main()
