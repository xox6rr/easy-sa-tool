import nmap

def nmap_scan(target):
    nm = nmap.PortScanner()
    output = []
    open_ports = []

    nm.scan(target, arguments="-T4 --top-ports 100")

    for host in nm.all_hosts():
        output.append(f"Host: {host}")
        output.append(f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            output.append(f"\nProtocol: {proto}")

            for port in nm[host][proto]:
                service = nm[host][proto][port]
                open_ports.append(port)

                output.append(
                    f"Port {port} | "
                    f"State: {service['state']} | "
                    f"Service: {service['name']} | "
                    f"Version: {service.get('version','N/A')}"
                )

    return "\n".join(output), open_ports
