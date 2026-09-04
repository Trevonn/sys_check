from os.path import isfile
from subprocess import run

if isfile("/usr/bin/gamescope"):
    gamescope_check = (
        str(run(["gamescope", "--version"], check=False, capture_output=True).stderr)
        .partition("version ")[2]
        .partition("(gcc")[0]
    )
else:
    gamescope_check = "Not installed"

if isfile("/usr/bin/mangohud"):
    mangohud_check = (
        str(run(["mangohud", "--version"], check=False, capture_output=True).stdout)
        .partition("v")[2]
        .strip("\\n'")
    )
else:
    mangohud_check = "Not installed"

if isfile("/usr/lib/udev/rules.d/60-steam-input.rules"):
    steam_udev = "Installed"
else:
    steam_udev = "Not installed"

lsmod = run("lsmod", check=False, capture_output=True).stdout

if "ntsync" in str(lsmod):
    ntsync_check = "Loaded"
else:
    ntsync_check = "Not loaded"

if "uinput" in str(lsmod):
    uinput_check = "Loaded"
else:
    uinput_check = "Not loaded"


def misc_info() -> None:
    print("Misc")
    print("......................")
    print(f"Mangohud             : {mangohud_check}")
    print(f"Gamescope            : {gamescope_check}")
    print(f"Steam udev rules     : {steam_udev}")
    print(f"NTSYNC               : {ntsync_check}")
    print(f"Uinput               : {uinput_check}")
