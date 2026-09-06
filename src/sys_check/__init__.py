import platform
import sys

from sys_check.cpu import cpu_info
from sys_check.gpu import gpu_info
from sys_check.help import help_info
from sys_check.misc import misc_info
from sys_check.system import system_info

if platform.system() != "Linux":
    print("This program only runs on Linux systems. Exiting")
    sys.exit()


VERSION = "3.3.1"

try:
    argument = sys.argv[1]
except IndexError:
    argument = "--print"


def main() -> None:
    if argument == "--help":
        help_info()
    elif argument == "--print":
        print(f"System Check {VERSION}")
        print()
        system_info()
        cpu_info()
        gpu_info()
        misc_info()
    elif argument == "--headless":
        print(f"System Check {VERSION}")
        print()
        system_info()
        cpu_info()
    else:
        print(f"{argument} in not a valid argument")


if __name__ == "__main__":
    main()
