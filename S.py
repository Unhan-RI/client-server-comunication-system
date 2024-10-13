import socket
import threading
import time

# Fungsi untuk menangani client secara terpisah
def handle_client(client_socket, client_address):
    with client_socket:
        # Mencatat waktu koneksi dalam detail mikrodetik
        connection_time = time.time()
        print(f"[{connection_time:.6f}] Connection from {client_address}")
        
        # Menerima pesan dari client
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                # Mencatat waktu penerimaan pesan
                receive_time = time.time()
                print(f"[{receive_time:.6f}] Received from {client_address}: {message}")
                
                # Mengirimkan balasan ke client
                reply = f"Echo: {message}"
                client_socket.send(reply.encode('utf-8'))
                
                # Mencatat waktu pengiriman balasan
                reply_time = time.time()
                print(f"[{reply_time:.6f}] Sent to {client_address}: {reply}")
                
                # Mencatat selisih waktu antara menerima dan mengirim balasan
                processing_time = (reply_time - receive_time) * 1000  # dalam milidetik
                print(f"[INFO] Processing time: {processing_time:.3f} ms")
                
            except ConnectionResetError:
                break

def start_server(host='192.168.0.109', port=5555):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Server listening on {host}:{port}")
    
    while True:
        client_socket, client_address = server.accept()
        # Menggunakan thread untuk menangani client secara bersamaan
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
