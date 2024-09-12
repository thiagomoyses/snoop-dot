from .submenus.sub_menus_01 import SubMenu01
from colorama import Fore, Style
from pyfiglet import figlet_format

class Menu:

    def __init__(self):
        self.main_options = [
            "IP-SNIFFER",
            "DIRECTORY BRUTE-FORCE"
        ]

    def main_menu(self):
        
        # Welcome
        title = figlet_format("SNOOP-DOT", font="starwars", width=200)
        print(Fore.GREEN + title + Style.RESET_ALL)
        print(Fore.BLUE + "Created by:" + Fore.RED + " Thiago da Silva Moyses" + Style.RESET_ALL)
        print(Fore.BLUE + "GitHub: " + Fore.GREEN + "https://github.com/thiagomoyses\n\n\n" + Style.RESET_ALL)

        # Choices
        while True:
            print(Fore.YELLOW + Style.BRIGHT + "=== MAIN MENU ===\n" + Style.RESET_ALL)
            for index, option in enumerate(self.main_options, start=1):
                print(Fore.BLUE + f"{index}. {option}" + Style.RESET_ALL)
            print(Fore.YELLOW + "================\n" + Style.RESET_ALL)

            try:
                choice = int(input(Fore.CYAN + "Please choose an option: "))
                runner = SubMenu01()
                runner.handle_option(choice)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")