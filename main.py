import argparse
from services import Scan
from colorama import init, Fore, Style
from pyfiglet import figlet_format

if __name__ == '__main__':

    title = figlet_format("IP-SNIFFER", font="starwars", width=200)
    print(Fore.GREEN + title + Style.RESET_ALL)
    print(Fore.RED + "Created by: Thiago da Silva Moyses" + Style.RESET_ALL)
    print()

    # Configura o argparse para receber o prefixo completo de IP como argumento
    parser = argparse.ArgumentParser(description="Scan network looking for active IPs")
    parser.add_argument("base_ip", help="The ip base to be scanned, with the following format x.x.0.0 (ex: 192.168.0.0)")
    args = parser.parse_args()

    scanner = Scan(args.base_ip)
    scanner.scan_network()