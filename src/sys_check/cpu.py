import os
import subprocess

clocksource_file = "/sys/devices/system/clocksource/clocksource0/current_clocksource"
cpu_freq_dir = "/sys/devices/system/cpu/cpu0/cpufreq/"
epp_dir = f"{cpu_freq_dir}/energy_performance_preference"

with open("/proc/cpuinfo") as file:
    for line in file:
        if "model name" in line:
            cpu_name = line.partition(": ")[2].strip()
        elif "cpu cores" in line:
            cpu_cores = line.partition(": ")[2].strip()
        elif "siblings" in line:
            cpu_threads = line.partition(": ")[2].strip()
        elif "vendor_id" in line:
            cpu_vendor = line.partition(": ")[2].strip()
            match cpu_vendor:
                case "AuthenticAMD":
                    cpu_vendor = "AMD"
                case "AuthenticIntel":
                    cpu_vendor = "Intel"
                case _:
                    cpu_vendor = "Unknown"

sensors = subprocess.run("sensors", check=False, capture_output=True).stdout
for line in sensors.splitlines():
    line = str(line)
    if "Tctl" in line:
        cpu_temp = line.partition("+")[2]

with open(f"{cpu_freq_dir}/scaling_governor") as file:
    cpu_gov = file.read().strip()

with open(f"{cpu_freq_dir}/scaling_driver") as file:
    cpu_driver = file.read().strip()

with open(f"{cpu_freq_dir}/boost") as file:
    value = file.read().strip()
    if value == "0":
        cpu_boost = "Off"
    elif value == "1":
        cpu_boost = "On"

with open("/sys/devices/system/cpu/amd_pstate/status") as file:
    amd_pstate = file.read().strip()

if os.path.isfile(epp_dir):
    with open(epp_dir) as file:
        epp_pref = file.read().strip()
else:
    epp_pref = "N/A"

with open(clocksource_file) as file:
    clocksource = file.read().strip()


def cpu_info() -> None:
    print("CPU")
    print("......................")
    print(f"Vendor               : {cpu_vendor}")
    print(f"Name                 : {cpu_name}")
    # print(f"Temperature          : {cpu_temp}")
    print(f"Cores                : {cpu_cores}")
    print(f"Threads              : {cpu_threads}")
    print(f"Governor             : {cpu_gov}")
    print(f"Driver               : {cpu_driver}")
    print(f"Turbo Boost          : {cpu_boost}")
    if cpu_vendor == "AMD":
        print(f"AMD P-State Mode     : {amd_pstate}")
    print(f"EPP Preference       : {epp_pref}")
    print(f"Clocksource          : {clocksource}")
    print()
