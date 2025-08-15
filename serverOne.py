import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 3000        # Port to listen on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        print(server_socket.accept())
        
        server_socket.accept()
        

if __name__ == "__main__":
    start_server()