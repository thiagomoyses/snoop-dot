import platform
import subprocess
import datetime
from re import findall

class Scan:
    def __init__(self, base_ip, output):
        self.base_ip = base_ip
        self.output = output
    
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

        print(f"{len(active_ips) } active IP(s) found.")

        # Save Ips in a txt
        if active_ips and self.output:

            #Create name for file
            file_name = f"active_ip_list-{datetime.datetime.now()}.txt"
            file_name = file_name.replace(" ", "-").replace(":", "-")

            with open(file_name, "w") as f:
                for ip in active_ips:
                    f.write(f"{ip}\n")
            print(f"Saved in -> {file_name}")