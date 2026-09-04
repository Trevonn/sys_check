from sys_check.cpu import cpu_info
from sys_check.gpu import gpu_info
from sys_check.misc import misc_info
from sys_check.system import system_info


def main() -> None:
    print("System Check 3.2.0")
    print()
    system_info()
    cpu_info()
    gpu_info()
    misc_info()


if __name__ == "__main__":
    main()
