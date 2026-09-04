import os


def req_check(tool: str) -> bool:
    return bool(os.path.isfile(f"/usr/bin/{tool}"))
