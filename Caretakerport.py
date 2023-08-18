import socket

def scan_ports(target, ports):
    open_ports = []
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Adjust the timeout as needed
        
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        
        sock.close()
    
    return open_ports

def main():
    target = input("Enter the target IP address: ")
    port_range = range(1, 100)  # Adjust the range of ports to scan
    
    open_ports = scan_ports(target, port_range)
    
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
