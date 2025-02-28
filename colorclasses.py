################################
# Header

__package_name__ = "colorclasses"
__version__ = "v1.1"
__license__ = "Unlicense"

__author__ = "mkow04"
__email__ = "maciejkowalski04@proton.me"

__all__ = ["Color", "Background", "Effect"]

################################
# Imports

from enum import Enum
import sys
import os


################################
# Checks

def supports_color() -> bool:
    if (not sys.stdout.isatty()) or os.getenv("TERM", "dumb") == "dumb":
        return False
    else:
        return True


################################
# Classes

class BaseColorEnum(Enum):
    def __str__(self):
        if supports_color():
            return str(self.value)
        else:
            return ""


class Color(BaseColorEnum):
    BLACK = "\033[30m"
    DARK_RED = "\033[31m"
    DARK_GREEN = "\033[32m"
    DARK_YELLOW = "\033[33m"
    DARK_BLUE = "\033[34m"
    DARK_MAGENTA = "\033[35m"
    DARK_CYAN = "\033[36m"
    GRAY = "\033[37m"
    DARK_GRAY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"


class Background(BaseColorEnum):
    BLACK = "\033[40m"
    DARK_RED = "\033[41m"
    DARK_GREEN = "\033[42m"
    DARK_YELLOW = "\033[43m"
    DARK_BLUE = "\033[44m"
    DARK_MAGENTA = "\033[45m"
    DARK_CYAN = "\033[46m"
    GRAY = "\033[47m"
    DARK_GRAY = "\033[100m"
    RED = "\033[101m"
    GREEN = "\033[102m"
    YELLOW = "\033[103m"
    BLUE = "\033[104m"
    MAGENTA = "\033[105m"
    CYAN = "\033[106m"
    WHITE = "\033[107m"


class Effect(BaseColorEnum):
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DARK = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    RAPID_BLINK = "\033[6m"
    REVERSE = "\033[7m"
    OBFUSCATE = "\033[8m"
    STRIKETHROUGH = "\033[9m"


################################
# Main run
# Shows an example of all colors

def main():
    line0 = f"{Color.CYAN}{Effect.BOLD}{__package_name__.capitalize()}  {Effect.RESET}{Effect.BOLD}{Effect.ITALIC}{__version__} {Effect.RESET}"
    line1 = f"{Color.CYAN}{Effect.BOLD}Author:{Effect.RESET} {__author__} {Effect.ITALIC}<{__email__}>{Effect.RESET}"

    lenght = 48

    print()

    print(f"{Color.DARK_CYAN}{'*'*(lenght)}{Effect.RESET}")
    print(f" {line0}")
    print(f" {line1}")
    print(f"{Color.DARK_CYAN}{'*'*(lenght)}{Effect.RESET}")

    print(f"\n{Color.CYAN}{Effect.BOLD} List of all possible formatting options:{Effect.RESET}")

    for item in [Color, Background, Effect]:
        print(f"\n{' '*5}{Color.DARK_CYAN}{Effect.BOLD}{item.__name__}s:{Effect.RESET}")

        for member in item:
            display_name = member.name.replace("_", " ").capitalize()
            callable_name = f"{item.__name__}.{member.name}"
            max_lenght = len(item.__name__)+15
            print(f"{' '*9}{Effect.BOLD}{callable_name:<{max_lenght}}-> {Effect.RESET}{member}{display_name}{Effect.RESET}")

    print("")


if __name__ == "__main__":
    main()
