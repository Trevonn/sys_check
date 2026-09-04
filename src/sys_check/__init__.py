import sys

from sys_check.cpu import cpu_info
from sys_check.gpu import gpu_info
from sys_check.help import help_info
from sys_check.misc import misc_info
from sys_check.system import system_info

VERSION = "3.2.1"
ARG_LIST = ("-h", "--help", "--print")

try:
    argument = sys.argv[1]
except IndexError:
    argument = "--print"


def main() -> None:
    if argument in ("--help", "-h"):
        help_info()
    elif argument not in ARG_LIST:
        print(f"{argument} in not a valid argument")

    if argument == "--print":
        print(f"System Check {VERSION}")
        print()
        system_info()
        cpu_info()
        gpu_info()
        misc_info()


if __name__ == "__main__":
    main()
