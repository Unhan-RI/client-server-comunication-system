import socket
import threading
import time

def client_program(host='127.0.0.1', port=5555, message="Hello, Server"):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Mencatat waktu sebelum koneksi dibuat
    connect_time = time.time()
    client.connect((host, port))
    
    # Mencatat waktu setelah koneksi berhasil
    post_connect_time = time.time()
    print(f"[{post_connect_time:.6f}] Connected to server at {host}:{port}")
    
    # Mencatat waktu sebelum pengiriman pesan
    send_time = time.time()
    client.send(message.encode('utf-8'))
    print(f"[{send_time:.6f}] Sent: {message}")
    
    # Mencatat waktu setelah menerima balasan dari server
    reply = client.recv(1024).decode('utf-8')
    receive_time = time.time()
    print(f"[{receive_time:.6f}] Server replied: {reply}")
    
    # Menghitung dan menampilkan waktu respons
    response_time = (receive_time - send_time) * 1000  # dalam milidetik
    print(f"[INFO] Response time: {response_time:.3f} ms")

    client.close()

if __name__ == "__main__":
    for i in range(100):  # Uji dengan 5 client secara bersamaan
        threading.Thread(target=client_program, args=( '127.0.0.1', 5555, f"Message from Client {i+1}")).start()
        time.sleep(0.1)  # Sedikit jeda antar client
