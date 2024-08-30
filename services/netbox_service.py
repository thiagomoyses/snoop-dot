import os
import pynetbox
from dotenv import load_dotenv

load_dotenv()

class Netbox:
    def __init__(self, ip_list):
        self.netbox_url = os.getenv('NETBOX_URL')
        self.netbox_token = os.getenv('NETBOX_TOKEN')
        self.netbox = pynetbox.api(self.netbox_url, token=self.netbox_token)
        self.ip_list = ip_list
    
    def send_ative_ips(self):
        for ip in self.ip_list:
            try:
                self.netbox.ipam.ip_addresses.create(
                    address=ip,
                    status="active"
                )
                print(f'IP {ip} sucessfully sent.')

            except pynetbox.RequestError as e:
                print(f'Error trying to send ip {ip}: {e}')