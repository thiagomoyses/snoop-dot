import argparse
from services import Scan
from colorama import init, Fore, Style
from pyfiglet import figlet_format
import sys

if __name__ == '__main__':

    output_file = False

    title = figlet_format("IP-SNIFFER", font="starwars", width=200)
    print(Fore.GREEN + title + Style.RESET_ALL)
    print(Fore.BLUE + "Created by:" + Fore.RED + " Thiago da Silva Moyses" + Style.RESET_ALL)
    print(Fore.BLUE + "GitHub: " + Fore.GREEN + "https://github.com/thiagomoyses" + Style.RESET_ALL)
    print()

    # Configura o argparse para receber o prefixo completo de IP como argumento
    parser = argparse.ArgumentParser(description="Scan network looking for active IPs")
    parser.add_argument("base_ip", help="The ip base to be scanned, with the following format x.x.0.0 (ex: 192.168.0.0)")
    parser.add_argument("--output", help="Output the scan results to a file")
    args = parser.parse_args()

    if args.output == 'true':
        output_file = True
    elif args.output == 'false':
        output_file = False
    else:
        print(Fore.RED + "Invalid value for --output. Accepted values are 'true' or 'false'." + Style.RESET_ALL)
        parser.print_help()
        sys.exit(1)
        

    scanner = Scan(args.base_ip, output_file)
    scanner.scan_network()