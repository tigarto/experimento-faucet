# Experimento con Mininet #

1. Crear la topologia


```bash
sudo mn --topo single,3 --mac --controller=remote,ip=127.0.0.1,port=6653 --controller=remote,ip=127.0.0.1,port=6654
```

Posteriormente se verifica las caracteristicas del switch creado:

```bash
# Comando
sudo ovs-vsctl show
# Salida
9ec06414-9bd9-4579-81d4-8e7801c2eb61
    Bridge "s1"
        Controller "ptcp:6634"
        Controller "tcp:127.0.0.1:6653"
        fail_mode: secure
        Port "s1-eth1"
            Interface "s1-eth1"
        Port "s1"
            Interface "s1"
                type: internal
        Port "s1-eth3"
            Interface "s1-eth3"
        Port "s1-eth2"
            Interface "s1-eth2"
    ovs_version: "2.5.5"
```

Si se aplica ping vemos que no hay:

```bash
containernet> h1 ping -c 1 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
From 10.0.0.1 icmp_seq=1 Destination Host Unreachable
--- 10.0.0.2 ping statistics ---
1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms
```

**Opcional**: Si se hacen cambios en el archivo de configuracion de prometheus (/etc/faucet/prometheus/prometheus.yml), reiniciar la aplicación:

```bash
sudo systemctl restart prometheus
```

2. Arrancar el faucet y el gauge:


El archivo de onfiguracion del faucet para este caso es:

```yaml
vlans:
    test_network:
        vid: 100
        description: "Red de prueba"

dps:
    s1:
        dp_id: 0x0000000000000001
        hardware: "Open vSwitch"
        interfaces:
            1:
                name: "h1"
                description: "atacante"
                native_vlan: test_network
            2:
                name: "h2"
                description: "cliente"
                native_vlan: test_network
            3:
                name: "h3"
                description: "servidor"
                native_vlan: test_network
```

Ahora arrancando la herramienta:


```bash
# Arrancando el faucet
sudo systemctl stop faucet
sudo systemctl disable faucet
sudo systemctl enable faucet
sudo faucet -v
# Arrancando el gauge
sudo gauge -v
```

Se puede verificar que ya hay ping:

```bash
containernet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 
h2 -> h1 h3 
h3 -> h1 h2 
*** Results: 0% dropped (6/6 received)
```

## Conclusión ##
El error que se esta intentando evitar aun permanece. Se va a intentar trabajar en un ambiente virtual.

