# Experimento 1 #

## Resumen ##

Test de conectividad con pings

## Comandos a emplear ##


Consola del servidor h3 donde IP(h3) = 10.0.0.253 

```bash
# Servidor  
iperf -s -p 5566 -i 1
```

Luego en el cliente, h1 (con IP(h1) = 10.0.0.251) para el caso.

```bash
# Cliente h1  
iperf -c 10.0.0.253 -p 5566 -t 20
```

```bash
# Cliente h2  
iperf -c 10.0.0.253 -p 5566 -t 20
```

**Preguntas**:
¿Que pasa si se hace individual cada prueba?
¿Que pasa para el caso simultaneo?

Cuando culmine el experimento reiniciar.


## Resultados obtenidos ##


