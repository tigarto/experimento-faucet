# Experimento con Mininet #

1. Crear la topologia


```bash
sudo python topologia-test.py 
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
containernet> pingall
*** Ping: testing ping reachability
h1 -> X X 
h2 -> X X 
h3 -> X X 
*** Results: 100% dropped (0/6 received)
```

**Opcional**: Si se hacen cambios en el archivo de configuracion de prometheus (/etc/faucet/prometheus/prometheus.yml), reiniciar la aplicación:

```bash
sudo systemctl restart prometheus
```

2. Arrancar el contenedor asociado al faucet:


El archivo de configuracion del faucet para este caso es (/etc/faucet/faucet.yml):

```yaml
vlans:
    test_network:
        vid: 100
        description: "Red de prueba"

dps:
    sw1:
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
sudo docker run -d \
    --name faucet \
    --restart=always \
    -v /etc/faucet/:/etc/faucet/ \
    -v /var/log/faucet/:/var/log/faucet/ \
    -p 6653:6653 \
    -p 9302:9302 \
    faucet/faucet

# Arrancando el gauge
sudo gauge -v
```

3. Arrancar el contenedor asociado al gauge:

```bash
# Arrancando el gauge
sudo docker run -d \
    --name gauge \
    --restart=always \
    -v /etc/faucet/:/etc/faucet/ \
    -v /var/log/faucet/:/var/log/faucet/ \
    -p 6654:6653 \
    -p 9303:9303 \
    faucet/gauge
```

4. Arrancar el contenedor asociado al cAdvisor:

```bash
# Arrancando el cadvisor
sudo docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:ro \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  google/cadvisor:latest
```


5. Veridicar targets




Se puede verificar que ya hay ping:

```bash
containernet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 
h2 -> h1 h3 
h3 -> h1 h2 
*** Results: 0% dropped (6/6 received)
```

Bajar contenedores:

```bash
sudo docker stop gauge
sudo docker stop faucet
sudo docker stop cadvisor
sudo docker rm cadvisor
sudo docker rm gauge
sudo docker rm faucet
```


## Conclusión ##
El error que se esta intentando evitar aun permanece. Se va a intentar trabajar en un ambiente virtual.

