Ademas de los metodos proporcionados por el faucet para obtener estadisticas, tambien se empleo la aplicación ryu.app.ofctl_rest la cual se cargo con el siguiente comando:

```bash

sudo faucet ....

```

Los comandos get y post para obtener las estadisticas empleando esta aplicación se pueden encontrar en el siguiente [enlace](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#ryu-app-ofctl-rest). Para el caso se tomaron las siguientes medidas:
1. **Obtener las estadisticas de los flujos de un switch** (Basicamente se obtiene la informacion asociada con la siguienente [estructura](http://flowgrammable.org/sdn/openflow/message-layer/flowmod/#tab_ofp_1_3)):

```bash
curl -X GET http://localhost:8080/stats/flow/1
```

2. **Obtener estadisticas de flujo agregado (Get aggregate flow stats)**:


```bash
curl -X GET http://localhost:8080/stats/aggregateflow/1
```

3. Get ports stats
Get ports stats of the switch which specified with Datapath ID in URI.



1. Prueba de conectividad: 

```bash
# Terminal mininet
pingall
```

**Parte 1**: Antes de la aplicacion del comando **pingall**:

**Aggregate flow stats**:

{
    "1": [
        {
            "packet_count": 96,
            "byte_count": 7552,
            "flow_count": 24
        }
    ]
}

**Get ports stats**:

{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 93,
            "duration_nsec": 64000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 10,
            "tx_packets": 49,
            "rx_bytes": 796,
            "tx_bytes": 5683,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 93,
            "duration_nsec": 70000000,
            "port_no": 1
        },
        {
            "rx_packets": 10,
            "tx_packets": 48,
            "rx_bytes": 796,
            "tx_bytes": 5593,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 93,
            "duration_nsec": 69000000,
            "port_no": 2
        },
        {
            "rx_packets": 10,
            "tx_packets": 48,
            "rx_bytes": 796,
            "tx_bytes": 5593,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 93,
            "duration_nsec": 70000000,
            "port_no": 3
        }
    ]
}

**Parte 2**: Antes de la aplicacion del comando **pingall**:

**Aggregate flow stats**:

{
    "1": [
        {
            "packet_count": 169,
            "byte_count": 13082,
            "flow_count": 24
        }
    ]
}


**Get ports stats**:

{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 162,
            "duration_nsec": 913000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 19,
            "tx_packets": 62,
            "rx_bytes": 1426,
            "tx_bytes": 6698,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 162,
            "duration_nsec": 919000000,
            "port_no": 1
        },
        {
            "rx_packets": 19,
            "tx_packets": 61,
            "rx_bytes": 1426,
            "tx_bytes": 6608,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 162,
            "duration_nsec": 918000000,
            "port_no": 2
        },
        {
            "rx_packets": 19,
            "tx_packets": 61,
            "rx_bytes": 1426,
            "tx_bytes": 6608,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 162,
            "duration_nsec": 919000000,
            "port_no": 3
        }
    ]
}


2. Prueba de ping fijo: 

```bash
# Terminal mininet
h1 ping -c 200 -i 0.5 h3
```

**Parte 1**: Antes de la aplicacion del comando **ping**:

**Aggregate flow stats**:

{
    "1": [
        {
            "packet_count": 68,
            "byte_count": 5592,
            "flow_count": 24
        }
    ]
}

**Get ports stats**:

{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 26,
            "duration_nsec": 666000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 9,
            "tx_packets": 41,
            "rx_bytes": 726,
            "tx_bytes": 4857,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 26,
            "duration_nsec": 673000000,
            "port_no": 1
        },
        {
            "rx_packets": 8,
            "tx_packets": 41,
            "rx_bytes": 656,
            "tx_bytes": 4837,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 26,
            "duration_nsec": 673000000,
            "port_no": 2
        },
        {
            "rx_packets": 8,
            "tx_packets": 41,
            "rx_bytes": 656,
            "tx_bytes": 4837,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 26,
            "duration_nsec": 673000000,
            "port_no": 3
        }
    ]
}

**Parte 2**: Una vez se ejecuta el comando **ping**:

```bash
h1 ping -c 200 -i 0.5 h3
...
64 bytes from 10.0.0.253: icmp_seq=197 ttl=64 time=0.061 ms
64 bytes from 10.0.0.253: icmp_seq=198 ttl=64 time=0.073 ms
64 bytes from 10.0.0.253: icmp_seq=199 ttl=64 time=0.058 ms
64 bytes from 10.0.0.253: icmp_seq=200 ttl=64 time=0.057 ms

--- 10.0.0.253 ping statistics ---
200 packets transmitted, 200 received, 0% packet loss, time 101903ms
rtt min/avg/max/mdev = 0.032/0.063/0.328/0.031 ms
```

**Aggregate flow stats**:

{
    "1": [
        {
            "packet_count": 1341,
            "byte_count": 127602,
            "flow_count": 24
        }
    ]
}

**Get ports stats**:

{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 220,
            "duration_nsec": 954000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 215,
            "tx_packets": 257,
            "rx_bytes": 20634,
            "tx_bytes": 25864,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 220,
            "duration_nsec": 961000000,
            "port_no": 1
        },
        {
            "rx_packets": 11,
            "tx_packets": 53,
            "rx_bytes": 866,
            "tx_bytes": 6048,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 220,
            "duration_nsec": 961000000,
            "port_no": 2
        },
        {
            "rx_packets": 215,
            "tx_packets": 256,
            "rx_bytes": 20634,
            "tx_bytes": 25774,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 220,
            "duration_nsec": 961000000,
            "port_no": 3
        }
    ]
}

3. Prueba iperf. [Enlace util](https://support.cumulusnetworks.com/hc/en-us/articles/216509388-Throughput-Testing-and-Troubleshooting):


http://therandomsecurityguy.com/openvswitch-cheat-sheet/



sudo ovs-ofctl dump-flows sw1 --protocols=OpenFlow13





tigarto@fuck-pc:~$ sudo ovs-ofctl dump-flows sw1 --protocols=OpenFlow13
OFPST_FLOW reply (OF1.3) (xid=0x2):
 cookie=0x5adc15c0, duration=4.268s, table=0, n_packets=5, n_bytes=426, priority=9000,in_port=1,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=4.268s, table=0, n_packets=5, n_bytes=426, priority=9000,in_port=2,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=4.268s, table=0, n_packets=5, n_bytes=426, priority=9000,in_port=3,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=4.267s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x5adc15c0, duration=4.268s, table=1, n_packets=0, n_bytes=0, priority=20490,dl_type=0x9000 actions=drop
 cookie=0x5adc15c0, duration=4.268s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=ff:ff:ff:ff:ff:ff actions=drop
 cookie=0x5adc15c0, duration=4.268s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=0e:00:00:00:00:01 actions=drop
 cookie=0x5adc15c0, duration=3.769s, table=1, n_packets=4, n_bytes=340, hard_timeout=285, priority=8191,in_port=3,dl_vlan=100,dl_src=ee:02:63:97:65:6d actions=goto_table:2
 cookie=0x5adc15c0, duration=3.479s, table=1, n_packets=4, n_bytes=340, hard_timeout=275, priority=8191,in_port=1,dl_vlan=100,dl_src=fa:51:ee:62:44:dd actions=goto_table:2
 cookie=0x5adc15c0, duration=3.418s, table=1, n_packets=3, n_bytes=250, hard_timeout=275, priority=8191,in_port=2,dl_vlan=100,dl_src=b6:08:43:c4:b0:dc actions=goto_table:2
 cookie=0x5adc15c0, duration=4.267s, table=1, n_packets=4, n_bytes=348, priority=4096,dl_vlan=100 actions=CONTROLLER:96,goto_table:2
 cookie=0x5adc15c0, duration=4.267s, table=1, n_packets=0, n_bytes=0, priority=0 actions=goto_table:2
 cookie=0x5adc15c0, duration=3.769s, table=2, n_packets=0, n_bytes=0, idle_timeout=435, priority=8192,dl_vlan=100,dl_dst=ee:02:63:97:65:6d actions=pop_vlan,output:3
 cookie=0x5adc15c0, duration=3.479s, table=2, n_packets=0, n_bytes=0, idle_timeout=425, priority=8192,dl_vlan=100,dl_dst=fa:51:ee:62:44:dd actions=pop_vlan,output:1
 cookie=0x5adc15c0, duration=3.418s, table=2, n_packets=0, n_bytes=0, idle_timeout=425, priority=8192,dl_vlan=100,dl_dst=b6:08:43:c4:b0:dc actions=pop_vlan,output:2
 cookie=0x5adc15c0, duration=4.267s, table=2, n_packets=15, n_bytes=1278, priority=0 actions=goto_table:3
 cookie=0x5adc15c0, duration=4.268s, table=3, n_packets=0, n_bytes=0, priority=8240,dl_dst=01:00:0c:cc:cc:cd actions=drop
 cookie=0x5adc15c0, duration=4.268s, table=3, n_packets=0, n_bytes=0, priority=8240,dl_vlan=100,dl_dst=ff:ff:ff:ff:ff:ff actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=4.268s, table=3, n_packets=0, n_bytes=0, priority=8236,dl_dst=01:80:c2:00:00:00/ff:ff:ff:ff:ff:f0 actions=drop
 cookie=0x5adc15c0, duration=4.267s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:80:c2:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=4.267s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:00:5e:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=4.267s, table=3, n_packets=15, n_bytes=1278, priority=8208,dl_vlan=100,dl_dst=33:33:00:00:00:00/ff:ff:00:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=4.267s, table=3, n_packets=0, n_bytes=0, priority=8192,dl_vlan=100 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=4.267s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop



tigarto@fuck-pc:~$ sudo ovs-ofctl dump-ports sw1 --protocols=OpenFlow13
OFPST_PORT reply (OF1.3) (xid=0x2): 4 ports
  port LOCAL: rx pkts=0, bytes=0, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=0, bytes=0, drop=0, errs=0, coll=0
           duration=88.694s
  port  1: rx pkts=10, bytes=796, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=49, bytes=5683, drop=0, errs=0, coll=0
           duration=88.700s
  port  2: rx pkts=10, bytes=796, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=49, bytes=5683, drop=0, errs=0, coll=0
           duration=88.700s
  port  3: rx pkts=10, bytes=796, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=49, bytes=5683, drop=0, errs=0, coll=0
           duration=88.700s




{
    "1": [
        {
            "packet_count": 108,
            "byte_count": 8472,
            "flow_count": 24
        }
    ]
}



{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 118,
            "duration_nsec": 489000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 10,
            "tx_packets": 49,
            "rx_bytes": 796,
            "tx_bytes": 5683,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 118,
            "duration_nsec": 495000000,
            "port_no": 1
        },
        {
            "rx_packets": 10,
            "tx_packets": 49,
            "rx_bytes": 796,
            "tx_bytes": 5683,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 118,
            "duration_nsec": 495000000,
            "port_no": 2
        },
        {
            "rx_packets": 10,
            "tx_packets": 49,
            "rx_bytes": 796,
            "tx_bytes": 5683,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 118,
            "duration_nsec": 495000000,
            "port_no": 3
        }
    ]
}

containernet> iperf
*** Iperf: testing TCP bandwidth between h1 and h3 
*** Results: ['32.3 Gbits/sec', '32.3 Gbits/sec']


tigarto@fuck-pc:~$ sudo ovs-ofctl dump-flows sw1 --protocols=OpenFlow13
OFPST_FLOW reply (OF1.3) (xid=0x2):
 cookie=0x5adc15c0, duration=185.142s, table=0, n_packets=401928, n_bytes=20212335876, priority=9000,in_port=1,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=185.142s, table=0, n_packets=10, n_bytes=776, priority=9000,in_port=2,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=185.142s, table=0, n_packets=243557, n_bytes=16074870, priority=9000,in_port=3,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=185.141s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x5adc15c0, duration=185.142s, table=1, n_packets=0, n_bytes=0, priority=20490,dl_type=0x9000 actions=drop
 cookie=0x5adc15c0, duration=185.142s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=ff:ff:ff:ff:ff:ff actions=drop
 cookie=0x5adc15c0, duration=185.142s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=0e:00:00:00:00:01 actions=drop
 cookie=0x5adc15c0, duration=184.643s, table=1, n_packets=243556, n_bytes=16074784, hard_timeout=285, priority=8191,in_port=3,dl_vlan=100,dl_src=ee:02:63:97:65:6d actions=goto_table:2
 cookie=0x5adc15c0, duration=184.353s, table=1, n_packets=401927, n_bytes=20212335790, hard_timeout=275, priority=8191,in_port=1,dl_vlan=100,dl_src=fa:51:ee:62:44:dd actions=goto_table:2
 cookie=0x5adc15c0, duration=184.292s, table=1, n_packets=8, n_bytes=600, hard_timeout=275, priority=8191,in_port=2,dl_vlan=100,dl_src=b6:08:43:c4:b0:dc actions=goto_table:2
 cookie=0x5adc15c0, duration=185.141s, table=1, n_packets=4, n_bytes=348, priority=4096,dl_vlan=100 actions=CONTROLLER:96,goto_table:2
 cookie=0x5adc15c0, duration=185.141s, table=1, n_packets=0, n_bytes=0, priority=0 actions=goto_table:2
 cookie=0x5adc15c0, duration=184.643s, table=2, n_packets=401917, n_bytes=20212335058, idle_timeout=435, priority=8192,dl_vlan=100,dl_dst=ee:02:63:97:65:6d actions=pop_vlan,output:3
 cookie=0x5adc15c0, duration=184.353s, table=2, n_packets=243547, n_bytes=16074094, idle_timeout=425, priority=8192,dl_vlan=100,dl_dst=fa:51:ee:62:44:dd actions=pop_vlan,output:1
 cookie=0x5adc15c0, duration=184.292s, table=2, n_packets=0, n_bytes=0, idle_timeout=425, priority=8192,dl_vlan=100,dl_dst=b6:08:43:c4:b0:dc actions=pop_vlan,output:2
 cookie=0x5adc15c0, duration=185.141s, table=2, n_packets=31, n_bytes=2370, priority=0 actions=goto_table:3
 cookie=0x5adc15c0, duration=185.142s, table=3, n_packets=0, n_bytes=0, priority=8240,dl_dst=01:00:0c:cc:cc:cd actions=drop
 cookie=0x5adc15c0, duration=185.142s, table=3, n_packets=1, n_bytes=42, priority=8240,dl_vlan=100,dl_dst=ff:ff:ff:ff:ff:ff actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=185.142s, table=3, n_packets=0, n_bytes=0, priority=8236,dl_dst=01:80:c2:00:00:00/ff:ff:ff:ff:ff:f0 actions=drop
 cookie=0x5adc15c0, duration=185.141s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:80:c2:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=185.141s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:00:5e:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=185.141s, table=3, n_packets=30, n_bytes=2328, priority=8208,dl_vlan=100,dl_dst=33:33:00:00:00:00/ff:ff:00:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=185.141s, table=3, n_packets=0, n_bytes=0, priority=8192,dl_vlan=100 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=185.141s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
tigarto@fuck-pc:~$ 



tigarto@fuck-pc:~$ sudo ovs-ofctl dump-ports sw1 --protocols=OpenFlow13
OFPST_PORT reply (OF1.3) (xid=0x2): 4 ports
  port LOCAL: rx pkts=0, bytes=0, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=0, bytes=0, drop=0, errs=0, coll=0
           duration=215.158s
  port  1: rx pkts=401929, bytes=20212335966, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=243600, bytes=16080190, drop=0, errs=0, coll=0
           duration=215.164s
  port  2: rx pkts=11, bytes=866, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=54, bytes=6138, drop=0, errs=0, coll=0
           duration=215.164s
  port  3: rx pkts=243558, bytes=16074960, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=401971, bytes=20212341196, drop=0, errs=0, coll=0







{
    "1": [
        {
            "packet_count": 1936516,
            "byte_count": 60685236936,
            "flow_count": 24
        }
    ]
}


{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 240,
            "duration_nsec": 435000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 401929,
            "tx_packets": 243600,
            "rx_bytes": 20212335966,
            "tx_bytes": 16080190,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 240,
            "duration_nsec": 441000000,
            "port_no": 1
        },
        {
            "rx_packets": 11,
            "tx_packets": 54,
            "rx_bytes": 866,
            "tx_bytes": 6138,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 240,
            "duration_nsec": 441000000,
            "port_no": 2
        },
        {
            "rx_packets": 243558,
            "tx_packets": 401971,
            "rx_bytes": 16074960,
            "tx_bytes": 20212341196,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 240,
            "duration_nsec": 442000000,
            "port_no": 3
        }
    ]
}



4. Prueba iperf distintas terminales. 


Al inicio:

{
    "1": [
        {
            "packet_count": 68,
            "byte_count": 5608,
            "flow_count": 24
        }
    ]
}



{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 36,
            "duration_nsec": 460000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 9,
            "tx_packets": 45,
            "rx_bytes": 726,
            "tx_bytes": 5270,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 36,
            "duration_nsec": 470000000,
            "port_no": 1
        },
        {
            "rx_packets": 9,
            "tx_packets": 44,
            "rx_bytes": 726,
            "tx_bytes": 5184,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 36,
            "duration_nsec": 470000000,
            "port_no": 2
        },
        {
            "rx_packets": 9,
            "tx_packets": 44,
            "rx_bytes": 726,
            "tx_bytes": 5184,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 36,
            "duration_nsec": 470000000,
            "port_no": 3
        }
    ]
}



```bash
# Terminal h3
iperf3 -s -p 5003
```

[ 19] 198.00-199.00 sec  3.52 GBytes  30.2 Gbits/sec                  
[ 19] 199.00-200.00 sec  3.66 GBytes  31.4 Gbits/sec                  
[ 19] 200.00-200.04 sec   142 MBytes  28.6 Gbits/sec                  
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[ 19]   0.00-200.04 sec   688 GBytes  29.5 Gbits/sec  10772             sender
[ 19]   0.00-200.04 sec   688 GBytes  29.5 Gbits/sec                  receiver
-----------------------------------------------------------
Server listening on 5003
-----------------------------------------------------------






```bash
# Terminal h1
iperf3 -c 10.0.0.253 -p 5003 -i 0.5 -t 200 
```


[ 18] 198.50-199.00 sec  1.75 GBytes  30.0 Gbits/sec    0   8.41 MBytes       
[ 18] 199.00-199.50 sec  1.92 GBytes  32.9 Gbits/sec    0   8.41 MBytes       
[ 18] 199.50-200.00 sec  1.75 GBytes  30.0 Gbits/sec    0   8.41 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[ 18]   0.00-200.00 sec   688 GBytes  29.5 Gbits/sec  10772             sender
[ 18]   0.00-200.00 sec   688 GBytes  29.5 Gbits/sec                  receive



tigarto@fuck-pc:~$ sudo ovs-ofctl dump-ports sw1 --protocols=OpenFlow13
OFPST_PORT reply (OF1.3) (xid=0x2): 4 ports
  port LOCAL: rx pkts=0, bytes=0, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=0, bytes=0, drop=0, errs=0, coll=0
           duration=360.090s
  port  1: rx pkts=13759660, bytes=739469627853, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=5490991, bytes=362415792, drop=0, errs=0, coll=0
           duration=360.100s
  port  2: rx pkts=12, bytes=936, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=57, bytes=6465, drop=0, errs=0, coll=0
           duration=360.100s
  port  3: rx pkts=5490946, bytes=362410219, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=13759704, bytes=739469633340, drop=0, errs=0, coll=0
           duration=360.100s




{
    "1": [
        {
            "packet_count": 38501264,
            "byte_count": 1479664080060,
            "flow_count": 21
        }
    ]
}

{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 416,
            "duration_nsec": 877000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 13759660,
            "tx_packets": 5490991,
            "rx_bytes": 739469627853,
            "tx_bytes": 362415792,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 416,
            "duration_nsec": 887000000,
            "port_no": 1
        },
        {
            "rx_packets": 12,
            "tx_packets": 57,
            "rx_bytes": 936,
            "tx_bytes": 6465,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 416,
            "duration_nsec": 887000000,
            "port_no": 2
        },
        {
            "rx_packets": 5490946,
            "tx_packets": 13759704,
            "rx_bytes": 362410219,
            "tx_bytes": 739469633340,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 416,
            "duration_nsec": 887000000,
            "port_no": 3
        }
    ]
}



4. Prueba con el ataque:

**Caso 1**: Sin el iperf




tigarto@fuck-pc:~$ sudo ovs-ofctl dump-flows sw1 --protocols=OpenFlow13
OFPST_FLOW reply (OF1.3) (xid=0x2):
 cookie=0x5adc15c0, duration=6.973s, table=0, n_packets=6, n_bytes=496, priority=9000,in_port=1,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=6.973s, table=0, n_packets=6, n_bytes=496, priority=9000,in_port=2,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=6.973s, table=0, n_packets=6, n_bytes=496, priority=9000,in_port=3,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=6.972s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x5adc15c0, duration=6.973s, table=1, n_packets=0, n_bytes=0, priority=20490,dl_type=0x9000 actions=drop
 cookie=0x5adc15c0, duration=6.973s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=ff:ff:ff:ff:ff:ff actions=drop
 cookie=0x5adc15c0, duration=6.973s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=0e:00:00:00:00:01 actions=drop
 cookie=0x5adc15c0, duration=6.838s, table=1, n_packets=5, n_bytes=406, hard_timeout=307, priority=8191,in_port=1,dl_vlan=100,dl_src=76:db:0f:46:8b:10 actions=goto_table:2
 cookie=0x5adc15c0, duration=6.772s, table=1, n_packets=4, n_bytes=320, hard_timeout=299, priority=8191,in_port=2,dl_vlan=100,dl_src=aa:9c:c0:e7:28:43 actions=goto_table:2
 cookie=0x5adc15c0, duration=6.744s, table=1, n_packets=5, n_bytes=410, hard_timeout=315, priority=8191,in_port=3,dl_vlan=100,dl_src=9a:de:01:50:f3:1d actions=goto_table:2
 cookie=0x5adc15c0, duration=6.973s, table=1, n_packets=4, n_bytes=352, priority=4096,dl_vlan=100 actions=CONTROLLER:96,goto_table:2
 cookie=0x5adc15c0, duration=6.972s, table=1, n_packets=0, n_bytes=0, priority=0 actions=goto_table:2
 cookie=0x5adc15c0, duration=6.838s, table=2, n_packets=0, n_bytes=0, idle_timeout=457, priority=8192,dl_vlan=100,dl_dst=76:db:0f:46:8b:10 actions=pop_vlan,output:1
 cookie=0x5adc15c0, duration=6.772s, table=2, n_packets=0, n_bytes=0, idle_timeout=449, priority=8192,dl_vlan=100,dl_dst=aa:9c:c0:e7:28:43 actions=pop_vlan,output:2
 cookie=0x5adc15c0, duration=6.744s, table=2, n_packets=0, n_bytes=0, idle_timeout=465, priority=8192,dl_vlan=100,dl_dst=9a:de:01:50:f3:1d actions=pop_vlan,output:3
 cookie=0x5adc15c0, duration=6.972s, table=2, n_packets=18, n_bytes=1488, priority=0 actions=goto_table:3
 cookie=0x5adc15c0, duration=6.973s, table=3, n_packets=0, n_bytes=0, priority=8240,dl_dst=01:00:0c:cc:cc:cd actions=drop
 cookie=0x5adc15c0, duration=6.973s, table=3, n_packets=0, n_bytes=0, priority=8240,dl_vlan=100,dl_dst=ff:ff:ff:ff:ff:ff actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=6.973s, table=3, n_packets=0, n_bytes=0, priority=8236,dl_dst=01:80:c2:00:00:00/ff:ff:ff:ff:ff:f0 actions=drop
 cookie=0x5adc15c0, duration=6.973s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:80:c2:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=6.973s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:00:5e:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=6.973s, table=3, n_packets=18, n_bytes=1488, priority=8208,dl_vlan=100,dl_dst=33:33:00:00:00:00/ff:ff:00:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=6.973s, table=3, n_packets=0, n_bytes=0, priority=8192,dl_vlan=100 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=6.972s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop




tigarto@fuck-pc:~$ sudo ovs-ofctl dump-ports sw1 --protocols=OpenFlow13
OFPST_PORT reply (OF1.3) (xid=0x2): 4 ports
  port LOCAL: rx pkts=0, bytes=0, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=0, bytes=0, drop=0, errs=0, coll=0
           duration=22.557s
  port  1: rx pkts=8, bytes=656, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=41, bytes=4857, drop=0, errs=0, coll=0
           duration=22.561s
  port  2: rx pkts=8, bytes=656, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=41, bytes=4857, drop=0, errs=0, coll=0
           duration=22.561s
  port  3: rx pkts=8, bytes=656, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=41, bytes=4857, drop=0, errs=0, coll=0
           duration=22.561s
tigarto@fuck-pc:~$ 



{
    "1": [
        {
            "packet_count": 96,
            "byte_count": 7632,
            "flow_count": 24
        }
    ]
}


{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 40,
            "duration_nsec": 711000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 9,
            "tx_packets": 45,
            "rx_bytes": 726,
            "tx_bytes": 5270,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 40,
            "duration_nsec": 715000000,
            "port_no": 1
        },
        {
            "rx_packets": 9,
            "tx_packets": 45,
            "rx_bytes": 726,
            "tx_bytes": 5270,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 40,
            "duration_nsec": 715000000,
            "port_no": 2
        },
        {
            "rx_packets": 9,
            "tx_packets": 45,
            "rx_bytes": 726,
            "tx_bytes": 5270,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 40,
            "duration_nsec": 715000000,
            "port_no": 3
        }
    ]
}


```bash
# Terminal h1 (atacante)
hping3 --flood --rand-source 10.0.0.253
```



root@fuck-pc:~/Documents/tesis_2018-2/experimento-faucet/experimento-paper-mini
net/reunion_25-01-2019# date
lun ene 28 16:46:47 -05 2019
root@fuck-pc:~/Documents/tesis_2018-2/experimento-faucet/experimento-paper-mini
net/reunion_25-01-2019# hping3 --flood --rand-source 10.0.0.253
HPING 10.0.0.253 (h1-eth0 10.0.0.253): NO FLAGS are set, 40 headers + 0 data bytes
hping in flood mode, no replies will be shown
^C
--- 10.0.0.253 hping statistic ---
3567003 packets transmitted, 0 packets received, 100% packet loss
round-trip min/avg/max = 0.0/0.0/0.0 ms
root@fuck-pc:~/Documents/tesis_2018-2/experimento-faucet/experimento-paper-mini
net/reunion_25-01-2019# date
lun ene 28 16:47:08 -05 2019
root@fuck-pc:~/Documents/tesis_2018-2/experimento-faucet/experimento-paper-mini
net/reunion_25-01-2019# 




{
    "1": [
        {
            "packet_count": 10782964,
            "byte_count": 581300868,
            "flow_count": 24
        }
    ]
}


{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 187,
            "duration_nsec": 946000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 3567015,
            "tx_packets": 20511,
            "rx_bytes": 192619070,
            "tx_bytes": 865332,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 187,
            "duration_nsec": 950000000,
            "port_no": 1
        },
        {
            "rx_packets": 11,
            "tx_packets": 20511,
            "rx_bytes": 866,
            "tx_bytes": 865332,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 187,
            "duration_nsec": 950000000,
            "port_no": 2
        },
        {
            "rx_packets": 20469,
            "tx_packets": 3567057,
            "rx_bytes": 860102,
            "tx_bytes": 192624300,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 187,
            "duration_nsec": 950000000,
            "port_no": 3
        }
    ]
}



tigarto@fuck-pc:~$ sudo ovs-ofctl dump-flows sw1 --protocols=OpenFlow13
OFPST_FLOW reply (OF1.3) (xid=0x2):
 cookie=0x5adc15c0, duration=208.722s, table=0, n_packets=3567014, n_bytes=192618980, priority=9000,in_port=1,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=208.722s, table=0, n_packets=10, n_bytes=776, priority=9000,in_port=2,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=208.722s, table=0, n_packets=20468, n_bytes=860012, priority=9000,in_port=3,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=208.721s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x5adc15c0, duration=208.722s, table=1, n_packets=0, n_bytes=0, priority=20490,dl_type=0x9000 actions=drop
 cookie=0x5adc15c0, duration=208.722s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=ff:ff:ff:ff:ff:ff actions=drop
 cookie=0x5adc15c0, duration=208.722s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=0e:00:00:00:00:01 actions=drop
 cookie=0x5adc15c0, duration=208.587s, table=1, n_packets=3567013, n_bytes=192618890, hard_timeout=307, priority=8191,in_port=1,dl_vlan=100,dl_src=76:db:0f:46:8b:10 actions=goto_table:2
 cookie=0x5adc15c0, duration=208.521s, table=1, n_packets=8, n_bytes=600, hard_timeout=299, priority=8191,in_port=2,dl_vlan=100,dl_src=aa:9c:c0:e7:28:43 actions=goto_table:2
 cookie=0x5adc15c0, duration=208.493s, table=1, n_packets=20467, n_bytes=859926, hard_timeout=315, priority=8191,in_port=3,dl_vlan=100,dl_src=9a:de:01:50:f3:1d actions=goto_table:2
 cookie=0x5adc15c0, duration=208.722s, table=1, n_packets=4, n_bytes=352, priority=4096,dl_vlan=100 actions=CONTROLLER:96,goto_table:2
 cookie=0x5adc15c0, duration=208.721s, table=1, n_packets=0, n_bytes=0, priority=0 actions=goto_table:2
 cookie=0x5adc15c0, duration=208.587s, table=2, n_packets=1, n_bytes=42, idle_timeout=457, priority=8192,dl_vlan=100,dl_dst=76:db:0f:46:8b:10 actions=pop_vlan,output:1
 cookie=0x5adc15c0, duration=208.521s, table=2, n_packets=0, n_bytes=0, idle_timeout=449, priority=8192,dl_vlan=100,dl_dst=aa:9c:c0:e7:28:43 actions=pop_vlan,output:2
 cookie=0x5adc15c0, duration=208.493s, table=2, n_packets=3567003, n_bytes=192618162, idle_timeout=465, priority=8192,dl_vlan=100,dl_dst=9a:de:01:50:f3:1d actions=pop_vlan,output:3
 cookie=0x5adc15c0, duration=208.721s, table=2, n_packets=20488, n_bytes=861564, priority=0 actions=goto_table:3
 cookie=0x5adc15c0, duration=208.722s, table=3, n_packets=0, n_bytes=0, priority=8240,dl_dst=01:00:0c:cc:cc:cd actions=drop
 cookie=0x5adc15c0, duration=208.722s, table=3, n_packets=20458, n_bytes=859236, priority=8240,dl_vlan=100,dl_dst=ff:ff:ff:ff:ff:ff actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=208.722s, table=3, n_packets=0, n_bytes=0, priority=8236,dl_dst=01:80:c2:00:00:00/ff:ff:ff:ff:ff:f0 actions=drop
 cookie=0x5adc15c0, duration=208.722s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:80:c2:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=208.722s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:00:5e:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=208.722s, table=3, n_packets=30, n_bytes=2328, priority=8208,dl_vlan=100,dl_dst=33:33:00:00:00:00/ff:ff:00:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=208.722s, table=3, n_packets=0, n_bytes=0, priority=8192,dl_vlan=100 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=208.721s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop





tigarto@fuck-pc:~$ sudo ovs-ofctl dump-ports sw1 --protocols=OpenFlow13
OFPST_PORT reply (OF1.3) (xid=0x2): 4 ports
  port LOCAL: rx pkts=0, bytes=0, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=0, bytes=0, drop=0, errs=0, coll=0
           duration=224.812s
  port  1: rx pkts=3567015, bytes=192619070, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=20511, bytes=865332, drop=0, errs=0, coll=0
           duration=224.816s
  port  2: rx pkts=11, bytes=866, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=20511, bytes=865332, drop=0, errs=0, coll=0
           duration=224.816s
  port  3: rx pkts=20469, bytes=860102, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=3567057, bytes=192624300, drop=0, errs=0, coll=0
           duration=224.816s
tigarto@fuck-pc:~$ 


Durante el ataque se hicieron los siguientes comandos:







containernet> iperf
*** Iperf: testing TCP bandwidth between h1 and h3 
*** Results: ['33.2 Gbits/sec', '33.2 Gbits/sec']
containernet> iperf h2 h3
*** Iperf: testing TCP bandwidth between h2 and h3 
*** Results: ['32.4 Gbits/sec', '32.4 Gbits/sec']
containernet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 
h2 -> h1 h3 
h3 -> h1 h2 
*** Results: 0% dropped (6/6 received)
containernet> 


Se ve inmunidad en la aplicacion.




**Caso 2**: Con el iperf

tigarto@fuck-pc:~$ sudo ovs-ofctl dump-flows sw1 --protocols=OpenFlow13
OFPST_FLOW reply (OF1.3) (xid=0x2):
 cookie=0x5adc15c0, duration=40.913s, table=0, n_packets=8, n_bytes=636, priority=9000,in_port=1,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=40.913s, table=0, n_packets=7, n_bytes=546, priority=9000,in_port=2,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=40.913s, table=0, n_packets=8, n_bytes=636, priority=9000,in_port=3,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=40.912s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x5adc15c0, duration=40.913s, table=1, n_packets=0, n_bytes=0, priority=20490,dl_type=0x9000 actions=drop
 cookie=0x5adc15c0, duration=40.913s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=ff:ff:ff:ff:ff:ff actions=drop
 cookie=0x5adc15c0, duration=40.913s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=0e:00:00:00:00:01 actions=drop
 cookie=0x5adc15c0, duration=40.777s, table=1, n_packets=7, n_bytes=550, hard_timeout=287, priority=8191,in_port=1,dl_vlan=100,dl_src=2e:17:8b:e7:c7:f5 actions=goto_table:2
 cookie=0x5adc15c0, duration=40.703s, table=1, n_packets=7, n_bytes=546, hard_timeout=320, priority=8191,in_port=3,dl_vlan=100,dl_src=3e:3c:d4:e6:48:9c actions=goto_table:2
 cookie=0x5adc15c0, duration=40.619s, table=1, n_packets=6, n_bytes=460, hard_timeout=299, priority=8191,in_port=2,dl_vlan=100,dl_src=66:84:9f:db:fc:62 actions=goto_table:2
 cookie=0x5adc15c0, duration=40.912s, table=1, n_packets=3, n_bytes=262, priority=4096,dl_vlan=100 actions=CONTROLLER:96,goto_table:2
 cookie=0x5adc15c0, duration=40.912s, table=1, n_packets=0, n_bytes=0, priority=0 actions=goto_table:2
 cookie=0x5adc15c0, duration=40.777s, table=2, n_packets=0, n_bytes=0, idle_timeout=437, priority=8192,dl_vlan=100,dl_dst=2e:17:8b:e7:c7:f5 actions=pop_vlan,output:1
 cookie=0x5adc15c0, duration=40.703s, table=2, n_packets=0, n_bytes=0, idle_timeout=470, priority=8192,dl_vlan=100,dl_dst=3e:3c:d4:e6:48:9c actions=pop_vlan,output:3
 cookie=0x5adc15c0, duration=40.619s, table=2, n_packets=0, n_bytes=0, idle_timeout=449, priority=8192,dl_vlan=100,dl_dst=66:84:9f:db:fc:62 actions=pop_vlan,output:2
 cookie=0x5adc15c0, duration=40.912s, table=2, n_packets=23, n_bytes=1818, priority=0 actions=goto_table:3
 cookie=0x5adc15c0, duration=40.913s, table=3, n_packets=0, n_bytes=0, priority=8240,dl_dst=01:00:0c:cc:cc:cd actions=drop
 cookie=0x5adc15c0, duration=40.913s, table=3, n_packets=0, n_bytes=0, priority=8240,dl_vlan=100,dl_dst=ff:ff:ff:ff:ff:ff actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=40.913s, table=3, n_packets=0, n_bytes=0, priority=8236,dl_dst=01:80:c2:00:00:00/ff:ff:ff:ff:ff:f0 actions=drop
 cookie=0x5adc15c0, duration=40.912s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:80:c2:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=40.912s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:00:5e:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=40.912s, table=3, n_packets=23, n_bytes=1818, priority=8208,dl_vlan=100,dl_dst=33:33:00:00:00:00/ff:ff:00:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=40.912s, table=3, n_packets=0, n_bytes=0, priority=8192,dl_vlan=100 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=40.912s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
tigarto@fuck-pc:~$ 


tigarto@fuck-pc:~$ sudo ovs-ofctl dump-ports sw1 --protocols=OpenFlow13
OFPST_PORT reply (OF1.3) (xid=0x2): 4 ports
  port LOCAL: rx pkts=0, bytes=0, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=0, bytes=0, drop=0, errs=0, coll=0
           duration=5.301s
  port  1: rx pkts=7, bytes=586, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=28, bytes=3469, drop=0, errs=0, coll=0
           duration=5.305s
  port  2: rx pkts=7, bytes=586, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=27, bytes=3288, drop=0, errs=0, coll=0
           duration=5.304s
  port  3: rx pkts=6, bytes=516, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=28, bytes=3338, drop=0, errs=0, coll=0
           duration=5.304s


{
    "1": [
        {
            "packet_count": 104,
            "byte_count": 8112,
            "flow_count": 24
        }
    ]
}


{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 76,
            "duration_nsec": 523000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 10,
            "tx_packets": 48,
            "rx_bytes": 796,
            "tx_bytes": 5593,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 76,
            "duration_nsec": 527000000,
            "port_no": 1
        },
        {
            "rx_packets": 10,
            "tx_packets": 49,
            "rx_bytes": 796,
            "tx_bytes": 5683,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 76,
            "duration_nsec": 526000000,
            "port_no": 2
        },
        {
            "rx_packets": 10,
            "tx_packets": 48,
            "rx_bytes": 796,
            "tx_bytes": 5593,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 76,
            "duration_nsec": 526000000,
            "port_no": 3
        }
    ]
}


```bash
# Terminal h3 (atacante)
hping3 --flood --rand-source 10.0.0.253
```



```bash
# Terminal h3 (servidor)
iperf3 -s -p 5003
```

[ 19] 197.00-198.00 sec  2.91 GBytes  25.0 Gbits/sec                  
[ 19] 198.00-199.00 sec  3.18 GBytes  27.3 Gbits/sec                  
[ 19] 199.00-200.00 sec  1.34 GBytes  11.5 Gbits/sec                  
[ 19] 200.00-200.04 sec  44.4 MBytes  8.41 Gbits/sec                  
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[ 19]   0.00-200.04 sec   618 GBytes  26.5 Gbits/sec  11376             sender
[ 19]   0.00-200.04 sec   618 GBytes  26.5 Gbits/sec                  receiver
-----------------------------------------------------------
Server listening on 5003
-----------------------------------------------------------


```bash
# Terminal h2 (cliente)
iperf3 -c 10.0.0.253 -p 5003 -i 0.5 -t 200 
```


[ 18] 198.00-198.50 sec  1.56 GBytes  26.8 Gbits/sec    0   3.67 MBytes       
[ 18] 198.50-199.00 sec  1.59 GBytes  27.3 Gbits/sec    0   3.68 MBytes       
[ 18] 199.00-199.50 sec   732 MBytes  12.3 Gbits/sec    0   3.69 MBytes       
[ 18] 199.50-200.01 sec   576 MBytes  9.56 Gbits/sec   90   2.68 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[ 18]   0.00-200.01 sec   618 GBytes  26.5 Gbits/sec  11376             sender
[ 18]   0.00-200.01 sec   618 GBytes  26.5 Gbits/sec                  receiver

iperf Done.


```bash
# Terminal h1 (atacante)
hping3 --flood --rand-source 10.0.0.253
```


root@fuck-pc:~/Documents/tesis_2018-2/experimento-faucet/experimento-paper-mini
net/reunion_25-01-2019# hping3 --flood --rand-source 10.0.0.253
HPING 10.0.0.253 (h1-eth0 10.0.0.253): NO FLAGS are set, 40 headers + 0 data bytes
hping in flood mode, no replies will be shown
^C
--- 10.0.0.253 hping statistic ---
25323461 packets transmitted, 0 packets received, 100% packet loss
round-trip min/avg/max = 0.0/0.0/0.0 ms
root@fuck-pc:~/Documents/tesis_2018-2/experimento-faucet/experimento-paper-mini
net/reunion_25-01-2019# 


tigarto@fuck-pc:~$ sudo ovs-ofctl dump-flows sw1 --protocols=OpenFlow13
OFPST_FLOW reply (OF1.3) (xid=0x2):
 cookie=0x5adc15c0, duration=495.738s, table=0, n_packets=25323479, n_bytes=1367468062, priority=9000,in_port=1,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=495.738s, table=0, n_packets=12749294, n_bytes=664336520640, priority=9000,in_port=2,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=495.738s, table=0, n_packets=6079654, n_bytes=401335682, priority=9000,in_port=3,vlan_tci=0x0000/0x1fff actions=push_vlan:0x8100,set_field:4196->vlan_vid,goto_table:1
 cookie=0x5adc15c0, duration=495.737s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x5adc15c0, duration=495.738s, table=1, n_packets=0, n_bytes=0, priority=20490,dl_type=0x9000 actions=drop
 cookie=0x5adc15c0, duration=495.738s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=ff:ff:ff:ff:ff:ff actions=drop
 cookie=0x5adc15c0, duration=495.738s, table=1, n_packets=0, n_bytes=0, priority=20480,dl_src=0e:00:00:00:00:01 actions=drop
 cookie=0x5adc15c0, duration=207.818s, table=1, n_packets=7526238, n_bytes=406416844, hard_timeout=317, priority=8191,in_port=1,dl_vlan=100,dl_src=2e:17:8b:e7:c7:f5 actions=goto_table:2
 cookie=0x5adc15c0, duration=195.695s, table=1, n_packets=2438810, n_bytes=128322460136, hard_timeout=288, priority=8191,in_port=2,dl_vlan=100,dl_src=66:84:9f:db:fc:62 actions=goto_table:2
 cookie=0x5adc15c0, duration=174.637s, table=1, n_packets=503175, n_bytes=33212176, hard_timeout=297, priority=8191,in_port=3,dl_vlan=100,dl_src=3e:3c:d4:e6:48:9c actions=goto_table:2
 cookie=0x5adc15c0, duration=495.737s, table=1, n_packets=27855, n_bytes=1495705926, priority=4096,dl_vlan=100 actions=CONTROLLER:96,goto_table:2
 cookie=0x5adc15c0, duration=495.737s, table=1, n_packets=0, n_bytes=0, priority=0 actions=goto_table:2
 cookie=0x5adc15c0, duration=495.602s, table=2, n_packets=6, n_bytes=252, idle_timeout=437, priority=8192,dl_vlan=100,dl_dst=2e:17:8b:e7:c7:f5 actions=pop_vlan,output:1
 cookie=0x5adc15c0, duration=495.444s, table=2, n_packets=6079637, n_bytes=401334584, idle_timeout=449, priority=8192,dl_vlan=100,dl_dst=66:84:9f:db:fc:62 actions=pop_vlan,output:2
 cookie=0x5adc15c0, duration=174.637s, table=2, n_packets=5040496, n_bytes=64505818576, idle_timeout=447, priority=8192,dl_vlan=100,dl_dst=3e:3c:d4:e6:48:9c actions=pop_vlan,output:3
 cookie=0x5adc15c0, duration=495.737s, table=2, n_packets=35, n_bytes=2602, priority=0 actions=goto_table:3
 cookie=0x5adc15c0, duration=495.738s, table=3, n_packets=0, n_bytes=0, priority=8240,dl_dst=01:00:0c:cc:cc:cd actions=drop
 cookie=0x5adc15c0, duration=495.738s, table=3, n_packets=2, n_bytes=84, priority=8240,dl_vlan=100,dl_dst=ff:ff:ff:ff:ff:ff actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=495.738s, table=3, n_packets=0, n_bytes=0, priority=8236,dl_dst=01:80:c2:00:00:00/ff:ff:ff:ff:ff:f0 actions=drop
 cookie=0x5adc15c0, duration=495.737s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:80:c2:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=495.737s, table=3, n_packets=0, n_bytes=0, priority=8216,dl_vlan=100,dl_dst=01:00:5e:00:00:00/ff:ff:ff:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=495.737s, table=3, n_packets=33, n_bytes=2518, priority=8208,dl_vlan=100,dl_dst=33:33:00:00:00:00/ff:ff:00:00:00:00 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=495.737s, table=3, n_packets=0, n_bytes=0, priority=8192,dl_vlan=100 actions=pop_vlan,output:1,output:2,output:3
 cookie=0x5adc15c0, duration=495.737s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop



tigarto@fuck-pc:~$ sudo ovs-ofctl dump-ports sw1 --protocols=OpenFlow13
OFPST_PORT reply (OF1.3) (xid=0x2): 4 ports
  port LOCAL: rx pkts=0, bytes=0, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=0, bytes=0, drop=0, errs=0, coll=0
           duration=534.180s
  port  1: rx pkts=25323480, bytes=1367468152, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=65, bytes=6986, drop=0, errs=0, coll=0
           duration=534.184s
  port  2: rx pkts=12749296, bytes=664336520820, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=6079698, bytes=401341478, drop=0, errs=0, coll=0
           duration=534.183s
  port  3: rx pkts=6079656, bytes=401335842, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=38062761, bytes=665696384478, drop=0, errs=0, coll=0
           duration=534.183s



{
    "1": [
        {
            "packet_count": 65768710,
            "byte_count": 861270277802,
            "flow_count": 24
        }
    ]
}



{
    "1": [
        {
            "rx_packets": 0,
            "tx_packets": 0,
            "rx_bytes": 0,
            "tx_bytes": 0,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 479,
            "duration_nsec": 266000000,
            "port_no": "LOCAL"
        },
        {
            "rx_packets": 25323480,
            "tx_packets": 63,
            "rx_bytes": 1367468152,
            "tx_bytes": 6713,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 479,
            "duration_nsec": 270000000,
            "port_no": 1
        },
        {
            "rx_packets": 12749296,
            "tx_packets": 6079696,
            "rx_bytes": 664336520820,
            "tx_bytes": 401341205,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 479,
            "duration_nsec": 269000000,
            "port_no": 2
        },
        {
            "rx_packets": 6079655,
            "tx_packets": 38062760,
            "rx_bytes": 401335772,
            "tx_bytes": 665696384275,
            "rx_dropped": 0,
            "tx_dropped": 0,
            "rx_errors": 0,
            "tx_errors": 0,
            "rx_frame_err": 0,
            "rx_over_err": 0,
            "rx_crc_err": 0,
            "collisions": 0,
            "duration_sec": 479,
            "duration_nsec": 269000000,
            "port_no": 3
        }
    ]
}



A medida que se esta ejecutando el ataque:



containernet> iperf
*** Iperf: testing TCP bandwidth between h1 and h3 
*** Results: ['33.2 Gbits/sec', '33.3 Gbits/sec']
containernet> iperf h2 h3
*** Iperf: testing TCP bandwidth between h2 and h3 
*** Results: ['32.4 Gbits/sec', '32.4 Gbits/sec']
containernet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 
h2 -> h1 h3 
h3 -> h1 h2 
*** Results: 0% dropped (6/6 received)




+++++

faucet --ryu-app simple_switch_13.py  --ryu-app ofctl_rest.py


-------------------------
/home/tigarto/Documents/tesis_2018-2/experimento-faucet/experimento-paper-mininet/reunion_25-01-2019



sudo mn --topo single,3 --mac --controller remote --switch ovsk,protocols=OpenFlow13
ovs-vsctl set bridge s1 protocols=OpenFlow13


ryu-manager --verbose simple_switch_13.py ofctl_rest.py




tigarto@fuck-pc:~$ sudo ovs-ofctl dump-flows s1 --protocols=OpenFlow13
OFPST_FLOW reply (OF1.3) (xid=0x2):
 cookie=0x0, duration=21.127s, table=0, n_packets=21, n_bytes=1758, priority=0 actions=CONTROLLER:65535


tigarto@fuck-pc:~$ sudo ovs-ofctl dump-ports s1 --protocols=OpenFlow13
OFPST_PORT reply (OF1.3) (xid=0x2): 4 ports
  port LOCAL: rx pkts=0, bytes=0, drop=24, errs=0, frame=0, over=0, crc=0
           tx pkts=0, bytes=0, drop=0, errs=0, coll=0
           duration=43.325s
  port  1: rx pkts=10, bytes=856, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=47, bytes=5490, drop=0, errs=0, coll=0
           duration=43.332s
  port  2: rx pkts=10, bytes=856, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=46, bytes=5400, drop=0, errs=0, coll=0
           duration=43.332s
  port  3: rx pkts=10, bytes=856, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=46, bytes=5400, drop=0, errs=0, coll=0
           duration=43.332s



{
    "1": [
        {
            "packet_count": 24,
            "byte_count": 1968,
            "flow_count": 1
        }
    ]
}


{
    "1": [
        {
            "duration_sec": 72,
            "rx_crc_err": 0,
            "rx_bytes": 0,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 0,
            "port_no": "LOCAL",
            "rx_dropped": 27,
            "rx_frame_err": 0,
            "tx_bytes": 0,
            "rx_packets": 0,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 961000000
        },
        {
            "duration_sec": 72,
            "rx_crc_err": 0,
            "rx_bytes": 926,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 51,
            "port_no": 1,
            "rx_dropped": 0,
            "rx_frame_err": 0,
            "tx_bytes": 5903,
            "rx_packets": 11,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 968000000
        },
        {
            "duration_sec": 72,
            "rx_crc_err": 0,
            "rx_bytes": 926,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 50,
            "port_no": 2,
            "rx_dropped": 0,
            "rx_frame_err": 0,
            "tx_bytes": 5813,
            "rx_packets": 11,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 968000000
        },
        {
            "duration_sec": 72,
            "rx_crc_err": 0,
            "rx_bytes": 926,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 50,
            "port_no": 3,
            "rx_dropped": 0,
            "rx_frame_err": 0,
            "tx_bytes": 5813,
            "rx_packets": 11,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 968000000
        }
    ]
}

containernet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 
h2 -> h1 h3 
h3 -> h1 h2 
*** Results: 0% dropped (6/6 received)


tigarto@fuck-pc:~$ sudo ovs-ofctl dump-flows s1 --protocols=OpenFlow13
OFPST_FLOW reply (OF1.3) (xid=0x2):
 cookie=0x0, duration=17.598s, table=0, n_packets=4, n_bytes=280, priority=1,in_port=2,dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01 actions=output:1
 cookie=0x0, duration=17.596s, table=0, n_packets=3, n_bytes=238, priority=1,in_port=1,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02 actions=output:2
 cookie=0x0, duration=17.589s, table=0, n_packets=4, n_bytes=280, priority=1,in_port=3,dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:01 actions=output:1
 cookie=0x0, duration=17.588s, table=0, n_packets=3, n_bytes=238, priority=1,in_port=1,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:03 actions=output:3
 cookie=0x0, duration=17.583s, table=0, n_packets=4, n_bytes=280, priority=1,in_port=3,dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:02 actions=output:2
 cookie=0x0, duration=17.582s, table=0, n_packets=3, n_bytes=238, priority=1,in_port=2,dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:03 actions=output:3
 cookie=0x0, duration=104.281s, table=0, n_packets=36, n_bytes=2724, priority=0 actions=CONTROLLER:65535


tigarto@fuck-pc:~$ sudo ovs-ofctl dump-ports s1 --protocols=OpenFlow13
OFPST_PORT reply (OF1.3) (xid=0x2): 4 ports
  port LOCAL: rx pkts=0, bytes=0, drop=32, errs=0, frame=0, over=0, crc=0
           tx pkts=0, bytes=0, drop=0, errs=0, coll=0
           duration=122.750s
  port  1: rx pkts=19, bytes=1486, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=63, bytes=6715, drop=0, errs=0, coll=0
           duration=122.757s
  port  2: rx pkts=20, bytes=1556, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=61, bytes=6555, drop=0, errs=0, coll=0
           duration=122.757s
  port  3: rx pkts=20, bytes=1556, drop=0, errs=0, frame=0, over=0, crc=0
           tx pkts=60, bytes=6485, drop=0, errs=0, coll=0
           duration=122.757s

{
    "1": [
        {
            "packet_count": 60,
            "byte_count": 4488,
            "flow_count": 7
        }
    ]
}



{
    "1": [
        {
            "duration_sec": 148,
            "rx_crc_err": 0,
            "rx_bytes": 0,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 0,
            "port_no": "LOCAL",
            "rx_dropped": 33,
            "rx_frame_err": 0,
            "tx_bytes": 0,
            "rx_packets": 0,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 559000000
        },
        {
            "duration_sec": 148,
            "rx_crc_err": 0,
            "rx_bytes": 1556,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 64,
            "port_no": 1,
            "rx_dropped": 0,
            "rx_frame_err": 0,
            "tx_bytes": 6918,
            "rx_packets": 20,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 566000000
        },
        {
            "duration_sec": 148,
            "rx_crc_err": 0,
            "rx_bytes": 1556,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 63,
            "port_no": 2,
            "rx_dropped": 0,
            "rx_frame_err": 0,
            "tx_bytes": 6828,
            "rx_packets": 20,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 566000000
        },
        {
            "duration_sec": 148,
            "rx_crc_err": 0,
            "rx_bytes": 1556,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 63,
            "port_no": 3,
            "rx_dropped": 0,
            "rx_frame_err": 0,
            "tx_bytes": 6828,
            "rx_packets": 20,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 566000000
        }
    ]
}



packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
(22545) accepted ('10.1.93.187', 49214)
10.1.93.187 - - [28/Jan/2019 17:44:16] "GET /metrics HTTP/1.1" 404 278 0.000597
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1
EVENT ofp_event->SimpleSwitch13 EventOFPPacketIn
packet in 1 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff 1


{
    "1": [
        {
            "packet_count": 1715746,
            "byte_count": 55962603876,
            "flow_count": 7
        }
    ]
}


{
    "1": [
        {
            "duration_sec": 369,
            "rx_crc_err": 0,
            "rx_bytes": 0,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 0,
            "port_no": "LOCAL",
            "rx_dropped": 186,
            "rx_frame_err": 0,
            "tx_bytes": 0,
            "rx_packets": 0,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 441000000
        },
        {
            "duration_sec": 369,
            "rx_crc_err": 0,
            "rx_bytes": 55922783502,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 603333,
            "port_no": 1,
            "rx_dropped": 0,
            "rx_frame_err": 0,
            "tx_bytes": 39823817,
            "rx_packets": 1112427,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 448000000
        },
        {
            "duration_sec": 369,
            "rx_crc_err": 0,
            "rx_bytes": 3012,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 240,
            "port_no": 2,
            "rx_dropped": 0,
            "rx_frame_err": 0,
            "tx_bytes": 15539,
            "rx_packets": 38,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 448000000
        },
        {
            "duration_sec": 369,
            "rx_crc_err": 0,
            "rx_bytes": 39817542,
            "rx_errors": 0,
            "tx_dropped": 0,
            "collisions": 0,
            "tx_packets": 1112480,
            "port_no": 3,
            "rx_dropped": 0,
            "rx_frame_err": 0,
            "tx_bytes": 55922789771,
            "rx_packets": 603281,
            "rx_over_err": 0,
            "tx_errors": 0,
            "duration_nsec": 448000000
        }
    ]
}




***************************************************************************************************************************


Get aggregate flow stats
Get aggregate flow stats of the switch which specified with Datapath ID in URI.






Get all flows stats of the switch which specified with Datapath ID in URI.




Resultados co

curl -X GET http://localhost:8080/stats/flow/1mandos




ryu.app.ofctl_rest provides REST APIs for retrieving the switch stats and Updating the switch stats. This application helps you debug your application and get various statistics.






https://github.com/CyberReboot/vent


