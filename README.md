# TCP Client and Server in Python

This project implements a TCP server and TCP client in Python that communicate with each other on localhost using port 5000.

## Requirements

- Python 3.x

## Running Instructions

1. First, start the server:
```bash
python server.py
```

2. In another terminal, start the client:
```bash
python client.py
```

## Manual Tests

### Test 1: Normal Message
1. Start the server in one terminal
2. Start the client in another terminal
3. In the client, type a message (e.g., "hello server")
4. Verify that the server responds with the message in uppercase ("HELLO SERVER")

### Test 2: Disconnection
1. With server and client running
2. In the client, type "DESCONEXION"
3. Verify that:
   - The client disconnects and ends its execution
   - The server closes the connection with that client but continues running
   - The server remains ready for new connections

## Features

- Server accepts connections on localhost:5000
- Converts received messages to uppercase
- Properly handles disconnection
- Supports multiple sequential connections


# Cliente y Servidor TCP en Python

En este proyecto se implementa un servidor y cliente TCP en Python que se comunican entre sí a través de localhost por el puerto 5000.

## Requisitos

- Python 3.x

## Instrucciones de Ejecución

1. Inicie el servidor con python o python3 (según aplique):
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
- Maneja la desconexión correctamente
- Soporta múltiples conexiones
