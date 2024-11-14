# Cliente y Servidor TCP en Python

Este proyecto implementa un servidor TCP y un cliente TCP en Python que se comunican entre sí en localhost usando el puerto 5000.

## Requisitos

- Python 3.x

## Instrucciones de Ejecución

1. Primero, inicie el servidor con python o python3 (según aplique):
```bash
python server.py
```
or

```bash
python3 server.py
```


2. En otra terminal, inicie el cliente con python o python3 (según aplique):
```bash
python client.py
```
or

```bash
python3 client.py
```

### Prueba 1: Mensaje Normal
1. Inicie el servidor en una terminal
2. Inicie el cliente en otra terminal
3. En el cliente, escriba un mensaje (por ejemplo: "hola servidor")
4. Verifique que el servidor responda con el mensaje en mayúsculas ("HOLA SERVIDOR")

### Prueba 2: Desconexión
1. Con servidor y cliente en ejecución
2. En el cliente, escriba "DESCONEXION"
3. Verifique que:
   - El cliente se desconecte y termine su ejecución
   - El servidor cierre la conexión con el cliente pero siga ejecutándose
   - El servidor quede listo para nuevas conexiones

## Características

- El servidor acepta conexiones en localhost:5000
- Convierte los mensajes recibidos a mayúsculas
- Maneja la desconexión apropiadamente
- Soporta múltiples conexiones secuenciales
