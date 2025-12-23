import socket
import requests
from nmap_scanner import nmap_scan

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP Address: {ip}")
        return ip
    except:
        print("[-] Could not resolve IP")
        return None

def scan_ports(ip):
    print("\n[+] Scanning common ports...")
    common_ports = [21, 22, 80, 443, 3306]
    
    for port in common_ports:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        sock.close()

def get_headers(url):
    print("\n[+] Fetching security headers...")
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        for h in ["Server", "X-Powered-By", "Content-Security-Policy"]:
            print(f"{h}: {headers.get(h, 'Not Found')}")
    except:
        print("[-] Could not fetch headers")

def main():
    print("=== Easy Cyber Security Scanner ===\n")
    target = input("Enter domain or IP: ")
    nmap_scan(target)

if __name__ == "__main__":
    main()
