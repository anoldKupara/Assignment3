import socket
import threading
import time


def server_function():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345

    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        while True:
            try:
                client_socket, address = server_socket.accept()
                print(f"Server: Connection from {address}")

                message = "Hello from server!"
                client_socket.send(message.encode('utf-8'))

                client_socket.close()

            except Exception as e:
                print(f"Server: Error handling client connection: {e}")

    except Exception as e:
        print(f"Server error: {e}")

    finally:
        server_socket.close()
        print("Server socket closed")


def client_function():
    time.sleep(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345

    try:
        client_socket.connect((host, port))
        print(f"Client: Connected to server at {host}:{port}")

        message = client_socket.recv(1024).decode('utf-8')
        print(f"Client: Message from server: {message}")

    except ConnectionRefusedError:
        print("Client: Error: Could not connect to server")

    except Exception as e:
        print(f"Client error: {e}")

    finally:
        client_socket.close()
        print("Client socket closed")


def main():
    server_thread = threading.Thread(target=server_function)
    client_thread = threading.Thread(target=client_function)

    server_thread.start()
    client_thread.start()

    client_thread.join()

    print("Main program completed")


if __name__ == "__main__":
    main()