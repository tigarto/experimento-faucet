# Experimento 1 #

## Resumen ##

Test de conectividad con pings

## Comandos a emplear ##

```bash
h1 ping -c 100 -i 0.5 h3
```

Cuando culmine el experimento reiniciar.


## Resultados obtenidos ##

```bash
Start : Mon Jan 21 17:29:03 2019
*** h1 : ('ping -c 100 -i 0.5 10.0.0.253',)
PING 10.0.0.253 (10.0.0.253) 56(84) bytes of data.
64 bytes from 10.0.0.253: icmp_seq=1 ttl=64 time=0.705 ms
64 bytes from 10.0.0.253: icmp_seq=2 ttl=64 time=0.091 ms
...

64 bytes from 10.0.0.253: icmp_seq=98 ttl=64 time=0.072 ms
64 bytes from 10.0.0.253: icmp_seq=99 ttl=64 time=0.067 ms
64 bytes from 10.0.0.253: icmp_seq=100 ttl=64 time=0.066 ms

--- 10.0.0.253 ping statistics ---
100 packets transmitted, 100 received, 0% packet loss, time 50689ms
rtt min/avg/max/mdev = 0.035/0.076/0.705/0.064 ms
End : Mon Jan 21 17:29:54 2019
```

