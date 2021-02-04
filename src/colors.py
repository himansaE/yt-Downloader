from colorama import Fore, Style


class color:
    def green(t):
        print(Fore.GREEN, t, Style.RESET_ALL)

    def red(t):
        print(Fore.RED, t, Style.RESET_ALL)

    def yellow(t):
        print(Fore.YELLOW, t, Style.RESET_ALL)
