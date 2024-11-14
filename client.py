import socket

def start_client():
    # Create TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5000)
    print(f"Connecting to {server_address}")
    client_socket.connect(server_address)
    
    try:
        while True:
            # Ask user for message
            message = input("Enter message (o DESCONEXION to exit): ")
            
            # Send message
            client_socket.send(message.encode('utf-8'))
            
            # If it's a disconnect message: DEXCONEXION, end
            if message == "DESCONEXION":
                print("Disconnecting from server...")
                break
            
            # Receive response
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server response: {response}")
            
    finally:
        print("Closing connection")
        client_socket.close()

if __name__ == "__main__":
    try:
        start_client()
    except KeyboardInterrupt:
        print("\nClient stopped")
    except Exception as e:
        print(f"Error: {e}")