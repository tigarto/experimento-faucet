

## Suposiciones##

1. Se tienen todas las herramientas instaladas y funcionales.

## Archivos de configuracion ##

1. [**faucet.yaml**](faucet.yaml): tiene la siguiente ruta: /etc/faucet/faucet.yaml

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

2. [**prometheus.yml**](prometheus.yml): tiene la siguiente rura: /etc/faucet/prometheus/prometheus.yml. Tambien, maneja la siguiente IP (de la interafaz de red inalambrica en el caso): wlp2s0 = 192.168.1.3. 

```yml
# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  - "faucet.rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'
    static_configs:
      - targets: ['192.168.1.3:9090']
  - job_name: 'faucet'
    static_configs:
      - targets: ['192.168.1.3:9302']
  - job_name: 'gauge'
    static_configs:
      - targets: ['192.168.1.3:9303']
  - job_name: 'cadvisor'
    static_configs:
      - targets: ['192.168.1.3:8080']
```

## Pasos para la realización de la prueba ##

### Opcionales ###

1. Reiniciar del protheus:

```bash
# Reinicio del prometheus
sudo systemctl restart prometheus
```
Este comando solo es necesario cuando se cambie el archivo **prometheus.yml**

### Para el experimento ###

1. Arranque de la topologia:

```bash
# Arrancar el faucet
sudo python topologia-test.py
```

2. Arrancar el wireshark eligiendo las interfaces en las cuales se analizara el trafico. Para nuestro caso estas seran: Loopback (Lo), sw1-eth1, sw1-eth2 y sw1-eth3.

```bash
# Arrancar el wireshark
sudo wireshark
```

3. Arranque del monitor de los contenedores (cAdvisor):

```bash
# Arrancar el cadvisor
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

4. Arranque del controlador faucet:

   1. Arranque del faucet.

```bash
# Arrancar el faucet
sudo docker run -d \
    --name faucet \
    --restart=always \
    -v /etc/faucet/:/etc/faucet/ \
    -v /var/log/faucet/:/var/log/faucet/ \
    -p 6653:6653 \
    -p 9302:9302 \
    faucet/faucet
```

   2. Arranque del gauge:

```bash
# Arrancar el gauge
sudo docker run -d \
    --name gauge \
    --restart=always \
    -v /etc/faucet/:/etc/faucet/ \
    -v /var/log/faucet/:/var/log/faucet/ \
    -p 6654:6653 \
    -p 9303:9303 \
    faucet/gauge
```

5. Empezar a experimentar y tomar metricas:


## Sobre el experimento ##

Para analizar el experimento, se procedio a ejecutar unos comandos sencillos y tomar unas metricas asociadas a los contenedores que hacen de nodos (h1, h2 y h3) mediante cAdvisor y mediante el controlador faucet.

### Sniffing usando wireshark ###

Se emplea wireshark para realizar las tareas de sniffing 

### Variables monitoreadas mediante cAdvisor ###

* **Variable 1**: Descripcion 
* **Variable 2**: Descripcion

### Variables monitoreadas mediante Faucet ###

Para mas invormacion ver el siguiente [enlace](https://docs.faucet.nz/en/latest/monitoring.html)

**Exportadas por faucet**
  * **of_packet_ins_total**: number of OF packet_ins received from DP.	
  * **of_errors_total**: number of OF errors received from DP.
  * **of_flowmsgs_sent_total**: number of OF flow messages (and packet outs) sent to DP.

  Todas las variables anteriores son tipo contador. Es decir solo aumentan.

**Exportadas por gauge**:
  

  Todas estas variables son tipo gauge, es decir, pueden aumentar y disminuir.

### Acceso web ###

Las siguientes son las URL para acceder a las herramientas de monitoreo:
1. **Prometheus**: localhost.9090
2. **Grafana**: localhost.3000
3. **cAdvisor**: localhost.8080


## Caracteristicas del experimento ##

```
h1: kwargs {'ip': '10.0.0.251'}
h1: update resources {'cpu_quota': -1}
h2: kwargs {'ip': '10.0.0.252'}
h2: update resources {'cpu_quota': -1}
h3: kwargs {'ip': '10.0.0.253'}
```


**Experimento 1**:

1. Se hacen 20 pings y se obtienen los resultados. Uno por cada host





Hora aproximada (19.35)




##Enlaces##
1. [catalyzeio/cadvisor-metrics](https://github.com/catalyzeio/cadvisor-metrics)
2. [cadvisor/docs/api.md](https://github.com/google/cadvisor/blob/master/docs/api.md)
3. [cadvisor/docs/api_v2.md](https://github.com/google/cadvisor/blob/master/docs/api_v2.md)
4. [Faucet](https://docs.faucet.nz/en/latest/)
5. [Monitoring](https://docs.faucet.nz/en/latest/monitoring.html)
6. [caesar0301/awesome-pcaptools](https://github.com/caesar0301/awesome-pcaptools)
7. [Awesome PCAP Tools](http://xiaming.me/awesome-pcaptools/)
8. [Network Traffic and Intrusion Simulations](https://edux.fit.cvut.cz/oppa/MI-SIB/prednasky/mi-sib-p06-NetworkSimulations.pdf)
9. [Tarea N°1: Mininet](http://profesores.elo.utfsm.cl/~agv/elo323/2s15/Assignments/Mininet.pdf)
10. [Assignment 1: Sockets, Mininet, & Performance](http://pages.cs.wisc.edu/~agember/cs640/s15/assign1/)
11. [D-ITG V. 2.6.1d Manual](http://www.grid.unina.it/software/ITG/manual/D-ITG2.6.1d-manual.pdf)
12. [Software Defined Network (SDN) --- Mininet, OVS, P4 switch, POX, RYU Learning Guide](http://csie.nqu.edu.tw/smallko/sdn/sdn.htm)
13. [THE (IN)SECURITY OF TOPOLOGY DISCOVERY IN OPENFLOW-BASED SOFTWARE DEFINED NETWORK](https://pdfs.semanticscholar.org/8278/7dfd17341612bd57e41f561ac82a770ba59c.pdf)
