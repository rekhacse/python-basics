from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()

# then use Termcolor for all colored text output
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Fore.RESET + Back.RESET + Style.RESET_ALL)
print('back to normal now')
print(colored('Hello, World!', 'green', 'on_red'))
print("\033[6;3HHello")
