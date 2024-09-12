from colorama import Fore, Style
from pyfiglet import figlet_format

class SubMenu01:

    def __init__(self):
        self.options = {
            "1": [
                "Directory Brute Force",
                "File Brute Force",
            ],
            "2": [
                "Active IPs Discovery"
            ]
        }

        self.menu_title = {
            "1": "DIR OPTIONS",
            "2": "IP OPTIONS"
        }
    
    def handle_sub_menu(self, option):
        if str(option) not in self.menu_title:
            print('Invalid option')
        else:
             while True:
                print(Fore.YELLOW + Style.BRIGHT + f"=== {self.menu_title[str(option)]} ===\n" + Style.RESET_ALL)
                for index, option in enumerate(self.options[str(option)], start=1):
                    print(Fore.BLUE + f"{index}. {option}" + Style.RESET_ALL)
                print(Fore.YELLOW + "================\n" + Style.RESET_ALL)
                try:
                    choice = int(input(Fore.CYAN + "Please choose an option: "))
                except ValueError:
                     print(Fore.RED + "Invalid input. Please enter a number.")
        

    def brute_force_menu(self):

        while True:
            print(Fore.YELLOW + Style.BRIGHT + "=== DIR OPTIONS ===\n" + Style.RESET_ALL)

            for index, option in enumerate(self.options["01"], start=1):
                print(Fore.BLUE + f"{index}. {option}" + Style.RESET_ALL)
            print(Fore.YELLOW + "================\n" + Style.RESET_ALL)

            try:
                choice = int(input(Fore.CYAN + "Please choose an option: "))
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")

    def handle_option(self, option):
        self.handle_sub_menu(option)