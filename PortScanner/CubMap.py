<<<<<<< HEAD
import socket

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.00001)
    try:
        scanner.connect((ip, port))
        return True
    except:
        return False
    finally:
        scanner.close()


def scan_ports(ip, startPort = 0, endPort = 1024):
    print(f"Scanning {ip}, from port {startPort} to {endPort}")
    for port in range(startPort, endPort+1):
        if scan_port(ip, port):
            print(f"Port {port} is open.")


target_ip = input("Target's ip address: ")
scan_ports(target_ip, 0, 80000)









=======
import socket

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.00001)
    try:
        scanner.connect((ip, port))
        return True
    except:
        return False
    finally:
        scanner.close()


def scan_ports(ip, startPort = 0, endPort = 1024):
    print(f"Scanning {ip}, from port {startPort} to {endPort}")
    for port in range(startPort, endPort+1):
        if scan_port(ip, port):
            print(f"Port {port} is open.")


target_ip = input("Target's ip address: ")
scan_ports(target_ip, 0, 80000)










>>>>>>> 4e34566d8118192411aa758ba2b4fca18ae04ee0
