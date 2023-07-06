import os
import platform

clear_cmd = ""

def clear_screen() -> None:
    os.system(clear_cmd)

if platform.system() != "Windows":
    clear_cmd = "clear"
else:
    clear_cmd = "cls"
    