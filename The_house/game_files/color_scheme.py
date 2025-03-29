#======================================================================
# color_scheme.py
# Defines reusable color constants for the game using Colorama
#======================================================================

#Import colorama
from colorama import just_fix_windows_console, Fore, Style

#Enable Windows ANSI escape sequence support
just_fix_windows_console()

#======================================================================

#Colors
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
WHITE = Fore.WHITE

#======================================================================

#Bright Colors
BRIGHT_RED = Style.BRIGHT + Fore.RED
BRIGHT_GREEN = Style.BRIGHT + Fore.GREEN
BRIGHT_YELLOW = Style.BRIGHT + Fore.YELLOW
BRIGHT_BLUE = Style.BRIGHT + Fore.BLUE
BRIGHT_CYAN = Style.BRIGHT + Fore.CYAN
BRIGHT_MAGENTA = Style.BRIGHT + Fore.MAGENTA
BRIGHT_WHITE = Style.BRIGHT + Fore.WHITE

#======================================================================

#Style
DIM = Style.DIM
DIM_WHITE = Style.DIM + Fore.WHITE
BOLD = Style.BRIGHT

RESET = Style.RESET_ALL  #call this after printing color to reset console back to normal color

#======================================================================

#End

#======================================================================