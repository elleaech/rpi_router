## Usage:
--------------

``` bash
sudo python3 rpi_router.py --help
```

- `client_link_t`: external server connection type with Raspberry Pi
- `client_addr`: Raspberry Pi's external IP address
- `client_addr_network_bytes`: number of bytes to represent Raspberry Pi's address at external network
>
- `gateway_link_t`: internal Raspberry Pi's clients connection type
- `gateway_addr`: internal gateway IP address (that is, Raspberry Pi's address as a gateway)
- `gateway_addr_network_bytes`: number of bytes to represent Raspberry Pi's address as a gateway

## Future
--------------

### Improvements

- Algorithms
- Return codes

### Portings

- Add more `RTAPIOS` subclasses?
- Add more `RTAddress` subclasses?

### Possible changes

- Add new configuration files?
- Change firewall type?
- Change dhcp server and client?
