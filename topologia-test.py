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
'''

from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.cli import CLI
from mininet.net import Containernet
from mininet.log import info, setLogLevel

import os

setLogLevel('info')

info('*** Create the controller \n')



c0 = RemoteController('c0', ip = "127.0.0.1", port = 6653)
info(c0)
"Create Simple topology example."
net = Containernet(build=False)
# Initialize topology


# Add containers
info('*** Adding docker containers using ubuntu-test images\n')
# Codigo DoS: https://github.com/firefoxbug/ddos/blob/master/
h1 = net.addDocker('h1', ip='10.0.0.251', dimage="ubuntu-test")                  # Cliente
h2 = net.addDocker('h2', ip='10.0.0.252', dimage="openswitch/ubuntuscapy")       # Atacante
h3 = net.addDocker('h3', ip='10.0.0.253', dimage="ubuntu-test")                  # Victima

# Add switches    
info('*** Adding switches\n')
s1 = OVSSwitch(name = 's1', failMode = 'secure')

# Add links    
info('*** Creating links\n')
net.addLink( h1, s1 )
net.addLink( h2, s1 )
net.addLink( h3, s1 )

net.addController('c0')

# Build the network
info('*** Build the network\n')
net.build()
info('*** Starting network\n')
net.start()
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()

