import socket
import time



target = input("Enter the target IP address or hostname: ")
port = int(input("Enter the port: "))
start_time = time.time()


# Scanning single port
sock = socket.socket()
sock.settimeout(0.5)
try:
    sock.connect((target, port))
    print(f"Port {port} is OPEN")
except:
    pass
finally:
        sock.close()
