#!/usr/bin/python

'''
Container:
sudo docker build -t ubuntu-test .

Topologia:

   h1 --- s1 --- h3
          |
          |
          h2

sudo python topologia-test.py 

Controlador: 

./pox.py log.level --DEBUG openflow.of_01 --port=6653 forwarding.l2_learning 


Comandos por si acaso:
sudo fuser -n tcp 6653 (https://gist.github.com/happyrobots/1101053)

https://www.programcreek.com/python/example/97395/mininet.cli.CLI
Esto es lo que necesito: https://sourceforge.net/p/ryu/mailman/message/35785685/


BUG:

 sudo ovs-vsctl show9ec06414-9bd9-4579-81d4-8e7801c2eb61
    Bridge "s1"
        Controller "tcp:127.0.0.1:6653"
            is_connected: true
        Controller "tcp:127.0.0.1:6653"
            is_connected: true
        fail_mode: secure
        Port "s1-eth3"
            Interface "s1-eth3"
        Port "s1-eth2"
            Interface "s1-eth2"
        Port "s1-eth1"
            Interface "s1-eth1"
        Port "s1"
            Interface "s1"
                type: internal
    ovs_version: "2.5.5"

Ver problemas en las IPs manejadas para el controlador

Conclusiones:
1. El Comando start no dio con swirches tipos ovs...
2. Se puede borrar la ojo la cosa esta pineando. 

'''

from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.cli import CLI
from mininet.net import Containernet
from mininet.log import info, setLogLevel

import os

setLogLevel('info')

info('*** Create the controller \n')


c0 = RemoteController('c0', ip = "127.0.0.1", port = 6653)
c1 = RemoteController('c1', ip = "127.0.0.1", port = 6654)

info(c0)
"Create Simple topology example."
net = Containernet(build=False)

net.addController('c0')
net.addController('c1')

# Initialize topology


# Add containers
info('*** Adding docker containers using ubuntu-test images\n')
# Codigo DoS: https://github.com/firefoxbug/ddos/blob/master/
h1 = net.addDocker('h1', ip='10.0.0.251', dimage="ubuntu-test")                  # Cliente
h2 = net.addDocker('h2', ip='10.0.0.252', dimage="openswitch/ubuntuscapy")       # Atacante
h3 = net.addDocker('h3', ip='10.0.0.253', dimage="ubuntu-test")                  # Victima

# Add switches    
info('*** Adding switches\n')
s1 = net.addSwitch('s1')

#s1.vsctl('sudo ovs-vsctl show')
# Add links    
info('*** Creating links\n')
net.addLink( h1, s1 )
net.addLink( h2, s1 )
net.addLink( h3, s1 )



#s1.vsctl('set-controller','s1','tcp:127.0.0.1:6653 tcp:127.0.0.1:6654')
#s1.cmd('ovs-vsctl set-controller s1 tcp:127.0.0.1:6653 tcp:127.0.0.1:6654')
#s1.start(['c0','c1'])
#s1.vsctl('set-controller','s1','tcp:127.0.0.1:6653 tcp:127.0.0.1:6654')
#s1.cmdPrint('sudo ovs-vsctl show')

# Build the network
info('*** Build the network\n')
net.build()
c0.start()
c1.start()
s1.start([c0,c1])
# s1.vsctl('set-controller','s1','tcp:127.0.0.1:6653 tcp:127.0.0.1:6654') 
'''
s1.cmd('ovs-vsctl set-controller s1 tcp:127.0.0.1:6653 tcp:127.0.0.1:6654')
Este comando da solo en consola
'''
info('*** Starting network\n')
net.start()
net.staticArp()
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()

