import platform
import subprocess
import datetime
import json
from pathlib import Path
from re import search

class Scan:
    def __init__(self, base_ip, output):
        self.base_ip = base_ip
        self.output = output
    
    @staticmethod
    def ping_ip(ip):
        print(f'Scanning IP: {ip}', end=' ... ')

        param = "-n" if platform.system().lower() == "windows" else "-c"
        ttl_data = ""
        ttl_value = None
        output = False

        command = ["ping", param, "1", ip]
        response = subprocess.Popen(command, stdout=subprocess.PIPE)
        response.wait()


        for line in response.stdout:
            ttl_data += str(line, 'utf-8')
            ttl_match = search(r"TTL=(\d+)", ttl_data)

            if ttl_match:
                ttl_value = ttl_match.group(1)


        if ttl_value:
            status = "Ativo"
            status_char = "✔"
            output = True
        else:
            status = "Inativo"
            status_char = "✘"
        
        print(f"{status_char} {status}")
        
        return [output, ttl_value]

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
                    check_ip = self.ping_ip(ip)

                    if check_ip[0]:
                        ip_info = f"IP: {ip} <--> Possible(s) OS: {check_ip[1]}"
                        active_ips.append(ip_info)
        else:
            for i in range(0,3):
                ip = f"{prefix}.{i}"
                check_ip = self.ping_ip(ip)

                print(check_ip[0])

                if check_ip[0]:
                    ip_info = f"IP: {ip} <--> Possible(s) OS: {check_ip[1]}"
                    active_ips.append(ip_info)

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

    def device_identifier(self, TTL):
        
        project_root = Path(__file__).resolve().parent.parent
        ttl_list_path = project_root/"resources"/"ttl_list.json"
        response = ""

        with open(ttl_list_path, 'r') as file:
            ttl_list = json.load(file)

        for key, value in ttl_list.items():
            if TTL == key:
                for os_name in value:
                    response = response + f"{os_name} / "

        if response == "":
            response = "No possible OS found"
        else:
            response = response[:-3]
        
        return response