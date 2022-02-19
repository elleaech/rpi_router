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

- Add more `RTAPIOS` subclasses?
- Add more `RTAddress` subclasses?

### Possible changes

- Change firewall type?
- Change dhcp server and client?
