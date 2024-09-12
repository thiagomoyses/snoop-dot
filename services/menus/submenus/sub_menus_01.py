from colorama import Fore, Style
from pyfiglet import figlet_format

class SubMenu01:

    def __init__(self):
        self.options = {
            "01": [
                "Directory Brute Force",
                "File Brute Force",
            ],
        }

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
        match option:
            case 2:
                self.brute_force_menu()
            
            case _:
                print('Invalid Option')