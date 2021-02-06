from colorama import Fore, Style
from os import system, name as os_name


class color:
    def green(t: str):
        print(Fore.GREEN, t, Style.RESET_ALL)

    def red(t: str):
        print(Fore.RED, t, Style.RESET_ALL)

    def yellow(t: str):
        print(Fore.YELLOW, t, Style.RESET_ALL)


def clear():
    if os_name in ('nt', 'dos'):
        system("cls")
    elif os_name in ('linux', 'osx', 'posix'):
        system.call("clear")
    else:
        print("\n") * 120
