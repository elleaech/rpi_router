# Raspberry Pi: Network Island

## About
--------------

`Raspberry Pi: Network Island` is a script that bridges your device network interface
and the network switch you're connecting to.

Whether `ethernet` or `wireless` connection is available, and your device doesn't match
the switch interface, `Raspberry Pi: Network Island` allows you to be online either way!

Using native Raspberry Pi network and relying on automation, `Raspberry Pi: Network Island` builds different subnetworks
from a original network. Allowing different types of interface between them.

## Usage:
--------------

``` bash
sudo python3 rpi_router.py --help
```

- `client_link_t`: external server connection with Raspberry Pi
- `client_addr`: Raspberry Pi's external IP address
- `client_addr_network_bytes`: number of bytes to represent Raspberry Pi's external network
>
- `gateway_link_t`: internal Raspberry Pi's clients connection
- `gateway_addr`: internal gateway IP address (that is, Raspberry Pi's address as a gateway)
- `gateway_addr_network_bytes`: number of bytes to represent Raspberry Pi's network as a gateway

> You may need a reboot for network configurations to be set...

## Future
--------------

### Improvements

- Algorithms
- Update network configuration on execution time

### Portings

- [Add more `RTAPIOS` subclasses?](https://github.com/elleaech/rpi_router/blob/main/router_cmd/os.py)
- [Add more `RTAddress` subclasses?](https://github.com/elleaech/rpi_router/blob/main/router_data/addr.py)

### Possible changes

- [Change firewall type?](https://github.com/elleaech/rpi_router/blob/main/router_cmd/firewall.py)
- [Change dhcp server and client?](https://github.com/elleaech/rpi_router/blob/main/router_cmd/dhcp.py)

## License
--------------
[Apache License 2.0](https://github.com/elleaech/rpi_router/blob/master/LICENSE)
