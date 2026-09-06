import os
import subprocess

from sys_check.req import req_check

if req_check("vulkaninfo") and req_check("glxinfo"):
    vulkan_summary = subprocess.run(
        ["vulkaninfo", "--summary"], check=False, capture_output=True
    ).stdout
    for line in vulkan_summary.splitlines():
        line = str(line)
        if "deviceName" in line:
            gpu_name = line.partition("= ")[2].rstrip("'")

        if "vendorID" in line:
            gpu_vendor = line.partition("= ")[2].rstrip("'")
            if gpu_vendor == "0x1002":
                gpu_vendor = "AMD"
            elif gpu_vendor == "0x8086":
                gpu_vendor = "Intel"
            elif gpu_vendor == "0x10de":
                gpu_vendor = "NVIDIA"

        if "driverInfo" in line:
            gpu_driver = f"{line.partition('= ')[2].rstrip("'")}"

        if "apiVersion" in line:
            vulkan_version = line.partition("= ")[2].rstrip("'")

        if "deviceType" in line:
            partition = line.partition("= ")[2].rstrip("'").lower()
            if "integrated" in partition:
                gpu_type = "Integrated"
            elif "discrete" in partition:
                gpu_type = "Discrete"

    glxinfo = subprocess.run(["glxinfo", "-B"], check=False, capture_output=True).stdout
    for line in glxinfo.splitlines():
        line = str(line)
        if "Dedicated video memory:" in line:
            gpu_vram = line.partition(": ")[2].rstrip("'")

        if "Max core profile version:" in line:
            opengl_version = line.partition(": ")[2].rstrip("'")


if os.path.isfile("/sys/class/drm/card1/device/power_dpm_force_performance_level"):
    with open("/sys/class/drm/card1/device/power_dpm_force_performance_level") as file:
        gpu_level = file.read().strip()
else:
    gpu_level = "N/A"


def gpu_info() -> None:
    print("GPU")
    print("......................")
    try:
        print(f"Vendor               : {gpu_vendor}")
        print(f"Name                 : {gpu_name}")
        print(f"Type                 : {gpu_type}")
        print(f"Driver               : {gpu_driver}")
        print(f"Vulkan               : {vulkan_version}")
        print(f"OpenGL               : {opengl_version}")
        print(f"VRAM                 : {gpu_vram}")
        if gpu_vendor == "AMD":
            print(f"AMDGPU Power State   : {gpu_level}")
    except NameError:
        print("Skipping GPU")
    print()
