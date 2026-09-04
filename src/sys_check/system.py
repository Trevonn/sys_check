from os import uname
from socket import gethostbyname, gethostname
from subprocess import run

hostname = gethostname()
ip_addr = gethostbyname(hostname)
kernel = uname().release
glibc = run(["ldd", "--version"], check=False, capture_output=True)
glibc = str(glibc.stdout).split()[3].removesuffix("\\nCopyright")

with open("/proc/sys/vm/max_map_count") as file:
    max_map_count = file.read().strip()

with open("/proc/meminfo") as file:
    line = str(file.readlines(1))
    free_mem_in_kb = line.split()[1]
    ram = f"{round(float(free_mem_in_kb) / (1024 * 1024), 2)} GiB"

limit_nofile = (
    str(run(["ulimit", "-Hn"], check=False, shell=True, capture_output=True).stdout)
    .lstrip("b'")
    .rstrip("\\n'")
)


def system_info() -> None:
    print("System")
    print("......................")
    print(f"Hostname             : {hostname}")
    print(f"IP Address           : {ip_addr}")
    print(f"Kernel               : {kernel}")
    print(f"glibc                : {glibc}")
    print(f"vm.max_map_count     : {max_map_count}")
    print(f"DefaultLimitNOFILE   : {limit_nofile}")
    print(f"RAM                  : {ram}")
    print()
