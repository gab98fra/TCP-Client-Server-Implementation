import socket

def start_server():
    # Create TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server_address = ('localhost', 5000)
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server started on localhost:5000")
    
    while True:
        print("Waiting for connections...")
        client_socket, client_address = server_socket.accept()
        
        try:
            print(f"Client connected from {client_address}")
            
            while True:
                # Recieve data
                data = client_socket.recv(1024).decode('utf-8')
                
                if not data:
                    break
                
                print(f"Message received: {data}")
                
                # Verify message: "DESCONEXION"
                if data == "DESCONEXION":
                    print("Client requested disconnection")
                    break
                
                # Convert message to uppercase and send response
                response = data.upper()
                client_socket.send(response.encode('utf-8'))
                
        finally:
            print("Closing connection with client")
            client_socket.close()

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nServer stopped")
    except Exception as e:
        print(f"Error: {e}")


