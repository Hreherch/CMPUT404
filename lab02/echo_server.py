#!/usr/bin/env python3
import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)

        while True:
            conn, addr = s.accept()
            print("connected to: " + addr[0] + ":" + str(addr[1]))
            full_data = b""
            while True:
                data = conn.recv(BUFFER_SIZE)
                full_data += data
                if not data: break
            print(full_data)
            conn.sendall(full_data)
except KeyboardInterrupt:
    s.close()
    exit()