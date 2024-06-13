def underlineText(text):
    return f"\033[4m{text}\033[0m"

def boldText(text):
    return f"\033[1m{text}\033[0m"

def printRed(text):
    print(f"\033[91m{text}\033[0m")

def printGreen(text):
    print(f"\033[92m{text}\033[0m")

def printYellow(text):
    print(f"\033[93m{text}\033[0m")

def printPurple(text):
    print(f"\033[95m{text}\033[0m")

def printCyan(text):
    print(f"\033[96m{text}\033[0m")

def printBlue(text):
    print(f"\033[94m{text}\033[0m")