import socket
# import termcolor

def scan(target, ports):
    for port in ports:
        scan_port(target, port)

def scan_port (ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        print(f"[+] Port {port} is open")
    except:
        print(f"[-] Port {port} is closed")

targets = input("[*] Enter targets to scan (split multiple targets with ,): ")
ports = input("[*] Enter How Many Ports You Want to Scan: ")   
if ',' in targets:
    # print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    print(("[*] Scanning Target: " + targets))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), range(1, int(ports)))
else:
    scan(targets, range(1, int(ports)))

