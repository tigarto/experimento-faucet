# Experimento con Faucet ##

## Pasos ##

1. Definir la topologia ([topologia-test.py](topologia-test.py)) y ponerla a funcionar. 

```bash
sudo python topologia-test.py
```

2. Verificar las caracteristicas del switch creado:

```bash
# Comando aplicado
sudo sudo ovs-vsctl show
# Salida para el caso
9ec06414-9bd9-4579-81d4-8e7801c2eb61
    Bridge "s1"
        Controller "tcp:127.0.0.1:6654"
        Controller "tcp:127.0.0.1:6653"
        fail_mode: secure
        Port "s1-eth2"
            Interface "s1-eth2"
        Port "s1-eth3"
            Interface "s1-eth3"
        Port "s1"
            Interface "s1"
                type: internal
        Port "s1-eth1"
            Interface "s1-eth1"
    ovs_version: "2.5.5"
```

3. El controlador que se empleará sera el faucet cuya arquitectura se muestra a continuación. 

![arquitectura_faucet](arquitectura_faucet.png)

