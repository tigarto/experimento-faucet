# Experimento 1 #

## Resumen ##

Test de conectividad con pings

## Comandos a emplear ##


Consola del servidor h3 donde IP(h3) = 10.0.0.253 

```bash
# Servidor  
iperf -s -p 5566 -i 0.5
```

Luego en el cliente, h1 (con IP(h1) = 10.0.0.251) para el caso.

```bash
# Cliente  
iperf -c 10.0.0.253 -p 5566 -t 25 -i 0.5
```

Cuando culmine el experimento reiniciar.


## Resultados obtenidos ##


