import platform
import subprocess

class Scan:
    def __init__(self, base_ip):
        self.base_ip = base_ip
    
    @staticmethod
    def ping_ip(ip):
        print(f'Scanning IP: {ip}', end=' ... ')


        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", ip]

        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if response.returncode == 0:
            status = "Ativo"
            status_char = "✔"
        else:
            status = "Inativo"
            status_char = "✘"
        
        print(f"{status_char} {status}")
        
        return response.returncode == 0

    def scan_network(self):
        
        active_ips = []

        # split the prefix of 3 octets and ignore the last octet of IP
        prefix = '.'.join(self.base_ip.split('.')[:2])

        for i in range(0, 256):
            for j in range(1, 256):
                ip = f"{prefix}.{i}.{j}"
                if self.ping_ip(ip):
                    print(f"Active IP Found: {ip}")
                    active_ips.append(ip)
        
        # Save Ips in a txt
        if active_ips:
            with open("active_ip_list.txt", "w") as f:
                for ip in active_ips:
                    f.write(f"{ip}\n")
            print(f"{len(active_ips)} Active IP(s) saved in -> active_ip_list.txt")
        else:
            print("No active IP found.")
