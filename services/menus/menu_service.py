import argparse
from services import Scan
from colorama import Fore, Style
from pyfiglet import figlet_format
import sys

class Menu:

    @staticmethod
    def main_menu():
        
        # Welcome
        title = figlet_format("SNOOP-DOT", font="starwars", width=200)
        print(Fore.GREEN + title + Style.RESET_ALL)
        print(Fore.BLUE + "Created by:" + Fore.RED + " Thiago da Silva Moyses" + Style.RESET_ALL)
        print(Fore.BLUE + "GitHub: " + Fore.GREEN + "https://github.com/thiagomoyses" + Style.RESET_ALL)
        print()

        output_file = False
        netbox_output = False
        
        parser = argparse.ArgumentParser(description="Scan network looking for active IPs")
        parser.add_argument("base_ip", help="The ip base to be scanned, with the following format x.x.0.0 (ex: 192.168.0.0)")
        parser.add_argument("--output", help="Output the scan results to a file")
        parser.add_argument("--netbox", help="Output the scan results to Netbox")
        args = parser.parse_args()

        if args.output:
            if args.output == 'true':
                output_file = True
            elif args.output == 'false':
                output_file = False
            else:
                print(Fore.RED + "Invalid value for --output. Accepted values are 'true' or 'false'." + Style.RESET_ALL)
                parser.print_help()
                sys.exit(1)

        if args.netbox:
            if args.netbox == 'true':
                netbox_output = True
            elif args.netbox == 'false':
                netbox_output = False
            else:
                print(Fore.RED + "Invalid value for --netbox. Accepted values are 'true' or 'false'." + Style.RESET_ALL)
                parser.print_help()
                sys.exit(1) 

        scanner = Scan(args.base_ip, output_file, netbox_output)
        scanner.scan_network()