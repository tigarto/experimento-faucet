


## Controlador Faucet ##

### Arquitectura ###

Faucet es un controlador Openflow que permite a los operadores de red correr sus redes de la misma manera como lo hacen en clusters de servidores y por lo tanto esta concebido para el desarrollo de aplicaciones de red. El la siguiente figura se muestra la arquitectura de faucet:

![arquitectura-faucet](arquitectura-faucet.png)

Teniendo en cuenta la figura anterior, y desde el punto se vista mas basico, Faucet tiene los siguientes componentes:
1. **Ryu**: Controlador Openflow en el cual se basa el faucet.
   1. **Faucet**: Parte que implementa las funciones de red, por ejemplo las aplicaciones de envio de paquetes (switching application). 
   2. **Gauge**: Aplicacion Ryu para el monitoreo y obtencion de estadisticas.
2. **time-series DB (Base de datos de series de tiempo)**
   1. **Opcion 1**: InfluxDB
   2. **Opcion 2** Prometheus.

En la siguiente figura se muestra prometheus, al cual se accede usando la URL: **http://localhost:9090**

![prometheus](prometheus.png)

3. **Grafana (Dashboard)**: Paneles de usuario. Estos paneles se pueden hacer en el mismo Grafana o instalarlos mediante el archivo de descripción JSON (que describe el panel) y que es compartido por otros. Para el caso los siguientes paneles, se obtubieron del siguiente [enlace](https://docs.faucet.nz/en/latest/tutorials/first_time.html). Para acceder a los paneles de grafana se emplea la siguiente URL: **http://localhost:3000**. A continuación se muestra cada una de los paneles:

**[Inventario](https://docs.faucet.nz/en/latest/_static/grafana-dashboards/faucet_inventory.json)**

![inventory](inventory.png) 

**[Instrumentacion](https://docs.faucet.nz/en/latest/_static/grafana-dashboards/faucet_instrumentation.json)**

![instrumentation](instrumentation.png)

**[Estadisticas de puertos](https://docs.faucet.nz/en/latest/_static/grafana-dashboards/faucet_port_statistics.json)**

![port_statistics](port_statistics.png)


Con el fin de contar mensajes entre el controlador y el switch se creo una nueva dashboard la cual se muestra a continuacion:

![cont_metricas](cont_metricas.png)


### Utilidad ###

Para nuestro caso, la mayor motivación en la elección fue la facilidad (que al parecer por el momento) ofrece este controlador en el desarrollo de aplicaciones. Esto se puede ver en atributos como: capacidad de ejecución en entornos virtuales y reales, open source que permite agregar nuevas caracteristicas, facilidad de debugging, facil administracion, etc.


## Experimento ##

### Topologia ###

La siguiente figura muestra la topologia de test donde **h1** sera el atacante, **h2** sera el cliente y **h3** sera el servidor.

![topologia-test](topologia-test.png)

El [script](topologia-test.py) que describe la topologia es:

```python
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.cli import CLI
from mininet.net import Containernet
from mininet.log import info, setLogLevel
import time

import os

setLogLevel('info')

info('*** Create the controller \n')

#info(c0)
"Create Simple topology example."
net = Containernet(switch = OVSSwitch, build=False)
net.addController('c0', controller = RemoteController, ip = "127.0.0.1", port = 6653)
net.addController('c1', controller = RemoteController, ip = "127.0.0.1", port = 6654)
# Initialize topology

# Add containers
h1 = net.addHost('h1', ip='10.0.0.251')  # Cliente
h2 = net.addHost('h2', ip='10.0.0.252')  # Atacante
h3 = net.addHost('h3', ip='10.0.0.253')  # Victima

# Add switches    
info('*** Adding switches\n')
sw1 = net.addSwitch('sw1', protocols='OpenFlow13')

# Add links    
info('*** Creating links\n')
net.addLink( h1, sw1 )
net.addLink( h2, sw1 )
net.addLink( h3, sw1 )

# Build the network
info('*** Build the network\n')
net.build()

info('*** Starting network\n')
net.start()

info('*** Running CLI\n')
CLI(net)

info('*** Stopping network')
net.stop()
```

### Pasos del experimento ###

A continuación se describen los pasos mas basicos para llevar a cabo el experimento:
1. Arrancar el faucet.
2. Arrancar el gauge.
3. Verificar en el prometheus que los targets este listos.
4. Mirar los resultados en grafana.
5. Arrancar mininet




1. [Faucet Deploying SDN in the Enterprise](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45641.pdf)
2. [Informacion Faucet](https://github.com/faucetsdn/faucet.nz)
3. [Faucet - The Open Source Production Quality OpenFlow Switch](https://wand.nz/~brad/talks/faucet.pdf)
4. https://www.ausnog.net/sites/default/files/ausnog-2018/presentations/1.8_Richard_Nelson_AusNOG2018.pdf
5. https://www.gdt.id.au/~gdt/presentations/2016-07-05-questnet-sdn/2016-07-05-questnet-sdn-notes.pdf
