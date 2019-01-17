#!/usr/bin/env python3
import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def connect_socket():
    HOST = "www.google.com"
    PORT = 80
    BUFFER_SIZE = 1024
    payload = """GET / HTTP/1.0
    Host: {HOST}

    """.format(HOST=HOST)
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    addr = addr_info[0]
    (family, socket_type, proto, cannon_name, sock_addr) = addr
    try:
        s = socket.socket(family, socket_type, proto)
        s.connect(sock_addr)
        s.sendall(payload.encode())
        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data
        return full_data
    except:
        print("DID NOT CONNECT")
        pass
    finally:
        s.close()
    return "FAILED".encode()

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
            conn.sendall(connect_socket())
except KeyboardInterrupt:
    s.close()
    exit()