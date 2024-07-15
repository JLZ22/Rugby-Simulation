def underlineText(text):
    return f"\033[4m{text}\033[0m"

def boldText(text):
    return f"\033[1m{text}\033[0m"

def printRed(*args, **kwargs):
    print(f"\033[91m", end="")
    print(*args, **kwargs)
    print(f"\033[0m", end="")

def printGreen(*args, **kwargs):
    print(f"\033[92m", end="")
    print(*args, **kwargs)
    print(f"\033[0m", end="")

def printYellow(*args, **kwargs):
    print(f"\033[93m", end="")
    print(*args, **kwargs)
    print(f"\033[0m", end="")

def printPurple(*args, **kwargs):
    print(f"\033[95m", end="")
    print(*args, **kwargs)
    print(f"\033[0m", end="")

def printCyan(*args, **kwargs):
    print(f"\033[96m", end="")
    print(*args, **kwargs)
    print(f"\033[0m", end="")

def printBlue(*args, **kwargs):
    print(f"\033[94m", end="")
    print(*args, **kwargs)
    print(f"\033[0m", end="")