import os
import platform

def clear():
    """
    Clears the terminal screen regardless of whether 
    the user is on Windows, Linux, macOS, or Android.
    """
    # Windows uses 'cls'
    if platform.system() == "Windows":
        os.system('cls')
    # Linux, macOS, and Android (Termux/Pydroid) use 'clear'
    else:
        os.system('clear')
