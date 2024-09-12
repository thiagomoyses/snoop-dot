import requests
from colorama import Fore, Style

class DirBF:
    
    def __init__(self, url, wordlist_path):
        self.url = url
        self.wordlist_path = wordlist_path

    
    def get_wordlist_lines(self):

        # var tp store lines
        response = []

        with open(self.wordlist_path, 'r') as file:
            for line in file:
                if '#' not in line:
                    response.append(line.strip())


        return response
    
    def brute_force_it(self):
        wordlist = self.get_wordlist_lines()
        root_url = self.url

        for dir in wordlist:
            
            final_url = f"{root_url}/{dir}"
            print(Fore.LIGHTBLACK_EX + f'Testing {final_url}', end=' ... ' + Style.RESET_ALL)
            
            r = requests.get(final_url)

            if r.status_code == 200:
                status_color = Fore.GREEN
            else:
                status_color = Fore.RED

            print(status_color + f"{r.status_code}" + Style.RESET_ALL)
    

if __name__ == '__main__':
    runner = DirBF('https://www.google.com', '/Users/tsm-mbp/projects/paralelo/ip-sniffer/resources/wordlists/directories/directory-list-2.3-small.txt')
    runner.brute_force_it()