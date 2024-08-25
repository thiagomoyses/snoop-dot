import platform
import subprocess
from re import findall

class Scan:
    def __init__(self, base_ip):
        self.base_ip = base_ip
    
    @staticmethod
    def ping_ip(ip):
        print(f'Scanning IP: {ip}', end=' ... ')

        param = "-n" if platform.system().lower() == "windows" else "-c"
        ttl_data = ""
        output = False

        command = ["ping", param, "1", ip]
        response = subprocess.Popen(command, stdout=subprocess.PIPE)
        response.wait()


        for line in response.stdout:
            ttl_data = ttl_data + str(line)
            find_ttl = findall("TTL", ttl_data)


        if find_ttl:
            status = "Ativo"
            status_char = "✔"
            output = True
        else:
            status = "Inativo"
            status_char = "✘"
        
        print(f"{status_char} {status}")
        
        return output

    def scan_network(self):
        
        active_ips = []
        prefix = '.'.join(self.base_ip.split('.')[:2])
        test_last_2 = True
        
        if int(self.base_ip.split('.')[2]) != 0 and int(self.base_ip.split('.')[3]) == 0:
            prefix = '.'.join(self.base_ip.split('.')[:3])
            test_last_2 = False


        if test_last_2:
            for i in range(0, 256):
                for j in range(1, 256):
                    ip = f"{prefix}.{i}.{j}"
                    if self.ping_ip(ip):
                        active_ips.append(ip)
        else:
            for i in range(0,256):
                ip = f"{prefix}.{i}"
                if self.ping_ip(ip):
                    active_ips.append(ip)


        # Save Ips in a txt
        if active_ips:
            with open("active_ip_list.txt", "w") as f:
                for ip in active_ips:
                    f.write(f"{ip}\n")
            print(f"{len(active_ips)} Active IP(s) saved in -> active_ip_list.txt")
        else:
            print("No active IP found.")
